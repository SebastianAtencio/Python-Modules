from alchemy import grimoire


def test() -> None:
    result = grimoire.light_spellbook.light_spell_record(
        'Fantasy', 'Earth, wind and fire'
    )
    print(f"Testing record light spell: {result}")


if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    test()
