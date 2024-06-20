import random


def generate_random_array(size):
    return [random.randint(-10000, 10000) for _ in range(size)]


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
