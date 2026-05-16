from ..potions import strength_potion
import elements
from ..elements import create_air


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' and "
            f"'{strength_potion()}' mixed with '{elements.create_fire()}'")


if __name__ == "__main__":
    lead_to_gold()
