from unit import Unit  # Класс юнита
from attacker import Attacker  # Возможность атаковать
from moveable import Moveable  # Возможность перемещаться


class Archer(Unit, Attacker, Moveable):  # Лучник — юнит с атакой и перемещением
    def __init__(self, name, x, y, hp, damage):  # Данные лучника и его урон
        super().__init__(name, x, y, hp)  # Общие данные передаём в Unit
        self.__damage = damage  # Запоминаем силу атаки

    def attack(self, unit):  # Атака цели, если лучник жив
        if self.isAlive():
            unit.receiveDamage(self.__damage)

    def move(self, x, y):  # Живой лучник может сменить позицию
        if self.isAlive():
            self.setPosition(x, y)
