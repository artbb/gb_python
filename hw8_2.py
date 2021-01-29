"""
2.	Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его
работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class OwnError(ZeroDivisionError):
    def __init__(self, split):
        self.split = split

try:
    del1 = int(input("Введите делимое: "))
    del2 = int(input("Введите делитель: "))
    if del2 == 0:
        raise OwnError("На 0 делить нельзя!")
    else:
        split = del1 / del2
        print(f"Результат деления: {round(split, 2)}")
except ValueError:
    print('Ошибка! Введите число')
except OwnError as err:
    print(err)
