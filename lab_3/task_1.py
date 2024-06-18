import os
from typing import Self
from dataclasses import dataclass, field


class LinkedList:
    @dataclass
    class Elem:
        val: int
        left: Self | None = field(default=None)
        right: Self | None = field(default=None)

    _head: Elem
    _last: Elem

    def __init__(self):
        self._head = self.Elem(val=0)
        self._head.left = self._head
        self._head.right = self._head
        
        self._last = self._head

    def find(self, item: int) -> Elem | None:
        current = self._head.right

        while current is not self._head and current.val != item:
            current = current.right

        return current if current is not self._head else None

    def exist(self, item: int) -> bool:
        return self.find(item) is None

    def append(self, item: int):
        temp = self.Elem(val=item, left=self._last, right=self._head)
        self._last.right = temp
        self._head.left = temp
        self._last = temp

    def insert_before(self, item: int, find_item: int) -> bool:
        prev = self._head
        current = prev.right

        while current is not None and current.val != find_item:
            prev = current
            current = prev.right

        if current is None:
            return False

        temp = self.Elem(val=item)
        prev.right = temp
        temp.right = current

        return True

    def insert_after(self, item: int, find_item: int) -> bool:
        prev = self._head
        current = prev.right

        while current is not None and current.val != find_item:
            prev = current
            current = prev.right

        if current is None:
            return False

        temp = self.Elem(val=item)
        temp.right = current.right
        current.right = temp

        if current.right is None:
            self._tail = current

        return True

    def delete(self, find_item: int):
        prev = self._head
        current = prev.right

        while current is not None and current.val != find_item:
            prev = current
            current = prev.right

        if current is None:
            return False

        prev.right = current.right

        if prev.right is None:
            self._tail = prev

        return True
    
    def iter_forward(self):
        current = self._head.right

        while current is not self._head:
            yield current.val
            current = current.right
    
    def iter_backward(self):
        current = self._head.left

        while current is not self._head:
            yield current.val
            current = current.left

    def __str__(self) -> str:
        return "[" + ", ".join([str(x) for x in self.iter_forward()]) + "]"


def run_command(l: LinkedList, command: str):
    match command:
        case "1":
            print("1. Прямое направление")
            print("2. Обратное направление")

            match input("Выберите направление: "):
                case "1":
                    print(f"Текущее состояние: {list(l.iter_forward())}")
                case "2":
                    print(f"Текущее состояние: {list(l.iter_backward())}")
                case _:
                    print("Неверно выбрано действие")

        case "2":
            item = int(input("Введите искомый элемент: "))
            res = "элемент существует" if l.exist(item) else f"элемент не найден"

            print(f"Результат поиска: {res}")

        case "3":
            item = int(input("Введите элемент: "))
            l.append(item)
            print("Элемент добавлен")

        case "4":
            item = int(input("Введите элемент: "))
            find_elem = int(input("Введите искомый элемент: "))
            res = l.insert_before(item, find_elem)

            print("Элемент добавлен" if res else "Не удалось вставить элемент")

        case "5":
            item = int(input("Введите элемент: "))
            find_elem = int(input("Введите искомый элемент: "))
            res = l.insert_after(item, find_elem)

            print("Элемент добавлен" if res else "Не удалось вставить элемент")

        case "6":
            find_elem = int(input("Введите искомый элемент: "))
            res = l.delete(find_elem)

            print("Элемент удален" if res else "Не удалось удалить элемент")

        case _:
            print("Неверно выбрано действие")


if __name__ == "__main__":
    stack = LinkedList()

    while True:
        print("1. Вывод текущего состояния")
        print("2. Поиск")
        print("3. Добавить")
        print("4. Вставка перед")
        print("5. Вставка после")
        print("6. Удаление")

        command = input("Выберите: ")
        os.system("cls")

        run_command(stack, command)

        print()
