"""
Docstring for alchemy.grimoire package
"""

__version__ = "1.0.0"
__author__ = "Alchemy Dev Team"

from .spellbook import record_spell
from .validator import validate_ingredients

__all__ = ["record_spell", "validate_ingredients"]
