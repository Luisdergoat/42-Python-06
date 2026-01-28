"""
Docstring for validator
"""


def validate_ingredients(ingredients: str) -> str:

    if not ingredients:
        return "No ingredients provided. Validation failed."

    valid_ingredients = ["fire", "water", "earth", "air"]
    if ingredients.lower() in valid_ingredients:
        return f"Ingredient '{ingredients}' is valid."
    else:
        return f"Ingredient '{ingredients}' is invalid."
