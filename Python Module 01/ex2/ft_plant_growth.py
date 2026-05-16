#!/usr/bin/env python3

class Plant:
    def __init__(
        self, name: str, height: float, age: int, growth: float
    ) -> None:
        self.name = name
        self.height = height
        self.age_days = age
        self.growth_rate = growth

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.age_days = self.age_days + 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


def main() -> None:
    p1 = Plant("Rose", 25.0, 30, 0.8)
    print("=== Garden Plant Growth ===")
    growth = 8
    initial = p1.height
    for day in range(1, growth):
        print(f"=== Day {day} ===")
        p1.show()
        p1.grow()
        p1.age()
    final = round(p1.height - initial, 0)
    print(f"Growth this week: {int(final)}cm")


if __name__ == "__main__":
    main()
