"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""
import re

with open('hw5_2.file', 'r', encoding='utf-8') as file5_2:
    raw = 0
    for line in file5_2:
        raw += 1
        l_d = len(re.findall("(\d+)", str(line.split()))) #исключаем из расчета кол-ва слов цифры
        w = 0
        for i in line.split():
            if len(i) == 1 and i.isdigit() == False:
                w += 1 #исключаем из расчета кол-во слов слова (или занки) с 1 символом
        print(f'В строке {raw} кол-во слов: {len(line.split()) - l_d - w}')
    print(f'\nВсего строк в файле: {raw}')
