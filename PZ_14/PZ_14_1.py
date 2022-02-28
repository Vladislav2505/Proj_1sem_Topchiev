# Вариант №28
# В исходном текстовом файле (dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и ДД/ММ/ГГГГ. Посчитать количество дат в
# каждом формате. Поместить в новый текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.

import re

with open("dates.txt", "r", encoding="utf-8") as file:  # открываем файл dates.txt на чтение
    text = file.read()  # считываем содержимое документа
    dote = re.findall(r'\d\d\.\d\d\.\d{4}', text)  # Создание шаблона ДД/ММ/ГГГГ
    slash = re.findall(r'\d\d/\d\d/\d{4}', text)  # Создание шаблона ДД.ММ.ГГГГ
    print(f"ДД.ММ.ГГГГ: {dote}\n Количество: {len(dote)}\n"
          f"ДД/ММ/ГГГГ: {slash}\n Количество: {len(slash)}")  # Вывод

with open('barbara.txt', 'w', encoding='utf-8') as barbara:  # Создание и запись нового файла
    for q in slash:
        barbara.writelines(f"{q}\n")