"""
3.	Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие
только чисел. Проверить работу исключения на реальном примере. Запрашивать у пользователя данные
и заполнять список необходимо только числами. Класс-исключение должен контролировать типы данных
элементов списка.
"""


class NumberError(Exception):
    def __init__(self, number):
        self.number = number


def my_proga():
    data = []
    while True:
        number = input('Введите число (для выхода наберите q): ')
        if number != 'q':
            try:
                if number.isdigit() != True:
                    raise NumberError("Ошибка! Введите число!")
            except NumberError as err:
                print(err)
            else:
                number = int(number)
                data.append(number)
        elif number == 'q':
            print('Введенный массив чисел:', data)
            print('Вы вышли из программы')
            break


my_proga()
