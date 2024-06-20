import os
from typing import Self
from dataclasses import dataclass, field


@dataclass
class Elem:
    val: int | None
    left: Self | None = field(default=None)
    right: Self | None = field(default=None)


class LinkedList:
    _head: Elem
    _count: int = 0

    def __init__(self):
        self._head = Elem(val=None)
        self._head.left = self._head
        self._head.right = self._head

    def empty(self) -> bool:
        return self._count == 0

    def find_forward(self, item: int) -> Elem | None:
        current = self._head.right

        while current is not self._head and current.val != item:
            current = current.right

        return current if current is not self._head else None

    def find_backward(self, item: int) -> Elem | None:
        current = self._head.left

        while current is not self._head and current.val != item:
            current = current.left

        return current if current is not self._head else None

    def exist_forward(self, item: int) -> bool:
        return self.find_forward(item) is not None

    def exist_backward(self, item: int) -> bool:
        return self.find_backward(item) is not None

    def insert_before(self, item: int, find_item: int) -> bool:
        current = self.find_forward(find_item)

        if current is None:
            return False

        temp = Elem(val=item, left=current.left, right=current)
        current.left.right = temp
        current.left = temp
        self._count += 1

        return True

    def insert_after(self, item: int, find_item: int) -> bool:
        current = self._head if self.empty() else self.find_forward(find_item)

        if current is None:
            return False

        temp = Elem(val=item, left=current, right=current.right)
        current.right.left = temp
        current.right = temp
        self._count += 1

        return True

    def remove(self, find_item: int):
        current = self.find_forward(find_item)

        if current is None:
            return False

        current.left.right = current.right
        current.right.left = current.left
        self._count -= 1

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
            print("1. Прямое направление")
            print("2. Обратное направление")

            direction = input("Выберите направление: ")
            item = int(input("Введите искомый элемент: "))

            match direction:
                case "1":
                    res = (
                        "элемент существует"
                        if l.exist_forward(item)
                        else f"элемент не найден"
                    )
                    res = f"Результат поиска: {res}"
                case "2":
                    res = (
                        "элемент существует"
                        if l.exist_backward(item)
                        else f"элемент не найден"
                    )
                    res = f"Результат поиска: {res}"
                case _:
                    res = "Неверно выбрано действие"

            print(res)

        case "3":
            item = int(input("Введите элемент: "))
            find_elem = int(input("Введите искомый элемент: "))
            res = l.insert_before(item, find_elem)

            print("Элемент добавлен" if res else "Не удалось вставить элемент")

        case "4":
            item = int(input("Введите элемент: "))
            find_elem = None if l.empty() else int(input("Введите искомый элемент: "))

            res = l.insert_after(item, find_elem)

            print("Элемент добавлен" if res else "Не удалось вставить элемент")

        case "5":
            find_elem = int(input("Введите искомый элемент: "))
            res = l.remove(find_elem)

            print("Элемент удален" if res else "Не удалось удалить элемент")

        case _:
            print("Неверно выбрано действие")


if __name__ == "__main__":
    l = LinkedList()

    while True:
        print("1. Вывод текущего состояния")
        print("2. Поиск")
        print("3. Добавить перед")
        print("4. Добавить после")
        print("5. Удаление")

        command = input("Выберите: ")
        os.system("cls")

        run_command(l, command)

        print()
