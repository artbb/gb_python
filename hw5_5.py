"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

f_text = open("hw5_5.file", 'w', encoding='utf-8')
f_text.write(input('Введите числа через пробел: '))
f_text.close()

try:
    with open('hw5_5.file', 'r', encoding='utf-8') as file5_5:
        for line in file5_5:
            summ_n = 0
            for n in line.split():
                n = int(n)
                summ_n += n
            print(f'Сумма числе в файле {f_text.name} равна {summ_n}.')
except ValueError:
    print('Ошибка! Введите числа через пробел')