import webbrowser
import requests
from urllib.parse import quote

class Ingredient:
    """Models a food ingredient with a name and amount"""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.name}, {self.amount}"
    
    def get_info(self):
        """Opens the Wikipedia page for this ingredient"""
        formatted_name = self.name.strip().replace(" ", "_").capitalize()
        url = f"https://en.wikipedia.org/wiki/{formatted_name}"
        
        # Check if the page exists
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Opening Wikipedia page for {self.name}...")
            webbrowser.open(url)
        else:
            print(f"Wikipedia page for '{self.name}' not found.")

# Interactive part
if __name__ == "__main__":
    user_input = input("Enter the name of an ingredient: ")
    ingredient = Ingredient(user_input, 1)
    ingredient.get_info()