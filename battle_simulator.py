from Pokemon import Pokemon 

pikachu = Pokemon("Picachu", "grass", 120)
charmander = Pokemon("Charmander", "fire", 130)

print(pikachu)
print(charmander)

pikachu.battle(charmander)
charmander.battle(pikachu)

pikachu.feed()
charmander.feed()