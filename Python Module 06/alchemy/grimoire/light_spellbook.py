def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    ans = validate_ingredients(ingredients)
    if "VALID" in ans:
        return f"Spell recorded: {spell_name} ({ans})"
    else:
        return f"Spell rejected: {spell_name} ({ans})"
