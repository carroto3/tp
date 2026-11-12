from unit import Unit
from building import Building
from attacker import Attacker


class Fort(Building, Attacker):
    def __init__(self, name, x, y, built, damage):
        super().__init__(name, x, y, built)
        self.__damage = damage

    def attack(self, unit):
        if not isinstance(unit, Unit):
            raise TypeError("атаковать можно только юнита")
        if not self.isBuilt() or not unit.isAlive():
            return False
        unit.receiveDamage(self.__damage)
        return True
