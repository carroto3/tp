from game_object import GameObject  # Базовый класс игровых объектов


class Building(GameObject):  # Постройка — объект с состоянием строительства
    def __init__(self, name, x, y, built):  # Имя, координаты и флаг постройки
        super().__init__(name, x, y)  # Инициализируем общую часть объекта
        self.__built = built  # Запоминаем, построено ли здание

    def isBuilt(self):  # Возвращает состояние строительства
        return self.__built
