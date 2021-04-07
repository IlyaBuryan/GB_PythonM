"""
3.	Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""

import random


def generator(start, end):
    number = 0
    while number == 0:
        number = random.randint(start, end)
    return number


my_list = [generator(-1, 10) for _ in range(10)]

print('Лист: ', my_list)


def fill_dict(n_elem):
    my_dict = {}
    for i in range(1, n_elem + 1):
        number = generator(-1, 10)
        my_dict[f'{number}_{i}'] = number
    return my_dict


my_dict = fill_dict(10)

print('Словарь: ', my_dict)
