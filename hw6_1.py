"""
1. Модификация: можно задавать время работы по каждому цвету и кол-во часов работы в сутки.
В зависимости от этого, светофор выключится (станет желтым) на оставшееся время
"""

from time import sleep
from termcolor import colored


class TrafficLight:
    __color = [colored('\u24C8 STOP', 'grey', 'on_red'), colored('\u24CC WAIT', 'grey', 'on_yellow'),
               colored('\u24BC GO  ', 'grey', 'on_green')]
    len_red = int(input('Введите продолжительность красного, сек: '))
    len_yellow = int(input('Введите продолжительность желтого, сек: '))
    len_green = int(input('Введите продолжительность зеленого, сек: '))
    len_work = float(input('Введите кол-во часов работы в сутки (десятичное число): '))

    def running(self):
        len_work_s = 3600 * TrafficLight.len_work  # кол-во сек работы
        len_work_all = round(len_work_s / (TrafficLight.len_red + TrafficLight.len_yellow + TrafficLight.len_green),
                             0)  # после этого кол-ва циклов светоров выключается (горит желтым), через 24 часа включается снова
        len_work_again = 3600 * 24 - len_work_s  # сколько должен гореть желтым (не работать)
        print(
            f'Светофор работает {TrafficLight.len_work} час. в сутки. Затем выключается (горит желтым) на {round(len_work_again / 3600, 2)} час.')
        i = [0, 1, 2]
        t = 0
        while t < len_work_all:
            for k in i:
                print(TrafficLight.__color[k])
                if k == 0:
                    sleep(TrafficLight.len_red)
                elif k == 1:
                    sleep(TrafficLight.len_yellow)
                elif k == 2:
                    sleep(TrafficLight.len_green)
            t += 1
        print(TrafficLight.__color[1])
        sleep(len_work_again)


t = TrafficLight()
while True:
    t.running()
