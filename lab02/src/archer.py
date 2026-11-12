from unit import Unit
from attacker import Attacker
from moveable import Moveable


class Archer(Unit, Attacker, Moveable):
    def __init__(self, name, x, y, hp, damage):
        super().__init__(name, x, y, hp)
        self.__damage = damage

    def attack(self, unit):
        if not isinstance(unit, Unit):
            raise TypeError("атаковать можно только юнита")
        if not self.isAlive() or not unit.isAlive():
            return False
        unit.receiveDamage(self.__damage)
        return True

    def move(self, x, y):
        if not self.isAlive():
            return False
        self._setPosition(x, y)
        return True
