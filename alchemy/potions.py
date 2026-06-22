from .elements import create_earth, create_air
import elements

def strength_potion() -> str:
    return f"Strength potion brewed with '{elements.create_fire()}' and '{elements.create_water()}'"

def healing_potion() -> str:
    return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"