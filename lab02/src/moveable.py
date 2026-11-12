from abc import ABC, abstractmethod  # Инструменты для абстрактных классов


class Moveable(ABC):  # Интерфейс: объект умеет перемещаться
    @abstractmethod
    def move(self, x, y):  # Перемещение в новые координаты
        pass
