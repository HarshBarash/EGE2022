test_data = [1, 3, 1, 1, 7]

""""
Домашняя работа. Модуль 4
"""


def sum(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    else:
        first = array[0]
        array.pop(0)  # pop == уничтожить
        return first + sum(array)


print(sum(test_data))


def length(array):
    if len(array) == 0:
        return 0
    else:
        return 1 + length(array[1:])  # "все элементы, начиная с 1",


print(length(test_data))


def max(array):
    if len(array) == 0:
        return 0
    elif array[0] > max(array[1::]):
        return array[0]
    else:
        return max(array[1:])  # "все элементы, начиная с 1",


print(max(test_data))

