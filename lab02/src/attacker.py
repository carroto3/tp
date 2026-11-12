from abc import ABC, abstractmethod  # Инструменты для абстрактных классов


class Attacker(ABC):  # Интерфейс: объект умеет атаковать
    @abstractmethod
    def attack(self, unit):  # Цель атаки — другой юнит
        pass
