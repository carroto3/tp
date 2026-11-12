from building import Building
from moveable import Moveable


class MobileHouse(Building, Moveable):
    def move(self, x, y):
        self._setPosition(x, y)
        return True
