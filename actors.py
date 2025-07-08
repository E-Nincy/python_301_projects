import random

class Hero:
    """The brave hero you control."""
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, opponent):
        print(f"{self.name} attacks {opponent.name}!")

        hero_roll = random.randint(1, 12) * self.level
        opp_roll = opponent.attack(self)

        print(f"You rolled {hero_roll}...")
        print(f"{opponent.name} rolled {opp_roll}...")

        if hero_roll >= opp_roll:
            print(f"Victory! {self.name} has defeated {opponent.name}.\n")
            return True
        else:
            print(f"Defeat! {opponent.name} has overpowered {self.name}.\n")
            return False

class Opponent:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, hero):
        return random.randint(1,12) * self.level
    
    def __repr__(self):
        return f"{self.name} (level{self.level})"
    
class Weakopponent (Opponent):
    def  attack(self, hero):
        print(f"{self.name} stumbles a little...")
        return random.randint(1, 6) * self.level
    
class FinalBossOpponent(Opponent):
    def __init__(self, name, level, special_power):
        super().__init__(name, level)
        self.special_power = special_power

    def attack(self, hero):
        base = random.randint(6, 12) * self.level
        if random.randint() < 0.3: 
            print(f"{self.name} uses their special power: {self.special_power}")
            return base * 2
        return base