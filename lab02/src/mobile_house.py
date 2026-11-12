from building import Building  # Класс построек
from moveable import Moveable  # Возможность перемещаться


class MobileHouse(Building, Moveable):  # Дом на колёсах — подвижная постройка
    def move(self, x, y):  # Дом может менять координаты
        self.setPosition(x, y)
