# Вариант №28.
# Дано целое число N (> 0). Найти сумму N ** 2 + (N + 1) ** 2 + (N + 2) ** 2 + ... + (2N) ** 2

N = input('Введите целое положительное число > 0: ')

while type(N) != int:  # Проверка исключений.
    try:
        N = int(N)
        if N <= 0:
            print(f'Некорректный ввод - {N}!')
            N = input('Введите целое положительное число: ')
    except ValueError:
        print(f'Некорректный ввод - {N}!')
        N = input('Введите целое положительное число: ')

result = 0
i = N

while i <= 2 * N:
    result += i ** 2
    i += 1
print(result)  # Вывод данных.
