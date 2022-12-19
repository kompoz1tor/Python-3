"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16]
[2, 3, 5, 6] => [12, 15]
"""

import random
from random import randint

lenght_list = int(input('Введите размер списка: '))
list = []
current_list = []

for i in range(lenght_list):
    list.append(randint(1, 11))

for i in range(len(list)):
    while i < len(list)/2 and lenght_list > len(list)/2:
        lenght_list = lenght_list - 1
        a = list[i] * list[lenght_list]
        current_list.append(a)
        i += 1

print(f'исходный массив: {list}')
print(f'произведение пар чисел списка: {current_list}')