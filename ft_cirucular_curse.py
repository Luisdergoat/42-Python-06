"""
Docstring for ft_cirucular_curse
"""

import alchemy.grimoire.validator as valid
import alchemy.grimoire.spellbook as spell


def main():
    print("=== Circular Curse Breaking ===")
    print("\nTesting ingredient validation:")
    ingredients = "fire", "air"
    for ingredient in ingredients:
        result = valid.validate_ingredients(ingredient)
        print(f"Validating '{ingredient}': {result}")
    ingredient = "dragon scales"
    result = valid.validate_ingredients(ingredient)
    print(f"Validating '{ingredient}': {result}")
    print("\nTesting spell recording with validation:")

    spell1 = [
        ("Fireball", "fire"),
    ]
    for spell_name, ingredients in spell1:
        result = spell.record_spell(spell_name, ingredients)
        print(f"Recording spell '{spell_name}' "
              f"with ingredients '{ingredients}': {result}")

    spell2 = [
        ("Dark Magic", "shadow")
    ]
    for spell_name, ingredients in spell2:
        result = spell.record_spell(spell_name, ingredients)
        print(f"Recording spell '{spell_name}' "
              f"with ingredients '{ingredients}': {result}")
    print("\nTesting late import technique:")
    try:
        from alchemy.grimoire import record_spell as late_valid
        spell3 = ("Lightning", "air")
        for spell_name, ingredients in [spell3]:
            result = late_valid(spell_name, ingredients)
            print(f"Late import recording of spell '{spell_name}': {result}")
    except ImportError as e:
        print(f"Late import failed: {e}")


if __name__ == "__main__":
    main()
