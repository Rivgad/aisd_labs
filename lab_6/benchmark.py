from functions import (
    generate_random_array,
    bubble_sort,
    heap_sort,
    quick_sort,
    selection_sort,
    insertion_sort,
    shell_sort,
    benchmark_function
)


if __name__ == "__main__":
    array_sizes = [10, 100, 1000, 10000]
    methods_list = [
        "Cортировка обменом",
        "Сортировка выбором",
        "Сортировка вставками",
        "Сортировка Шелла",
        "Быстрая сортировка",
        "Пирамидальная сортировка",
    ]
    data = [[0 for _ in range(len(array_sizes))] for _ in range(len(methods_list))]

    print(f"Benchmark start...")
    for index in range(len(array_sizes)):
        array_size = array_sizes[index]
        array = generate_random_array(array_size)

        data[0][index] = benchmark_function(array, bubble_sort)
        data[1][index] = benchmark_function(array, selection_sort)
        data[2][index] = benchmark_function(array, insertion_sort)
        data[3][index] = benchmark_function(array, shell_sort)
        data[4][index] = benchmark_function(array, quick_sort)
        data[5][index] = benchmark_function(array, heap_sort)

    head_format = "{:>25}" + "{:>10}" * (len(array_sizes))
    print(head_format.format("Размер массива", *array_sizes))

    row_format = "{:>25}" + "{:>10.4f}" * (len(array_sizes))
    for item, row in zip(methods_list, data):
        print(row_format.format(item, *row))
