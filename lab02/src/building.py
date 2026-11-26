from game_object import GameObject


class Building(GameObject):
    def __init__(self, id, name, x, y, built):
        super().__init__(id, name, x, y)
        self.__built = built

    def isBuilt(self):
        return self.__built
