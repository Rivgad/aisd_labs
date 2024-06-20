import os
from typing import Self
from dataclasses import dataclass, field


@dataclass
class Elem:
    val: int
    next: Self | None = field(default=None)


class Queue:
    _count: int = 0
    _first: Elem
    _last: Elem
    
    def __init__(self):
        elem = Elem(val=0)
        self._first = elem
        self._last = self._first

    def empty(self):
        return self._first.next is None

    def put(self, num: int):
        temp = Elem(val=num)
        self._last.next = temp
        self._last = temp

        self._count += 1

    def get(self) -> int | None:
        if self.empty():
            return None
        
        temp = self._first.next
        self._first.next = temp.next
        
        if self.empty():
            self._last = self._first
            
        return temp.val

    def __str__(self) -> str:
        arr = []
        temp = self._first.next
        
        while temp is not None:
            arr.append(str(temp.val))
            temp = temp.next

        return "[" + ", ".join(arr) + "]"


def run_command(queue: Queue, command: str):
    match command:
        case "1":
            print(f"Пустота: {queue.empty()}")

        case "2":
            elem = input("Введите элемент (целочисленное): ")
            if not elem.isnumeric():
                print("Элемент не является числом")
            else:
                queue.put(int(elem))
                print("Элемент успешно добавлен")

        case "3":
            elem = queue.get()
            if elem:
                print(f"Удален элемент: {elem}")
            else:
                print("Очередь пуста")

        case "4":
            print(f"Текущее состояние: {queue}")

        case _:
            print("Неверно выбрано действие")



if __name__ == "__main__":
    queue = Queue()

    while True:
        print("1. Проверить пустоту")
        print("2. Добавление элемента")
        print("3. Удаление элемента")
        print("4. Вывод текущего состояния")
        command = input("Выберите: ")
        os.system("cls")

        run_command(queue, command)

        print()
