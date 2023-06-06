from pokemon_main_types import ElectricPokemon, FirePokemon, WaterPokemon, GhostPokemon
from delay_function import delay_print


# tests
pikachu = ElectricPokemon('Pikachu', 120)
charmander = FirePokemon('Charmander', 150)
bulbasour = WaterPokemon('Bulbosour', 130)
ghastly = GhostPokemon('Ghastly', 90)

charizard = FirePokemon('Charizard', 1500)

charizard.poke_battle(pikachu)