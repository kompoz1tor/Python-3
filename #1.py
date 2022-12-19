"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
import random
from random import randint

list = []
for i in range(5):
    list.append(randint(0, 10))
print(f'Исходный список: {list}')

sum = 0
for i in range (len(list)):
    if i % 2 != 0:
        sum = sum + list[i]
print(f'Сумма чисел на нечетных индексах равна: {sum} ')