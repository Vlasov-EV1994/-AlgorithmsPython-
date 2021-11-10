# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
import random
import timeit

# Обычная сортировка пузырьком, всё работает, интересно было посмотреть с временем выполнения и сравнить разные
# вариации выполнения сортировки, делал в том числе и замеры через функции с использованием cProfile.
a = [random.randint(-100, 100) for i in range(15)]
print(a)
start_time_a = timeit.default_timer()
for i in range(14):
    for x in range(14 - i):
        if a[x] > a[x + 1]:
            a[x], a[x + 1] = a[x + 1], a[x]
print(timeit.default_timer() - start_time_a)
print(a)

b = [random.randint(-100, 100) for i in range(15)]
print(b)
start_time_b = timeit.default_timer()
c = sorted(b)
print(timeit.default_timer() - start_time_b)
print(c)
