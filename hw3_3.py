"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func(num1, num2, num3):
    my_list = (num1, num2, num3)
    my_list_s = sorted(my_list)[::-1]
    print(f'Сортированный список: {my_list_s}')
    return my_list_s[0] + my_list_s[1]


try:
    print('Сумма двух наибольших равна: ', my_func(float(input('Введите число 1: ')), float(input('Введите число 2: ')),
                                                   float(input('Введите число 3: '))))
except ValueError:
    print('Введите числа')
