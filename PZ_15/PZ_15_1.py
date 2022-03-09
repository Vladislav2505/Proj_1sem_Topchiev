# Вариант №28
# В матрице элементы последней строки заменить на 0.

from random import randint

matrix = [[randint(0, 5) for i in range(3)] for j in range(3)]  # создание матрицы

print("Исходная матрица: ", matrix)
for i in range(len(matrix)):
    matrix[2][i] = 0  # Замена на 0

print("Результат: ", matrix)  # Вывод
