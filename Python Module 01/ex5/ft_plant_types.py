#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age
        self.growth_rate = 2.1

    def grow(self, unit: int = 1) -> None:
        self.height = round(self.height + (self.growth_rate * unit), 1)

    def age(self, old: int = 1) -> None:
        self.age_days = self.age_days + old

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming is False:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self.is_blooming = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {float(self.trunk_diameter)}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{float(self.height)}cm long and "
              f"{float(self.trunk_diameter)}cm wide")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest = harvest_season
        self.value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest}")
        print(f" Nutritional value: {self.value}")

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.value += days

    def grow(self, days: int = 1) -> None:
        super().grow(days)
        print(f"[make {self.name.lower()} grow and age for {days} days]")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    tomato.age(20)
    tomato.grow(20)
    tomato.show()


if __name__ == "__main__":
    main()
