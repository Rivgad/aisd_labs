from functions import (
    generate_random_array,
    bubble_sort,
    selection_sort,
    insertion_sort,
)
from timeit import default_timer as timer


def benchmark_function(array: list, function):
    arr_copy = array.copy()
    start = timer()
    function(arr_copy)
    end = timer()
    return round(end - start, 4)


if __name__ == "__main__":
    array_sizes = [10, 100, 1000, 10000]
    methods_list = [
        "Cортировка обменом",
        "Сортировка выбором",
        "Сортировка вставками",
    ]
    data = [[0 for _ in range(len(methods_list))] for _ in range(len(array_sizes))]

    print(f"Benchmark start...")
    for index in range(len(array_sizes)):
        array_size = array_sizes[index]
        array = generate_random_array(array_size)

        data[index][0] = benchmark_function(array, bubble_sort)
        data[index][1] = benchmark_function(array, selection_sort)
        data[index][2] = benchmark_function(array, insertion_sort)

    row_format = "{:>15}" + "{:>25}" * (len(methods_list))
    print(row_format.format("Размер массива", *methods_list))

    for item, row in zip(array_sizes, data):
        print(row_format.format(item, *row))
