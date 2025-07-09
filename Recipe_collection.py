import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://codingnomads.github.io/"

index_response = requests.get(BASE_URL + "recipes/")
index_soup = BeautifulSoup(index_response.text, "html.parser")

recipe_links = []

for a in index_soup.find_all("a"):
    href = a.get("href", "")
    if href.startswith("recipes/") and href.endswith(".html"):
        recipe_links.append(BASE_URL + href)

print("Recipe links found:", recipe_links)
print(f"Total links: {len(recipe_links)}")

all_recipes = []

for link in recipe_links:
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.find("h1").text.strip()
    li_tags = soup.find_all("li")
    li_texts = [li.text.strip() for li in li_tags]

    recipe_data = {
        "title": title,
        "content": li_texts,
        "url": link
    }
    all_recipes.append(recipe_data)

with open("codingnomads_recipes.json", "w", encoding="utf-8") as f:
    json.dump(all_recipes, f, indent=2, ensure_ascii=False)

print(f"{len(all_recipes)} recipes saved to codingnomads_recipes.json ✅")

