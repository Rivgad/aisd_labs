import math
import random
from timeit import default_timer as timer


def generate_random_array(size):
    return [random.randint(-10000, 10000) for _ in range(size)]


def benchmark_function(array: list, function):
    arr_copy = array.copy()
    start = timer()
    function(arr_copy)
    end = timer()
    return round(end - start, 4)


def bubble_sort(array):
    n = len(array) - 1

    for i in range(n,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


def selection_sort(array):
    n = len(array) - 1

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


def shell_sort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array


def quick_sort(array: list):
    n = len(array)
    if n > 1:
        pivot=array[n//2]
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quick_sort(smlr_lst) + equal_lst + quick_sort(grtr_lst))
    else:
        return array


def heap_sort(array):
    def heapify(array, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and array[i] < array[l]:
            largest = l
        if r < n and array[largest] < array[r]:
            largest = r
        
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify(array, n, largest)

    n = len(array)
    for i in range(n//2, -1, -1):
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array
