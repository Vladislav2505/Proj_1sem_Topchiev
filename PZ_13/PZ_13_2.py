# Вариант №28
# Составить генератор (yield), который переведет символы строки из верхнего регистра в нижний.

# Функция, переведет символы строки из верхнего регистра в нижний.
def func_generator(ls):
    for i in ls:
        if type(i) == str:
            i = i.lower()
        yield i


lst = ["CAT", "DOG", "SNAKE"]  # входные данные
q = []  # список, в который будет записан результат
generator = func_generator(lst)  # создаем генератор

# Добавляем элементы, которые возвращает yield, в список output
for j in generator:
    q.append(j)

print("Результат: ", q)  # вывод результата