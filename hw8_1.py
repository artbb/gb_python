"""
1.	Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
@classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
try:
    class Data:
        def __init__(self, data):
            self.data = data

        @classmethod
        def class_data(cls, data):
            day = int(data.split('-')[0])
            month = int(data.split('-')[1])
            year = int(data.split('-')[2])
            return f'день - {day}, месяц - {month}, год - {year}'

        @staticmethod
        def stat_data(data):
            day = int(data.split('-')[0])
            month = int(data.split('-')[1])
            year = int(data.split('-')[2])
            if day > 31:
                print('Ошибка! Выберите день от 1 до 31')
            if month > 12:
                print('Ошибка! Выберите месяц от 1 до 12')
            if year > 2100:
                print('Ошибка! Выберите год от 1 до 2100')
            if day < 31 and month < 31 and year < 2100:
                return f'Дата {data} введена корректно'


    d1 = input('Введите дату в формате ДД-ММ-ГГГГ: ')

    print(Data.class_data(d1))
    print(Data.stat_data(d1))

except Exception:
    print('Ошибка! Введите дату в формате ДД-ММ-ГГГГ')
