import alchemy.transmutation.recipes


def test() -> None:
    print(f"{alchemy.transmutation.recipes.lead_to_gold()}")


if __name__ == "__main__":
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print("Testing lead to gold: ", end="")
    test()
