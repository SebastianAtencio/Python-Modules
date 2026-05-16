from ex0 import Creature
from .exceptions import InvalidStrategyError
from abc import ABC, abstractmethod
from typing import Any


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        temp: Any = creature
        try:
            temp.transform
            return True
        except AttributeError:
            return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                f"aggressive strategy")
        temp: Any = creature
        print(temp.transform())
        print(temp.attack())
        print(temp.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        temp: Any = creature
        try:
            temp.heal
            return True
        except AttributeError:
            return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                f"defensive strategy")
        temp: Any = creature
        print(temp.attack())
        print(temp.heal())
