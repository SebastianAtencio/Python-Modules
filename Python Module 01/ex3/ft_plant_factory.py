#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


def main() -> None:
    plant_factory = [
        ("Rose", 25.0, 30),
        ("Oak", 200.0, 365),
        ("Cactus", 5.0, 90),
        ("Sunflower", 80.0, 45),
        ("Fern", 15.0, 120)
    ]
    print("=== Plant Factory Output ===")
    for info in plant_factory:
        new_plant = Plant(info[0], info[1], info[2])
        print("Created: ", end="")
        new_plant.show()


if __name__ == "__main__":
    main()
