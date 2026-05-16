from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    status = "INVALID"
    for item in allowed:
        if item in ingredients_lower:
            status = "VALID"
            break
    return f"{ingredients} - {status}"
