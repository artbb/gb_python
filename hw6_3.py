"""
вопрос: в конструкторе прописал/инициировал все параметры отдельно, на лекции сказали,
что можно одним массивом инициировать self.mylist = [name, surname, position]
однако при реализации программа этих параметров не видит. как сделать так, чтобы
читалось из массива
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Полное имя: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Оклад и бонус: {self._income["wage"] + self._income["bonus"]}'


p = Position(input('Введите имя: '), input('Введите фамилию: '), input('Введите должность: '), int(input('Введите оклад: ')), int(input('Введите бонус: ')))
print(p.get_full_name())
print(p.get_total_income())
