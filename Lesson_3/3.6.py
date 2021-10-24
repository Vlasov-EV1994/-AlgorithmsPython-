# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# Создаём список как и в прошлых задания.
# Тут был вариант убрать все не уникальные значения, и работало бы ещё лучше, это сделать легко в случае необходимости,
# а так он минимум и максимум берёт по первым встретившимся
from random import randint
numbers = []
for i in range(10):
    x = randint(0, 10)
    numbers.append(x)
print(numbers)

# Создаём переменные и ложим в них минимум максимум и индексы их.
min_num = min(numbers)
max_num = max(numbers)
print(min_num, max_num)
idx_min = numbers.index(min_num)
idx_max = numbers.index(max_num)

# Тут мы проверяем где находится элемент что бы сделать коректный срез по рассположению минимума и максимума в списке.
if idx_min > idx_max:
    sum_numbers = numbers[idx_max + 1: idx_min]
    print(sum_numbers)  # Числа между максимумом и минимумом
    print(sum(sum_numbers))
elif idx_max > idx_min:
    sum_numbers = numbers[idx_min + 1: idx_max]
    print(sum_numbers)  # Числа между максимумом и минимумом
    print(sum(sum_numbers))
