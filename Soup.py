# Python project: COOKING SOUP
# -----------------------------------------------
#For this project, you'll create a custom Soup()
# class that can take Ingredient() and Spice() objects and use them 
# to look up soup recipes on the Internet.

import webbrowser

# Ingedient() and Spice() class - I use it as a base
class Ingredient:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
class Spice(Ingredient):
    def grind(self):
        print(F"You grind the {self.name}.")


# Now I create the Soup class
class Soup:
    def __init__(self, *ingredients):
        self.ingredients = []
        for item in ingredients:
            if isinstance(item, Ingredient):
                self.ingredients.append(item)
            else: 
                raise ValueError(f"{item} is not a valid ingredient")
    
    def cook(self):
        if not self.ingredients:
            print("No ingredients added. Air soup?")
            return
        
        ingredient_names = [str(i) for i in self.ingredients]
        query = "+".join(ingredient_names) + "+soup+ecipe"
        url = f"https://www.google.com/search?q={query}"
        print(F"Searching for a recipe with: {', '.join(ingredient_names)}")
        webbrowser.open(url)

# -- Test the code --
if __name__ == "__main__":
    carrot = Ingredient("carrot")
    chicken = Ingredient("chicken")
    cumin = Spice("cumin")

    # Try to grind a spice
    cumin.grind()

    #Make a soup with them 
    soup_of_the_day = Soup(carrot, chicken, cumin)

    # Cook (search for recipe)
    soup_of_the_day.cook()