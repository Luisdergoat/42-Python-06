## This project has been created as part of the 42 curriculum by lunsold
---

## Dieses Repository enthält die Lösungen für das Python Modul 06 der 42 Schule.

![42 Badge](https://img.shields.io/badge/42-Project-blue)
![Language](https://img.shields.io/badge/Language-python-orange)

# 42-Python-06

Python-Modul mit Fokus auf **Import-Mechanismen** und **Package-Strukturierung** mit `__init__.py`-Dateien.

## Konzepte

### `__init__.py` - Package Control
Die `__init__.py`-Datei verwandelt einen Ordner in ein Python-Package und kontrolliert, was nach außen sichtbar ist:

```python
# alchemy/__init__.py
from .elements import create_fire, create_water
from .potions import healing_potion, strength_potion

__all__ = ["create_fire", "create_water", "healing_potion", "strength_potion"]
# create_earth und create_air sind NICHT exportiert!
```

**Effekt**: `alchemy.create_fire()` funktioniert, aber `alchemy.create_earth()` wirft einen `AttributeError`, obwohl die Funktion in `elements.py` existiert.

### Import-Techniken

**1. Verschiedene Import-Stile** (`ft_import_transmutation.py`)
```python
import alchemy.elements                      # Voller Pfad nötig
from alchemy.elements import create_fire     # Direkte Verwendung
from alchemy.potions import healing_potion as heal  # Mit Alias
from alchemy import create_water             # Via __init__.py
```

**2. Absolute vs. Relative Imports** (`ft_pathway_debate.py`)
```python
# In basic.py (absoluter Import)
from alchemy.elements import create_earth

# In advanced.py (relative Imports)
from .basic import lead_to_gold        # Gleiches Package
from ..potions import healing_potion   # Parent Package
```

**3. Circular Import Prevention** (`ft_circular_curse.py`)
```python
# Late Import - Import erst zur Laufzeit, nicht beim Modulstart
def main():
    from alchemy.grimoire import record_spell  # Vermeidet Zirkel
```

**4. Package Metadata** (`ft_sacred_scroll.py`)
```python
print(alchemy.__version__)  # Definiert in __init__.py
print(alchemy.__author__)
```

## Struktur
```
alchemy/
├── __init__.py          # Exportiert create_fire, create_water, potions
├── elements.py          # Basis-Elemente
├── potions.py           # Verwendet relative Imports
├── grimoire/
│   ├── __init__.py      # Exportiert record_spell, validate_ingredients
│   ├── spellbook.py     # Verwendet relative Imports
│   └── validator.py
└── transmutation/
    ├── __init__.py      # Exportiert alle Transmutationen
    ├── basic.py         # Absolute Imports
    └── advanced.py      # Relative Imports (.basic, ..potions)
```

## Verwendung
```bash
python3 ft_import_trransmutation.py  # Import-Stile
python3 ft_pathway_debate.py         # Absolute vs. Relative
python3 ft_cirucular_curse.py        # Circular Import Lösung
python3 ft_sacred_scroll.py          # __init__.py Kontrolle
```