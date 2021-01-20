"""
3)	Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). Нарезать звездочками!!.
"""


class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        pass

    def __add__(self, other):
        return f'Сумма: {self.cell + other.cell}'

    def __sub__(self, other):
        sub = self.cell - other.cell
        return f'Вычитание: {sub}' if sub > 0 else 'Клеток нет'

    def __truediv__(self, other):
        return f'Деление {self.cell // other.cell}'

    def __mul__(self, other):
        return f'Умножение: {self.cell * other.cell}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.cell / row)):
            result += '*' * row + '\n'
        result += '*' * (self.cell % row) + '\n'
        return result
try:
    cell_1 = Cell(int(input('Введите кол-во клеток 1: ')))
    cell_2 = Cell(int(input('Введите кол-во клеток 2: ')))
except ValueError:
    print('Введите целое число')

try:
    print(cell_1 + cell_2)
    print(cell_1 - cell_2)
    print(cell_1 / cell_2)
    print(cell_1 * cell_2)
    print(cell_1.make_order(int(input('Введите кол-во ячеек в ряд: '))))
except:
    print('')
