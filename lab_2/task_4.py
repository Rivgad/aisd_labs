import os
from typing import Self
from dataclasses import dataclass, field


@dataclass
class Elem:
    val: int
    next: Self | None = field(default=None)


class LinkedList:
    _head: Elem
    _tail: Elem

    def __init__(self):
        self._head = Elem(val=0)
        self._tail = self._head

    def exist(self, item: int) -> bool:
        current = self._head.next

        while current is not None and current.val != item:
            current = current.next

        return current is None

    def append(self, item: int):
        temp = Elem(val=item)
        self._tail.next = temp
        self._tail = temp

    def insert_before(self, item: int, find_item: int) -> bool:
        prev = self._head
        current = prev.next

        while current is not None and current.val != find_item:
            prev = current
            current = prev.next

        if current is None:
            return False

        temp = Elem(val=item)
        prev.next = temp
        temp.next = current

        return True

    def insert_after(self, item: int, find_item: int) -> bool:
        if self._head.next is None:
            self.append(item)
            return True

        prev = self._head
        current = prev.next

        while current is not None and current.val != find_item:
            prev = current
            current = prev.next

        if current is None:
            return False

        temp = Elem(val=item)
        temp.next = current.next
        current.next = temp

        if current.next is None:
            self._tail = current

        return True

    def delete(self, find_item: int):
        prev = self._head
        current = prev.next

        while current is not None and current.val != find_item:
            prev = current
            current = prev.next

        if current is None:
            return False

        prev.next = current.next

        if prev.next is None:
            self._tail = prev

        return True

    def __str__(self) -> str:
        arr = []
        current = self._head.next

        while current is not None:
            arr.append(str(current.val))
            current = current.next

        return "[" + ", ".join([str(x) for x in arr]) + "]"


def run_command(l: LinkedList, command: str):
    match command:
        case "1":
            print(f"Текущее состояние: {l}")

        case "2":
            item = int(input("Введите искомый элемент: "))
            res = "элемент не найден" if l.exist(item) == -1 else f"элемент найден"

            print(f"Результат поиска: {res}")

        case "3":
            item = int(input("Введите элемент: "))
            l.append(item)
            print("Элемент добавлен")

        case "4":
            find_elem = int(input("Введите искомый элемент: "))
            item = int(input("Введите элемент: "))
            res = l.insert_before(item, find_elem)

            print("Элемент добавлен" if res else "Не удалось вставить элемент")

        case "5":
            find_elem = int(input("Введите искомый элемент: "))
            item = int(input("Введите элемент: "))
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
