"""
Alchemy Package
"""

__version__ = "1.0.0"
__author__ = "Alchemy Dev Team"


from .elements import create_fire, create_water
from .potions import healing_potion, strength_potion

__all__ = ["create_fire", "create_water", "healing_potion", "strength_potion"]
# Note: create_earth and create_air are intentionally not imported here
