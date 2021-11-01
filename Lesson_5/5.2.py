# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import defaultdict

# Очень не очень реализация данной задачи, ниже будет попытка переделать этот код с функциями.
# Создаём словарь добавляем символы шестнадцатиричной системы. Создаём ключи в словаре.
dict_num = defaultdict(int)
symbols = '0123456789ABCDEF'
counter = 0
for i in symbols:
    dict_num[i] += counter
    counter += 1
# Создаём переменные для выполнения задания, можно переделать на input что бы вводить другие.
num_first = list('A2')[:: -1]
num_second = list('C4F')[:: -1]

first = 0
second = 0
# Переводим в число.
for i in range(len(num_first)):
    first += dict_num[num_first[i]] * 16 ** i
print(first)

for i in range(len(num_second)):
    second += dict_num[num_second[i]] * 16 ** i
print(second)

# Делаем две переменных сложения и умножения полученых чисел.
result_a = first + second
result_b = first * second

# Создаём два пустых списка что бы внести в них ответ, поиском нужного значения в словаре. Можно кстати res_a и res_b,
# реализовать через очередь наверное, пробовал, работает, но смысла зачем так делать не понял.
res_a = []
res_b = []
while result_a > 0:
    x = result_a % 16
    for i in dict_num:
        if dict_num[i] == x:
            res_a.append(i)
    result_a //= 16

while result_b > 0:
    x = result_b % 16
    for i in dict_num:
        if dict_num[i] == x:
            res_b.append(i)
    result_b //= 16


print(f'Сумма = {res_a[:: -1]}')
print(f'Произведение = {res_b[:: -1]}')

# Попытка переделать данный код в функцию.


def transformation(number_fi):
    result_fi = 0
    number_fi = list(number_fi[:: -1])
    for fi in range(len(number_fi)):
        result_fi += dict_num_fx[number_fi[fi]] * 16 ** fi
    return result_fi


def calculation(number_fx):
    result_fx = []
    while number_fx > 0:
        x_x = number_fx % 16
        for fx in dict_num_fx:
            if dict_num_fx[fx] == x_x:
                result_fx.append(fx)
        number_fx = number_fx // 16
    result_fx = result_fx[:: -1]
    return result_fx


dict_num_fx = defaultdict(int)
symbols_fx = '0123456789ABCDEF'
counter_fx = 0
for i in symbols_fx:
    dict_num_fx[i] += counter_fx
    counter_fx += 1

number_first = transformation('A2')
number_second = transformation('C4F')
sum_num = number_first + number_second
multiplication = number_first * number_second
print(calculation(sum_num))
print(calculation(multiplication))

# Это самое тяжёлое задание пока что которое было) очень тяжело далось почему то.
