"""
7.	Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата
"""


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a != 0 and self.b >= 0:
            return f'{self.a}+{self.b}i'
        elif self.a != 0 and self.b < 0:
            return f'{self.a}{self.b}i'
        elif self.a == 0:
            return f'{self.b}i'

    def __add__(self, other):
        if (self.a + other.a) != 0 and (self.b + other.b) >= 0:
            return f'Сумма: {self.a + other.a}+{self.b + other.b}i'
        elif (self.a + other.a) != 0 and (self.b + other.b) < 0:
            return f'Сумма: {self.a + other.a}{self.b + other.b}i'
        elif (self.a + other.a) == 0:
            return f'Сумма: {self.b + other.b}i'

    def __mul__(self, other):
        if (self.a * other.a - self.b * other.b) != 0 and (self.a * other.b + self.b * other.a) >= 0:
            return f'Умножение: {self.a * other.a - self.b * other.b}+{self.a * other.b + self.b * other.a}i'
        elif (self.a * other.a - self.b * other.b) != 0 and (self.a * other.b + self.b * other.a) < 0:
            return f'Умножение: {self.a * other.a - self.b * other.b}{self.a * other.b + self.b * other.a}i'
        elif (self.a * other.a - self.b * other.b) == 0:
            return f'Умножение: {self.a * other.b + self.b * other.a}i'


c_1 = Complex(4, -4)
c_2 = Complex(7, 5)

print('Комплексное число 1:', c_1)
print('Комплексное число 2:', c_2)
print(c_1 + c_2)
print(c_1 * c_2)
