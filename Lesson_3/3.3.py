# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# Импортируем модуль для создания рандомного списка чисел.
from random import randint
numbers = []
for i in range(10):
    x = randint(1, 100)
    numbers.append(x)
# Проверям что бы список был.
print(numbers)

# Создаём две переменых в которые заносятся индексы минимального и максимального числа.
min_num_idx = numbers.index(min(numbers))
max_num_idx = numbers.index(max(numbers))

print(min_num_idx, max_num_idx)
# Меняем индексы местами. Работает даже если несколько одинаковых минимальных цифр или максимальных,
# но местами меряются первые в списке.
numbers[min_num_idx], numbers[max_num_idx] = numbers[max_num_idx], numbers[min_num_idx]
print(numbers)
