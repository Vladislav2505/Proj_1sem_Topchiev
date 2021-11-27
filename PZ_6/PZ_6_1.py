# Вариант № 28
#  Дан список A размера N. Найти максимальный элемент из его элементов с нечетными
# номерами: A1, A3, A5, ... .

print(max([element for i, element in enumerate(map(int, input().split())) if i % 2 or i == 0]))
