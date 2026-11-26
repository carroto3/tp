from game_object import GameObject


class Unit(GameObject):
    def __init__(self, id, name, x, y, hp):
        super().__init__(id, name, x, y)
        self.__hp = max(0.0, hp)

    def isAlive(self):
        return self.__hp > 0

    def getHp(self):
        return self.__hp

    def receiveDamage(self, damage):
        if damage < 0:
            raise ValueError("урон не может быть отрицательным")
        self.__hp = max(0.0, self.__hp - damage)
