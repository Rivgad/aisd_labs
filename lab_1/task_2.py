import os
from typing import Self
from dataclasses import dataclass, field

@dataclass
class Elem:
    val: int
    next: Self | None = field(default=None)


class Stack:
    _sp: Elem | None = None

    def is_empty(self):
        return self._sp is None

    def push(self, num: int):
        self._sp = Elem(val=num, next=self._sp)
    
    def pop(self) -> int | None:
        if self._sp is None:
            return None
        
        val = self._sp.val
        self._sp = self._sp.next
        return val
    
    def __str__(self) -> str:
        curr = self._sp
        res: list[str] = []
        while curr is not None:
            res.append(str(curr.val))
            curr = curr.next

        return "[" + ", ".join(reversed(res)) + "]"
    
def  run_command(stack: Stack, command: str):
    match command:
        case "1":
            print(f"Пустота стека: {stack.is_empty()}")
        
        case "2":
            elem = input("Введите элемент (целочисленное): ")
            if not elem.isnumeric():
                print("Элемент не является числом")
            else:
                stack.push(int(elem))
                print("Элемент успешно добавлен")
        
        case "3":
            elem = stack.pop()
            if elem:
                print(f"Удален элемент: {elem}")
            else:
                print("Стек пуст")
        
        case "4":
            print(f"Текущее состояние: {stack}")
        
        case _:
            print("Неверно выбрано действие")

if __name__ == "__main__":
    stack = Stack()

    while True:
        print("1. Проверить пустоту")
        print("2. Добавление элемента")
        print("3. Удаление элемента")
        print("4. Вывод текущего состояния")
        command = input("Выберите: ")
        os.system("cls")

        run_command(stack, command)

        print()
            

                