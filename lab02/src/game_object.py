class GameObject:
    def __init__(self, id, name, x, y):
        self.__id = id
        self.__name = name
        self.__x = x
        self.__y = y

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def _setPosition(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("координаты должны быть числами")
        self.__x = x
        self.__y = y
