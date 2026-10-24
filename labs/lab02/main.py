from game_objects import Archer, Fort, MobileHome


def main() -> None:
    archer = Archer("Archer", 0, 0)
    target = Archer("Target", 5, 5)
    fort = Fort("Fort", 10, 10)
    home = MobileHome("MobileHome", 3, 3)

    fort.build()
    archer.move(1, 2)
    home.move(2, 1)
    fort.attack(target)
    archer.attack(target)

    print(f"{archer.get_name()} id={archer.get_id()} pos=({archer.get_x()}, {archer.get_y()}) hp={archer.get_hp()} alive={archer.is_alive()}")
    print(f"{target.get_name()} id={target.get_id()} pos=({target.get_x()}, {target.get_y()}) hp={target.get_hp()} alive={target.is_alive()}")
    print(f"{fort.get_name()} id={fort.get_id()} pos=({fort.get_x()}, {fort.get_y()}) built={fort.is_built()}")
    print(f"{home.get_name()} id={home.get_id()} pos=({home.get_x()}, {home.get_y()}) built={home.is_built()}")


if __name__ == "__main__":
    main()
