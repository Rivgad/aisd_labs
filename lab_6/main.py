from timeit import default_timer as timer
from functions import (
    generate_random_array,
    benchmark_function,
    bubble_sort,
    heap_sort,
    quick_sort,
    selection_sort,
    insertion_sort,
    shell_sort,
)


if __name__ == "__main__":
    method_names = [
        "Cортировка обменом",
        "Сортировка выбором",
        "Сортировка вставками",
        "Сортировка Шелла",
        "Быстрая сортировка",
        "Пирамидальная сортировка",
    ]
    for i in range(len(method_names)):
        print(f"{i + 1}) {method_names[i]}")
    choice = int(input("Выберите метод сортировки: ")) - 1
    method = method_names[choice]

    array_size = int(input("Введите размер массива: "))
    if array_size > 10000:
        array_size = 10000
    array = generate_random_array(array_size)
    print("Размер массива:", array_size)

    # Выполнение сортировки выбранным методом
    if method == method_names[0]:
        result = benchmark_function(array, bubble_sort)
    elif method == method_names[1]:
        result = benchmark_function(array, selection_sort)
    elif method == method_names[2]:
        result = benchmark_function(array, insertion_sort)
    elif method == method_names[3]:
        result = benchmark_function(array, shell_sort)
    elif method == method_names[4]:
        result = benchmark_function(array, quick_sort)
    elif method == method_names[5]:
        result = benchmark_function(array, heap_sort)

    print(f"{method} выполнил за {result} секунд.")
