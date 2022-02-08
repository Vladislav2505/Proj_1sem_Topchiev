# Вариант №28
# Организовать и вывести последовательность из 20 целых чисел, выбрать не повторяющиеся элементы, найти их количество.
# Элементы больше 5 увеличить в два раза.

from random import randint

# Создаем список с рандомными целыми числами
numbers = [randint(1, 21) for i in range(randint(20, 20))]
length = len(numbers)
print(f'Старый список: {numbers}')

# Находиим уникальные элементы и их количество
list_of_unique_numbers = []
for i in numbers:
    if numbers.count(i) == 1:
        list_of_unique_numbers.append(i)
a = len(list_of_unique_numbers)

# Увеличиваем их в два раза (n > 5)
list_of_unique_numbers_new = [n * 5 for n in list_of_unique_numbers if n > 5]

# Выводим данные
print(f'Не повторяющиеся элементы: {list_of_unique_numbers}')
print(f'Их количество: {a}')
print(f'Элементы больше 5 увеличить в два раза: {list_of_unique_numbers_new}')
