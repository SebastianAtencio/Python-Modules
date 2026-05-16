from ex0 import AquaFactory, FlameFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2 import BattleStrategy
from ex1.capabilities import HealCapability, TransformCapability
from typing import List, Tuple


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    combos = []
    for fact, strat in opponents:
        temp_c = fact.create_base()
        if isinstance(temp_c, HealCapability):
            creature_name = "Healing"
        elif isinstance(temp_c, TransformCapability):
            creature_name = "Transform"
        else:
            creature_name = temp_c.name
        strat_name = strat.__class__.__name__.replace("Strategy", "")
        combos.append(f"({creature_name}+{strat_name})")
    print(f"[ {', '.join(combos)} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i+1, len(opponents)):
            fact_a, strat_a = opponents[i]
            fact_b, strat_b = opponents[j]
            c1 = fact_a.create_base()
            c2 = fact_b.create_base()
            print()
            print("* Battle *")
            print(c1.describe())
            print(" vs. ")
            print(c2.describe())
            print(" now fight!")
            try:
                strat_a.act(c1)
                strat_b.act(c2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame_f = FlameFactory()
    aqua_f = AquaFactory()
    heal_f = HealingCreatureFactory()
    tran_f = TransformCreatureFactory()
    normal_s = NormalStrategy()
    defensive_s = DefensiveStrategy()
    aggressive_s = AggressiveStrategy()
    print("Tournament 0 (basic)")
    battle([(flame_f, normal_s), (heal_f, defensive_s)])
    print()
    print("Tournament 1 (error)")
    battle([(flame_f, aggressive_s), (heal_f, defensive_s)])
    print()
    print("Tournamet 2 (multiple)")
    opponents2 = [
        (aqua_f, normal_s),
        (heal_f, defensive_s),
        (tran_f, aggressive_s)
    ]
    battle(opponents2)
