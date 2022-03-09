# Вариант №28
# В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.

from random import randint

matrix = [[randint(0, 5) for i in range(3)] for j in range(3)]  # создание матрицы

print("Исходная матрица: ", matrix)
n = int(input("Введите номер столбца n <= 3: "))
if n <= 3:
    for i in range(0, len(matrix)):
        matrix[i][n - 1] = matrix[i][n - 1] * 2  # Увеличиваем столбец в два раза
    print("Результат: ", matrix)  # Вывод
else:
    print('В матрице три столба!!!')
