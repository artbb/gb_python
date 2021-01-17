"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road:
    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width
        self._tcRoad = 2.5
        self._hight = 0.05

    def road_mass(self):
        tc = self._length * self._width * self._tcRoad * self._hight
        print(f'Для покрытия дорожного полотна потребуется {tc} тн асфальта')

r = Road(int(input('Введите длину дороги, м: ')), int(input('Введите ширину дороги, м: ')))
r.road_mass()
