from game_object import GameObject


class Building(GameObject):
    def __init__(self, name, x, y, built):
        super().__init__(name, x, y)
        self.__built = built

    def isBuilt(self):
        return self.__built

    def build(self):
        self.__built = True
