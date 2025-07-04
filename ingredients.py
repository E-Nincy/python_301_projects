# CLASSES AN OBJECT-ORIENTED PROGRAMMING
class Ingredient:
    """Models an ingredient including its name and amount"""
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"There are {self.amount} of {self.name}"
    
    def use(self, use_amount):
        """Reduces the amount of ingredient available"""
        self.amount -= use_amount

    def expire(self):
        """Expire the ingredient item."""
        print(f"Whoops, these {self.name} went bad....")
        self.name = "expired " + self.name

# I N H E R I T A N C E

# built a subclass called spice
class Spice(Ingredient):
    """Models a spice to flavor your food."""

# create a custom method grind()
    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

c = Ingredient('carrots', 3)
p = Spice('pepper', 20)

p.grind()  # OUTPUT: You have now 20 of ground pepper.
c.grind()  # OUTPUT: AttributeError: 'Ingredient' object has no attribute 'grind'


# override the expire() method

# customize the __init__() method