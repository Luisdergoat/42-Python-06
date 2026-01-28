"""
Docstring for spellbook
"""

from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:

    if not spell_name:
        return "Spell name cannot be empty."
    if not ingredients:
        return "Ingredients cannot be empty."

    checked_ingredients = validate_ingredients(ingredients)
    if "invalid" in checked_ingredients:
        return f"Spell rejected: '{spell_name}': {checked_ingredients}"

    return (
        f"Spell '{spell_name}' "
        f"recorded successfully with ingredients: {ingredients}")
