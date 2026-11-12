from game_object import GameObject  # Базовый класс игровых объектов


class Unit(GameObject):  # Юнит — игровой объект с запасом здоровья
    def __init__(self, name, x, y, hp):  # Принимаем имя, координаты и здоровье
        super().__init__(name, x, y)  # Инициализируем общую часть объекта
        self.__hp = hp  # Запоминаем текущее здоровье

    def isAlive(self):  # Юнит жив, пока здоровье положительно
        return self.__hp > 0

    def getHp(self):  # Возвращает текущее здоровье
        return self.__hp

    def receiveDamage(self, damage):  # Обрабатывает полученный урон
        self.__hp -= damage  # Отнимаем урон от здоровья

        if self.__hp < 0:  # Здоровье не может уйти в минус
            self.__hp = 0
