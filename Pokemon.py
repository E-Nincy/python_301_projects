# Requirements
# Your class should follow these specifications:

# Each Pokemon should have a name, primary_type, max_hp, and hp.
# Primary types should be limited to water, fire, and grass.
# Implement a battle() method based on rock-paper-scissors that decides 
# who wins based only on the primary_type:
# water > fire > grass > water
# Display messages that explain who won or lost a battle.
# If a Pokemon loses a battle, they lose some of their hp.
# If you call the feed() method on a Pokemon, they regain some hp.
# Then, write a second script file that imports your Pokemon() class and 
# write the code for a small battle simulator.

# Create a Pokemon

class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp
        
    def __str__(self):
        return f"{self.name}, ({self.primary_type}: {self.hp}/{self.max_hp})"
    
# Feed them
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} has now {self.hp} HP.")

        else:
            print(f"{self.name} is full.")

# Make them battle
    def battle(self, other):
        print(f"\n⚔️ {self.name} ({self.primary_type}) VS {other.name} ({other.primary_type})")
        
        result = self.typewheel(self.primary_type, other.primary_type)
        
        if result == "win":
            print(f"{self.name} wins!")
            other.hp -= 3
            if other.hp < 0:
                other.ho = 0
            print(f"{other.name} loses 3 HP! ({other.hp}/{other.max_hp} HP)")
        elif result == "lose":
            print(f"{self.name} loses!")
            self.hp -=3 
            if self.hp < 0:
                self.hp = 0
            print(f"{self.name} loses 3 HP! ({self.hp}/{self.max_hp} HP)")
        else: 
            print("It's a tie! No one loses HP!")
        # Cal typewheel()
    
    @staticmethod
    def typewheel(type1, type2):
        result = {0: "lose", 1: "win", -1: "tie"}
        # mapping between types and result conditions
        game_map = {"water": 0, "fire": 1, "grass": 2}

        # implement win-lose matrix
        wl_matrix = [
            [-1, 1, 0], # water
            [0, -1, 1], # fire
            [1, 0, -1], # grass
        ]

        # declare winner
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]


# Take a look at it 
if __name__ == '__main__':
    Squirtle = Pokemon("Squirtle", "water", 150)
    Charmeleon = Pokemon("Charmeleon", "fire, 100")

    print(Squirtle)
    print(Charmeleon)

    Squirtle.battle(Charmeleon)
    Charmeleon.battle(Squirtle)
    Squirtle.feed()