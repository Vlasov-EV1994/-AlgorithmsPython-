# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# Опять строкой запрашиваем, создаём список через split и пустой список для внесения в него суммы чисел.
numbers = input('Введите числа через пробел: ')
list_numbers = numbers.split()
result = []
# Идём по списку переводим каждый элемент в int и сразу добавляем сумму в список result.
for i in list_numbers:
    res = [int(j) for j in i]
    result.append(sum(res))
# Узнаём индекс положения числа в списке result
maximum_idx = (result.index(max(result)))
# Подставляем и готово
print(f'Максимальное число по сумме цифр: {list_numbers[maximum_idx]}, сумма его цифр равна: {max(result)}')
