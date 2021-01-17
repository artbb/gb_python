"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы
должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра. TITLE не просто так
"""


class Stationery:
    title = input('Введите название проекта: ')

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Проект {Stationery.title}. Ручкой'


class Pencil(Stationery):
    def draw(self):
        return f'Проект {Stationery.title}. Карандашом'


class Handle(Stationery):
    def draw(self):
        return f'Проект {Stationery.title}. Маркером'


st = Stationery()
print(st.draw())
pen = Pen()
print(pen.draw())
pencil = Pencil()
print(pencil.draw())
handle = Handle()
print(handle.draw())
