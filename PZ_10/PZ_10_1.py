# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов. Среднее арифметическое элементов первого и второго файлов.
# Количество нечетных элементов первого и второго файлов. Элементы общие для двух файлов.
# Количество элементов, общих для двух файлов:

from random import randint

# Генерация первого текстового файла с исходныи данными
with open('text1_PZ_10_1.txt', 'w') as inp:
    seq = " ".join([str(randint(0, 10)) for i in range(10)])
    seq = seq.replace('0', '1')
    inp.writelines(seq)

# Генерация второго текстового файла с исходныи данными
with open('text1_PZ_10_1(2).txt', 'w') as inp:
    seq = " ".join([str(randint(-10, -1)) for q in range(10)])
    seq = seq.replace('0', '1')
    inp.writelines(seq)

# Генерация третьего текстового файла с исходныи данными
with open('text1_PZ_10_1(3).txt', 'w', encoding='utf-8') as r:
    with open('text1_PZ_10_1.txt', 'r', encoding='utf-8') as p:
        a = p.read()
        n = a.split()
        v2_1 = sum([int(i) for i in n]) / len(n)  # Среднее арифметическое элементов первого файла
    with open('text1_PZ_10_1(2).txt', 'r', encoding='utf-8') as o:
        b = o.read()
        j = b.split()
        v2_2 = sum([int(i) for i in j]) / len(j)  # Среднее арифметическое элементов первого файла
    # Вывод данных
    r.write(f'1-й файл: {a}\n')
    r.write(f'2-й  файл: {b}\n')
    r.write(f'Среднее арифметическое элементов первого файла: {str(v2_1)}\n')
    r.write(f'Среднее арифметическое элементов второго файла:{str(v2_2)}\n')
    re = 0
    rt = 0
    # Подсчет количества нечетных элементов
    for i in [int(i) for i in n]:
        if i % 2:
            re += 1
    k = b.replace('-', '').split()
    for i in [int(i) for i in j]:
        if i % 2:
            rt += 1
    r.write(f'Количество нечетных элементов первого и второго файлов: {int(re + rt)}\n')
    a = {int(i) for i in n}
    b = {int(i) for i in k}
    rty = a & b  # Нахождение количества элементов, общих для двух файлов
    # Вывод данных
    r.write(f'Элементы общие для двух файлов: {rty}\n')
    r.write(f'Количество элементов, общих для двух файлов: {len(rty)}\n')