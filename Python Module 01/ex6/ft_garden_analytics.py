class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_count} grow, {self.age_count} "
                  f"age, {self.show_count} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age
        self.growth_rate = 2
        self.stats = self._Stats()

    def grow(self, unit: int = 1) -> None:
        self.stats.grow_count += 1
        self.height = round(self.height + (self.growth_rate * unit), 1)

    def age(self, old: int = 1) -> None:
        self.stats.age_count += 1
        self.age_days = self.age_days + old

    def show(self) -> None:
        self.stats.show_count += 1
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    @staticmethod
    def is_old(days: int) -> bool:
        if days < 365:
            older = False
        else:
            older = True
        print(f"Is {days} days more than a year? -> {older}")
        return older

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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
        self.is_blooming = True
        self.show()


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade = 0

        def display(self) -> None:
            super().display()
            print(f"{self.shade} shade")

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.diameter = trunk_diameter
        self.stats: Tree._TreeStats = self._TreeStats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {float(self.diameter)}cm")

    def produce_shade(self) -> None:
        self.stats.shade += 1
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{float(self.height)}cm long and {float(self.diameter)}cm wide")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def show(self) -> None:
        super().show()
        if self.is_blooming:
            print(f" Seeds: {self.seeds}")
        else:
            print(" Seeds: 0")


def display(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.is_old(30)
    Plant.is_old(400)
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(4)
    rose.bloom()
    display(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display(oak)
    oak.produce_shade()
    display(oak)
    print()
    print("=== Seed")
    sun = Seed("Sunflower", 80.0, 45, "yellow", 42)
    sun.show()
    print("[make sunflower grow, age and bloom]")
    sun.grow(15)
    sun.age(20)
    sun.bloom()
    display(sun)
    print()
    print("===Anonymous")
    anony = Plant.anonymous()
    anony.show()
    display(anony)


if __name__ == "__main__":
    main()
