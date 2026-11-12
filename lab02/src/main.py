from archer import Archer
from fort import Fort
from mobile_house import MobileHouse


def main():
    archer = Archer("Лучник", 2, 3, 100, 20)
    enemy = Archer("Противник", 5, 5, 100, 10)
    fort = Fort("Крепость", 1, 1, True, 30)
    house = MobileHouse("Дом на колёсах", 4, 4, True)

    print("Игровые объекты:")
    print(archer.getName(), "ID:", archer.getId())
    print("Координаты:", archer.getX(), archer.getY())
    print("Здоровье:", archer.getHp())

    print("\nАтака через общий интерфейс:")
    for attacker in (archer, fort):
        print(type(attacker).__name__, "попал:", attacker.attack(enemy))
    print("Здоровье противника:", enemy.getHp())

    print("\nСмерть юнита:")
    while enemy.isAlive():
        fort.attack(enemy)
    print("Здоровье противника:", enemy.getHp(), "Жив:", enemy.isAlive())

    fallen = Archer("Павший", 0, 0, 0, 10)
    print("Атака мёртвого лучника:", fallen.attack(archer))
    print("Перемещение мёртвого лучника:", fallen.move(1, 1))

    print("\nНедостроенная крепость:")
    target = Archer("Цель", 9, 9, 100, 10)
    new_fort = Fort("Новая крепость", 6, 6, False, 25)
    print("Построена:", new_fort.isBuilt())
    print("Попадание:", new_fort.attack(target))
    new_fort.build()
    print("Построена:", new_fort.isBuilt())
    print("Попадание:", new_fort.attack(target))

    print("\nПеремещение:")
    print("Лучник:", archer.move(6, 7), archer.getX(), archer.getY())
    print("Дом на колёсах:", house.move(8, 9), house.getX(), house.getY())


if __name__ == "__main__":
    main()
