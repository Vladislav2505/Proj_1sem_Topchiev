# Вариант №28
# По данному P определить, через сколько месяцев размер вклада превысит 1100 руб.

p = input('Введите P: ')  # Процент.

while type(p) != float or p < 0 or p > 25:  # Проверка исключений.
    try:
        p = float(p)
        if p < 0 or p > 25:
            print("Неправильно ввели!")
            p = input("Введите число: ")
    except ValueError:
        print("Неправильно ввели!")
        p = input("Введите число: ")

s = 1000  # Начальный вклад в банке.
k = 0

while s <= 1100:
    s = s * (p / 100 + 1)
    k += 1
print("Количество месяцев: ", k, " ", "Итоговый размер вклада: ", s)
