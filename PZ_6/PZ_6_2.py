# Вариант № 28
# Дан целочисленный список A размера N (< 15). Переписать в новый целочисленный
# список B все элементы с порядковыми номерами, кратными трем (3, 6, ...)
from random import randint
n = int(input('Введите n (n < 15): '))  # Ввод данных
a = [randint(1, 100) for i in range(n)]
print(a)
b = []
for i in range(0, len(a), 3):
    b.append(a[i])  # Добавление нового значения
print(f'Длина списка b: {len(b)}')  # Вывод длины
print(f'Список b: {b}')  # Вывод списка