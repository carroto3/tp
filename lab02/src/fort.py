from building import Building  # Класс построек
from attacker import Attacker  # Возможность атаковать


class Fort(Building, Attacker):  # Крепость — постройка, которая умеет стрелять
    def __init__(self, name, x, y, built, damage):  # Данные крепости и урон
        super().__init__(name, x, y, built)  # Передаём общие данные в Building
        self.__damage = damage  # Запоминаем силу атаки

    def attack(self, unit):  # Стреляем только после постройки
        if self.isBuilt():
            unit.receiveDamage(self.__damage)
