#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age_days = 0
        self.set_height(height)
        self.set_age(age)
        print(f"Plant created: {self.name}: {self._height}cm, "
              f"{self._age_days} days old")

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(value)

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = int(value)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days


def main() -> None:
    print("=== Garden Security System ===")
    p1 = Plant("Rose", 15.0, 10)
    print()
    p1.set_height(25)
    print(f"Height updated: {int(p1.get_height())}cm")
    p1.set_age(30)
    print(f"Age updated: {p1.get_age()} days")
    print()
    p1.set_height(-5)
    p1.set_age(-4)
    print()
    print(
            f"Current state: {p1.name}: {float(p1.get_height())}cm, "
            f"{p1.get_age()} days old"
        )


if __name__ == "__main__":
    main()
