"""
Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением дробной части элементов. 
(подробности в конце записи семинара).
Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

#random.uniform(<Начало>, <Конец>) — возвращает псевдослучайное вещественное число в диапазоне
import random
from random import uniform


number = int(input('Введите размер списка: '))
list = []
for i in range(number):
    real_number = uniform(0, 11)
    list.append(round(real_number, 2))

min = list[0]
max = 0

for i in range(len(list)):
    if max < list[i]:
        max = list[i]
    if min > list[i]:
        min = list[i]
difference = (max - int(max)) - (min - int(min))

print(f'исходный список: {list}')
print(f'максимальное значение: {max} , минимальное значение: {min}')
print(abs(round(difference,2)))