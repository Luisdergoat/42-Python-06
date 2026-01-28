"""
Docstring for ft_sacred_scroll
"""

import alchemy


def main():
    print("=== Sacred Scroll mastery ===")

    print("\nTesting direct module access:")
    print(f"alchemy.elements.create_fire(): "
          f"{alchemy.create_fire()}")
    print(f"alchemy.elements.create_water(): "
          f"{alchemy.create_water()}")
    print(f"alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): "
          f"{alchemy.elements.create_air()}")
    print()
    print("\nTesting package metadata access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
        print(f"alchemy.create_water(): {alchemy.create_water()}")
        print("alchemy.create_earth(): "
              f"{alchemy.create_earth()}")
        print("alchemy.create_air(): "
              f"{alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_earth(): not exposed")
        print("alchemy.create_air(): not exposed")
    print()
    print("Package metadata:")
    version = alchemy.__version__
    author = alchemy.__author__
    print(f"Version: {version}")
    print(f"Author: {author}")


if __name__ == "__main__":
    main()
