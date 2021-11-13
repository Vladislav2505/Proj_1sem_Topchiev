# Вариант 28.
# Дано целое число в диапазоне 1-7. Вывести строку — название дня недели, соответствующее данному числу.

k = input("Введите число в диапазоне 1-7: ")  # Ввод данных.

while type(k) != int:  # Проверка исключений.
    try:
        k = int(k)
    except ValueError:
        print("Неправильно ввели!")
        k = input("Введите число: ")

if k == 1:
    print('Понедельник')  # Вывод конечных данных.
elif k == 2:
    print('Вторник')  # Вывод конечных данных.
elif k == 3:
    print('Среда')  # Вывод конечных данных.
elif k == 4:
    print('Четверг')  # Вывод конечных данных.
elif k == 5:
    print('Пятница')  # Вывод конечных данных.
elif k == 6:
    print('Суббота')  # Вывод конечных данных.
elif k == 7:
    print('Воскресенье')  # Вывод конечных данных.
else:
    print('Нет такого дня недели.')
