# Вариант № 28.
# Описать функцию AddLeftDigit(D, K), добавляющую к целому положительному числу K слева цифру D.

# Объявление функции.
def add_left_digit(d, k):
    global K
    K = str(d) + str(k)
    return K


# Ввод данных.
K = int(input("k: "))
D1 = int(input("Введите D1(в диапазоне от 1 до 9): "))
while D1 < 1 or D1 > 9:  # Проверка условия.
    print('Вы ввели неккоректное значение D1.')
    D1 = int(input("Введите D1(в диапазоне от 1 до 9): "))
print(add_left_digit(D1, K))
D2 = int(input("Введите D2(в диапазоне от 1 до 9): "))
while D2 < 1 or D2 > 9:  # Проверка условия.
    print('Вы ввели неккоректное значение D2.')
    D2 = int(input("Введите D2(в диапазоне от 1 до 9): "))
print(add_left_digit(D2, K))  # Вывод данных.
