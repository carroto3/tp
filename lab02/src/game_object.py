class GameObject:  # Базовый класс для всех игровых объектов
    next_id = 1  # Счётчик для выдачи уникальных идентификаторов

    def __init__(self, name, x, y):  # Сохраняем имя и начальные координаты
        self.__id = GameObject.next_id  # Присваиваем объекту номер
        GameObject.next_id += 1  # Подготавливаем номер для следующего объекта
        self.__name = name  # Запоминаем имя объекта
        self.__x = x  # Запоминаем координату X
        self.__y = y  # Запоминаем координату Y

    def getId(self):  # Возвращает идентификатор объекта
        return self.__id

    def getName(self):  # Возвращает имя объекта
        return self.__name

    def getX(self):  # Возвращает координату X
        return self.__x

    def getY(self):  # Возвращает координату Y
        return self.__y

    def setPosition(self, x, y):  # Меняет положение объекта
        self.__x = x
        self.__y = y
