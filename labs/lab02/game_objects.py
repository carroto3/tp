from abc import ABC, abstractmethod


class Attacker(ABC):
    @abstractmethod
    def attack(self, unit: "Unit") -> None:
        ...


class Moveable(ABC):
    @abstractmethod
    def move(self, dx: int, dy: int) -> None:
        ...


class GameObject:
    _next_id = 1

    def __init__(self, name: str, x: int, y: int) -> None:
        self._id = GameObject._next_id
        GameObject._next_id += 1
        self._name = name
        self._x = x
        self._y = y

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def _shift(self, dx: int, dy: int) -> None:
        self._x += dx
        self._y += dy


class Unit(GameObject):
    def __init__(self, name: str, x: int, y: int, hp: float) -> None:
        super().__init__(name, x, y)
        self._hp = float(hp)

    def is_alive(self) -> bool:
        return self._hp > 0

    def get_hp(self) -> float:
        return self._hp

    def receive_damage(self, damage: float) -> None:
        if damage < 0:
            raise ValueError("damage must be non-negative")
        self._hp = max(0.0, self._hp - float(damage))


class Building(GameObject):
    def __init__(self, name: str, x: int, y: int, built: bool = False) -> None:
        super().__init__(name, x, y)
        self._built = built

    def is_built(self) -> bool:
        return self._built

    def build(self) -> None:
        self._built = True


class Archer(Unit, Attacker, Moveable):
    def __init__(self, name: str, x: int, y: int, hp: float = 100.0, damage: float = 15.0) -> None:
        super().__init__(name, x, y, hp)
        self._damage = float(damage)

    def attack(self, unit: Unit) -> None:
        unit.receive_damage(self._damage)

    def move(self, dx: int, dy: int) -> None:
        self._shift(dx, dy)


class Fort(Building, Attacker):
    def __init__(self, name: str, x: int, y: int, damage: float = 25.0) -> None:
        super().__init__(name, x, y)
        self._damage = float(damage)

    def attack(self, unit: Unit) -> None:
        if not self.is_built():
            raise RuntimeError("fort is not built yet")
        unit.receive_damage(self._damage)


class MobileHome(Building, Moveable):
    def move(self, dx: int, dy: int) -> None:
        self._shift(dx, dy)
