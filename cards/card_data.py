from dataclasses import dataclass


@dataclass
class Card:
    expansion: str
    expansion_shortcut: str
    name: str
    language: str
    rarity: str
    collector_number: int
    price_cents: int
    condition: str
    foil: bool
