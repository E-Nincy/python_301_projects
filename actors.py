import random

class Hero:
    """The brave hero you control."""
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, opponent):
        print(f"{self.name} attacks {opponent.name}!")

        hero_roll = random.randint(1, 12) * self.level
        opp_roll = random.randint(1, 12) * opponent.level

        print(f"You roll a {hero_roll}...")
        print(f"{opponent.name} rolls a {opp_roll}...")

        if hero_roll >= opp_roll:
            print(f"Victory! {self.name} has defeated {opponent.name}.\n")
            return True
        else:
            print(f"Defeat! {opponent.name} has overpowered {self.name}.\n")
            return False

class Opponent:
    """The enemies you'll face in the game."""
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Opponent: {self.name} (Level {self.level})"
