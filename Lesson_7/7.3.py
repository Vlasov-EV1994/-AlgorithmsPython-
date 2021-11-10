# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random


# Не понял как можно сделать без сортировки, там же в любом случае будет хоть как то она использована,
# но я точно ошибаюсь) В итоге схитрил и сделал методом слияния как и прошлое задание,
# ну и вариант только если количество элементов не чётное.
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


m = 4
b = 2 * m + 1
numbers = [random.randint(0, 100) for i in range(b)]
print(numbers)

numbers_sort = merge_sort(numbers)
print(numbers_sort)
s = (len(numbers_sort) / 2) - 0.5
print(numbers_sort[round(s)])
