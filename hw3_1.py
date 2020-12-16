"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def calc_2(num1, num2):
    mult1 = num1 * num2
    summ1 = num1 + num2
    subtr1 = num1 - num2
    try:
        div1 = num1 / num2
        print(
            f"Деление: {round(div1, 2)} \nУмножение: {round(mult1, 2)} \nСумма: {round(summ1, 2)} \nРазница: {round(subtr1, 2)}")
    except ZeroDivisionError:
        print(
            f"Деление: второе число 0, делить нельзя \nУмножение: {round(mult1, 2)}, \nСумма: {round(summ1, 2)}, \nРазница: {round(subtr1, 2)}")

try:
    calc_2(float(input('Введите число 1: ')), float(input('Введите число 2: ')))
except ValueError:
    print('Введите число')
