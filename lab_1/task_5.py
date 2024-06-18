import os
from array import array
from itertools import chain


class Queue:
    _arr: array
    _size: int
    _count: int = 0
    _first: int = 0
    _last: int = 0
    
    def __init__(self, size: int = 10):
        self._arr = array("q", [0 for _ in range(size)])
        self._size = size

    def empty(self):
        return self._count == 0

    def full(self):
        return self._count == self._size

    def put(self, num: int) -> bool:
        if self.full():
            return False

        self._arr[self._last] = num
        self._last += 1

        if self._last > self._size - 1:
            self._last = 0

        self._count += 1
        return True

    def get(self) -> int | None:
        if self.empty():
            return None

        elem = self._arr[self._first]
        self._first += 1
        if self._first > self._size - 1:
            self._first = 0
        
        self._count -= 1
        return elem

    def __str__(self) -> str:
        if self._first >= self._last and not self.empty():
            r = chain(range(self._first, self._size), range(0, self._last))
        else:
            r = range(self._first, self._last)
        
        return "[" + ", ".join([str(self._arr[i]) for i in r]) + "]"


def run_command(queue: Queue, command: str):
    match command:
        case "1":
            print(f"Пустота: {queue.empty()}")

        case "2":
            print(f"Заполненность: {queue.full()}")

        case "3":
            elem = input("Введите элемент (целочисленное): ")
            if not elem.isnumeric():
                print("Элемент не является числом")
            else:
                if queue.put(int(elem)):
                    print("Элемент успешно добавлен")
                else:
                    print("Очередь заполнена")

        case "4":
            elem = queue.get()
            if elem:
                print(f"Удален элемент: {elem}")
            else:
                print("Очередь пуста")

        case "5":
            print(f"Текущее состояние: {queue}")

        case _:
            print("Неверно выбрано действие")



if __name__ == "__main__":
    print([1,2,3] + [4,5,6])
    size = input("Введите максимальный размер очереди (по-умолчанию 10): ")
    size = 10 if not size.isnumeric() else int(size)
    print(f"Максимальный размер: {size} элементов")

    queue = Queue(size=size)

    while True:
        print("1. Проверить пустоту")
        print("2. Проверить заполненность")
        print("3. Добавление элемента")
        print("4. Удаление элемента")
        print("5. Вывод текущего состояния")
        command = input("Выберите: ")
        os.system("cls")

        run_command(queue, command)

        print()
