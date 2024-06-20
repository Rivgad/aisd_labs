import os
from dataclasses import dataclass, field
from typing import Self


@dataclass
class Element:
    val: int | None = field(default=None)
    next: Self | None = field(default=None)


class SubList:
    _head: Element
    _tail: Element
    _count: int = 0
    next: Self | None = None

    def __init__(self):
        self._head = Element()
        self._tail = self._head

    def first(self) -> Element | None:
        return self._head.next

    def empty(self) -> bool:
        return self._count == 0

    def append(self, val: int):
        self._tail.next = Element(val)
        self._tail = self._tail.next
        self._count += 1

    def remove(self):
        if self.empty():
            return False

        current = self._head

        while current.next is not self._tail:
            current = current.next

        current.next = None
        self._tail = current
        self._count -= 1

        return True

    def __iter__(self):
        current = self._head.next
        while current is not None:
            yield current
            current = current.next


class ListsList:
    _head: SubList
    _tail: SubList
    _count: int = 0

    def __init__(self) -> None:
        self._head = SubList()
        self._tail = self._head

    def empty(self):
        return self._count == 0

    def append(self):
        self._tail.next = SubList()
        self._tail = self._tail.next
        self._count += 1

    def find(self, item: int) -> tuple[int, int]:
        main = self._head.next
        i = 0
        while main is not None:
            sub = main.first()
            j = 0
            while sub is not None:
                if sub.val == item:
                    return (i, j)

                sub = sub.next
                j += 1

            main = main.next
            i += 1

        return (-1, -1)

    def exist(self, item: int) -> bool:
        main = self._head.next

        while main is not None:
            sub = main.first()
            while sub is not None:
                if sub.val == item:
                    return True

                sub = sub.next
            main = main.next

        return False

    def sub_append(self, val: int, index: int = -1):
        if self.empty():
            self.append()

        if index != -1:
            current = self._head.next
            for _ in range(index):
                current = current.next
                if current is None:
                    return False
        else:
            current = self._tail

        current.append(val)
        return True

    def remove(self):
        if self.empty():
            return False

        current = self._head

        while current.next is not self._tail:
            current = current.next

        current.next = None
        self._tail = current
        self._count -= 1

        return True

    def sub_remove(self, index: int = -1):
        if self.empty():
            return False

        if index == -1:
            current = self._tail
        else:
            current = self._head
            for _ in range(index + 1):
                current = current.next

                if current is None:
                    return False

        return current.remove()

    def __iter__(self):
        current = self._head.next

        while current is not None:
            yield current
            current = current.next

    def __str__(self) -> str:
        arr = []

        for sub in self:
            s = f"  {[x.val for x in sub]}"
            arr.append(s)

        return "[\n" + ",\n".join(arr) + "\n]"


def run_command(l: ListsList, command: str):
    match command:
        case "1":
            print(f"Текущее состояние:\n{l}")

        case "2":
            item = int(input("Введите искомый элемент: "))
            res = l.find(item)
            res = f"элемент существует в списке {res[0]}, индекс {res[1]}" if res[0] != -1 else f"элемент не найден"

            print(f"Результат поиска: {res}")

        case "3":
            l.append()
            print("Список добавлен")

        case "4":
            index = None if l.empty() else int(input("Введите номер списка: "))
            item = int(input("Введите элемент: "))

            res = l.sub_append(item, index)

            print("Элемент добавлен" if res else "Не удалось вставить элемент")

        case "5":
            res = l.remove()

            print("Список удален" if res else "Не удалось удалить список")

        case "6":
            index = int(input("Введите номер списка: "))
            res = l.sub_remove(index)

            print("Элемент удален" if res else "Не удалось удалить элемент")

        case _:
            print("Неверно выбрано действие")


if __name__ == "__main__":
    l = ListsList()
    l.append()
    l.sub_append(1)
    l.sub_append(2)
    l.append()
    l.sub_append(3)
    l.sub_append(4)
    l.append()
    l.append()
    l.sub_append(6)
    l.sub_append(7)

    while True:
        print("1. Проход по структуре")
        print("2. Поиск")
        print("3. Добавить список")
        print("4. Добавить элемент")
        print("5. Удалить список")
        print("6. Удалить элемент")

        command = input("Выберите: ")
        os.system("cls")

        run_command(l, command)

        print()
