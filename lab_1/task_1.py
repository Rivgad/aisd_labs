from array import array
import os


class Stack:
    _arr: array
    _sp: int = 0

    def __init__(self, size: int = 10):
        self._arr = array("q", [0 for _ in range(size)])
        self._max_sp = size - 1

    def is_empty(self):
        return self._sp == 0

    def is_full(self):
        return self._sp == self._max_sp

    def push(self, num: int) -> bool:
        if self.is_full():
            return False

        self._arr[self._sp] = num
        self._sp += 1

        return True

    def pop(self) -> int | None:
        if self.is_empty():
            return None

        self._sp -= 1
        return self._arr[self._sp]

    def __str__(self) -> str:
        return "[" + ", ".join([str(self._arr[i]) for i in range(self._sp)]) + "]"


def run_command(stack: Stack, command: str):
    match command:
        case "1":
            print(f"Пустота стека: {stack.is_empty()}")

        case "2":
            print(f"Заполненность стек: {stack.is_full()}")

        case "3":
            elem = input("Введите элемент (целочисленное): ")
            if not elem.isnumeric():
                print("Элемент не является числом")
            else:
                if stack.push(int(elem)):
                    print("Элемент успешно добавлен")
                else:
                    print("Стек полон")

        case "4":
            elem = stack.pop()
            if elem:
                print(f"Удален элемент: {elem}")
            else:
                print("Стек пуст")

        case "5":
            print(f"Текущее состояние: {stack}")

        case _:
            print("Неверно выбрано действие")


if __name__ == "__main__":
    size = input("Введите размер стека (по-умолчанию 10): ")
    size = 10 if not size.isnumeric() else int(size)
    print(f"Размер стека: {size} элементов")

    stack = Stack(size=size)

    while True:
        print("1. Проверить пустоту")
        print("2. Проверить заполненность")
        print("3. Добавление элемента")
        print("4. Удаление элемента")
        print("5. Вывод текущего состояния")
        command = input("Выберите: ")
        os.system("cls")

        run_command(stack, command)

        print()
