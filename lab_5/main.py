from timeit import default_timer as timer
from functions import (
    generate_random_array,
    bubble_sort,
    selection_sort,
    insertion_sort,
)


if __name__ == "__main__":
    method_names = [
        "Cортировка обменом (метод пузырька)",
        "Сортировка выбором",
        "Сортировка вставками",
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
    arr_copy = array.copy()
    start = timer()
    if method == method_names[0]:
        swaps = bubble_sort(arr_copy)
    elif method == method_names[1]:
        swaps = selection_sort(arr_copy)
    elif method == method_names[2]:
        swaps = insertion_sort(arr_copy)

    end = timer()

    print(f"{method} выполнил {swaps} пересылок за {end - start} секунд.")
