import os
from array import array


class List:
    _arr: array
    _size: int
    _count: int = 0

    def __init__(self, size):
        self._size = size
        self._arr = array("q", [0 for _ in range(size)])

    def empty(self):
        return self._count == 0

    def full(self):
        return self._count == self._size

    def find(self, item: int) -> int:
        for i in range(self._count):
            if self._arr[i] == item:
                return i

        return -1

    def add(self, item: int) -> bool:
        if self.full():
            return False

        self._arr[self._count] = item
        self._count += 1

        return True

    def insert_before(self, item: int, find_item: int) -> bool:
        index = self.find(find_item)

        if index == -1 or self.empty() or self.full():
            return False

        for i in range(self._count - 1, index - 1, -1):
            self._arr[i + 1] = self._arr[i]

        self._arr[index] = item
        self._count += 1

        return True

    def insert_after(self, item: int, find_item: int) -> bool:
        index = self.find(find_item)

        if index == -1 or self.empty() or self.full():
            return False

        for i in range(self._count - 1, index, -1):
            self._arr[i + 1] = self._arr[i]

        self._arr[index + 1] = item
        self._count += 1

        return True

    def delete(self, find_item: int) -> bool:
        index = self.find(find_item)

        if index == -1:
            return False

        for i in range(index, self._count - 1, 1):
            self._arr[i] = self._arr[i + 1]

        self._count -= 1

        return True

    def __str__(self) -> str:
        return "[" + ", ".join([str(self._arr[i]) for i in range(self._count)]) + "]"


def run_command(l: List, command: str):
    match command:
        case "1":
            print(f"Текущее состояние: {l}")

        case "2":
            item = int(input("Введите искомый элемент: "))

            index = l.find(item)
            res = (
                "элемент не найден"
                if index == -1
                else f"индекс искомого элемента = {index}"
            )

            print(f"Результат поиска: {res}")

        case "3":
            item = int(input("Введите элемент: "))
            res = l.add(item)
            print("Элемент добавлен" if res else "Не удалось вставить элемент")

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
    size = input("Введите размер стека (по-умолчанию 10): ")
    size = 10 if not size.isnumeric() else int(size)
    print(f"Размер стека: {size} элементов")

    stack = List(size=size)

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
