# Из предложенного текстового файла (text18-28.txt) вывести на экран его содержимое, количество символов в тексте.
# Сформировать новый файл, в который поместить текст предварительно вставив после строки N произвольную фразу.

# Ввод данных
t = str(input('Введите произвольную фразу: '))
n = int(input('Введите номер строки от 1 до 7: '))

# Генерация первого текстового файла
with open('text18-28.txt', 'r', encoding='utf-8') as a:
    p = a.read()
    print(p)  # Содержимое файла
    print('Количество символов в тексте: ', len(p))  # Количество символов в тексте

with open('text18-28.txt', 'r', encoding='utf-8') as a:
    with open('text1_PZ_10_2.txt', 'w', encoding='utf-8') as c:  # Генерация второго текстового файла
        p = a.read()
        c.write(p)

with open('text18-28.txt', 'r', encoding='utf-8') as a:
    with open('text1_PZ_10_2.txt', 'w', encoding='utf-8') as c:
        # Вставляем после строки N произвольную фразу.
        z = 0
        for line in a:
            if n == z:
                c.write(f'{t}\n')
            z += 1
            c.write(line)
        if n == 7:
            c.write(f'\n{t}')
