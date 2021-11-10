# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


# Пока читал про данный вид сортировки встречал шаблоны выполнения данной сортировки, разобрал именно этот вариант.

def merge_sort(list_number):
    if len(list_number) <= 1:
        return list_number

    left_side = merge_sort(list_number[:len(list_number) // 2])
    right_side = merge_sort(list_number[len(list_number) // 2:])

    i = 0
    x = 0
    result = []

    while i < len(left_side) or x < len(right_side):
        if i >= len(left_side):
            result.append(right_side[x])
            x += 1
        elif x >= len(right_side):
            result.append(left_side[i])
            i += 1
        elif left_side[i] < right_side[x]:
            result.append(left_side[i])
            i += 1
        else:
            result.append(right_side[x])
            x += 1
    return result


a = [round(random.uniform(0, 50), 3) for i in range(15)]
print(a)
print(merge_sort(a))
