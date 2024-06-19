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

    def empty(self) -> bool:
        return self._count == 0

    def append(self, val: int):
        self._tail.next = Element(val)
        self._tail = self._tail.next
        self._count += 1

    def remove(self):
        current = self._head

        while current.next is not self._tail:
            current = current.next

        current.next = None
        self._count -= 1

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
        current = self._head

        while current.next is not self._tail:
            current = current.next

        current.next = None
        self._count -= 1

    def sub_remove(self, index: int = -1):
        if self.empty():
            return False
        
        



def run_command(l: ListsList, command: str):
    match command:
        case "1":
            print(f"Текущее состояние: {list(l)}")

        case "2":
            item = int(input("Введите искомый элемент: "))

            res = (
                "элемент существует"
                if l.exist(item)
                else f"элемент не найден"
            )

            print(f"Результат поиска: {res}")

        case "3":
            l.append()

            print("Список добавлен")

        case "4":
            find_elem = None if l.empty() else int(input("Введите номер списка: "))
            item = int(input("Введите элемент: "))

            res = l.append(item, find_elem)

            print("Элемент добавлен" if res else "Не удалось вставить элемент")

        case "5":
            find_elem = int(input("Введите номер списка: "))
            res = l.remove(find_elem)

            print("Список удален" if res else "Не удалось удалить список")

        case "6":
            find_elem = None if l.empty() else int(input("Введите номер списка: "))
            item = int(input("Введите элемент: "))

            res = l.remove(item, find_elem)

            print("Элемент добавлен" if res else "Не удалось вставить элемент")

        case _:
            print("Неверно выбрано действие")


if __name__ == "__main__":
    # stack = ListsList()

    while True:
        print("1. Проход по структуре")
        print("2. Поиск")
        print("3. Добавить список")
        print("4. Добавить элемент")
        print("5. Удалить список")
        print("6. Удалить элемент")

        command = input("Выберите: ")
        os.system("cls")

        # run_command(stack, command)

        print()
