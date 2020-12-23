"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

file, l_hour, l_type = argv
text1 = print(
    f'Введите через пробел параметры для расчета заработной платы: \n1. кол-во рабочих часов (за месяц); \n2. тип сотрудника (1 - менеджмент, 2 - рабочий) \n')
try:
    l_hour = int(l_hour)
    l_type = int(l_type)
    if l_type == 1:
        zp = l_hour * 2000
        l_name = 'менеджмент'
    elif l_type == 2:
        zp = l_hour * 1000
        l_name = 'рабочий'
    else:
        print('Введите тип сотрудника 1 или 2')

    if l_hour > 200 and l_type == 1:
        bonus = (l_hour - 100) * 1000
    elif l_hour > 200 and l_type == 2:
        bonus = (l_hour - 100) * 500
    else:
        bonus = 0

    l_all = zp + bonus

    print(
        f'Сотрудник из {l_name.upper()} проработал {l_hour} ч/мес. Зарплата составила {zp} руб., бонус {bonus} руб. Всего выплата {l_all} руб.')
except:
    print(
        'Введите 2 параметра через пробел: кол-во отработанных часов в месяц и тип сотрудника 1 или 2. (Пример: .../python hw4_1.py 220 1)')
