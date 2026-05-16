from ex1 import HealingCreatureFactory, TransformCreatureFactory
from typing import Any


def main() -> None:
    print("Testing Creature with healing capability")
    factory_heal = HealingCreatureFactory()
    factory_tran = TransformCreatureFactory()
    base_heal: Any = factory_heal.create_base()
    evolved_heal: Any = factory_heal.create_evolved()
    print(" base:")
    print(base_heal.describe())
    print(base_heal.attack())
    print(base_heal.heal())
    print(" evolved")
    print(evolved_heal.describe())
    print(evolved_heal.attack())
    print(evolved_heal.heal())
    print()
    print("Testing Creature with transform capability")
    base_tran: Any = factory_tran.create_base()
    evolved_tran: Any = factory_tran.create_evolved()
    print(" base:")
    print(base_tran.describe())
    print(base_tran.attack())
    print(base_tran.transform())
    print(base_tran.attack())
    print(base_tran.revert())
    print(" evolved")
    print(evolved_tran.describe())
    print(evolved_tran.attack())
    print(evolved_tran.transform())
    print(evolved_tran.attack())
    print(evolved_tran.revert())


if __name__ == "__main__":
    main()
