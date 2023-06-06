from pokemon_main_types import ElectricPokemon, FirePokemon, WaterPokemon, GhostPokemon


pikachu = ElectricPokemon('Pikachu', 120)
charmander = FirePokemon('Charmander', 150)
bulbasour = WaterPokemon('Bulbosour', 130)
ghastly = GhostPokemon('Ghastly', 90)

charizard = FirePokemon('Charizard', 1500)

print(pikachu.attacks)
print(charmander.attacks)
print(bulbasour.attacks)
print(ghastly.attacks)
print(charizard.hp)