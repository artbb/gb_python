"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
"""
class Car:
    plc = int(input('Выберите класс: 1-TownCar, 2-SportCar, 3-WorkCar, 4-PoliceCar: '))
    name = int(input('Выберите марку: 1-Audi, 2-BMW, 3-VW, 4-Lada: '))
    color = int(input('Выберите цвет: 1-красный, 2-желтый, 3-черный, 4-белый: '))
    drt = int(input('Выберите направление движения: 1-вперед, 2-назад, 3-влево, 4-вправо, 5-стоп: '))
    speed = int(input('Задайте вашу скорость, км/ч: '))
    plc1 = {1: 'TownCar', 2: 'SportCar', 3: 'WorkCar', 4: 'PoliceCar'}
    nm1 = {1: 'Audi', 2: 'BMW', 3: 'VW', 4: 'Lada'}
    clr1 = {1: 'красный', 2: 'желтый', 3: 'черный', 4: 'белый'}
    drt1 = {1: 'вперед', 2: 'назад', 3: 'влево', 4: 'вправо', 5: 'стоп'}

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return Car.drt1.get(Car.drt)

    def show_speed(self):
        return Car.speed


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости! Не более 40 км/ч'
        else:
            return f'Скорость допустимая'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости! Не более 60 км/ч'
        else:
            return f'Скорость допустимая'

class SportCar(Car):
    def nm_car(self):
        if Car.name == 3 or Car.name == 4:
            return f'Ошибка! {Car.nm1.get(Car.name)} не спортивная машина!'
        else:
            return f'{Car.nm1.get(Car.name)} - спортивная машина'

class PoliceCar(Car):
    def show_police(self):
        if self.plc == 4:
            return f'Вы из полиции!'
        else:
            return f'Вы не из полиции'


if Car.plc == 1:
    car = Car(Car.plc1.get(Car.plc), Car.speed, Car.clr1.get(Car.color), False)
    town = TownCar(Car.plc1.get(Car.plc), Car.speed, Car.clr1.get(Car.color), False)
    print(
        f'\nВаша машина: ({Car.plc1.get(Car.plc)}, {Car.nm1.get(Car.name)}, {Car.clr1.get(Car.color)}).\nСкорость {car.show_speed()} км/ч. {town.show_speed()}.\nДвижение {car.go()}')

if Car.plc == 2:
    car = Car(Car.plc1.get(Car.plc), Car.speed, Car.clr1.get(Car.color), False)
    sport = SportCar(Car.plc1.get(Car.plc), Car.speed, Car.clr1.get(Car.color), False)
    print(
        f'\nВаша машина: ({Car.plc1.get(Car.plc)}, {Car.nm1.get(Car.name)}, {Car.clr1.get(Car.color)}, {sport.nm_car()}).\nСкорость {car.show_speed()} км/ч.\nДвижение {car.go()}')

if Car.plc == 3:
    car = Car(Car.plc1.get(Car.plc), Car.speed, Car.clr1.get(Car.color), False)
    work = WorkCar(Car.plc1.get(Car.plc), Car.speed, Car.clr1.get(Car.color), False)
    print(
        f'\nВаша машина: ({Car.plc1.get(Car.plc)}, {Car.nm1.get(Car.name)}, {Car.clr1.get(Car.color)}).\nСкорость {car.show_speed()} км/ч. {work.show_speed()}.\nДвижение {car.go()}')

if Car.plc == 4:
    car = Car(Car.plc1.get(Car.plc), Car.speed, Car.clr1.get(Car.color), True)
    police = PoliceCar(Car.plc1.get(Car.plc), Car.speed, Car.clr1.get(Car.color), True)
    print(
        f'\nВаша машина: ({Car.plc1.get(Car.plc)}, {Car.nm1.get(Car.name)}, {Car.clr1.get(Car.color)}. {police.show_police()}).\nСкорость {car.show_speed()} км/ч.\nДвижение {car.go()}')
