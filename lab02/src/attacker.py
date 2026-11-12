from abc import ABC, abstractmethod


class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass
