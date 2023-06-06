from pokemon_main_types import ElectricPokemon, FirePokemon, WaterPokemon, GhostPokemon
import time
import sys

# got this func from here https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
# + one additional new line print at the end of the loop

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
    print('\n')

# test pokemon
pikachu = ElectricPokemon('Pikachu', 120)
charmander = FirePokemon('Charmander', 150)
bulbasour = WaterPokemon('Bulbosour', 130)
ghastly = GhostPokemon('Ghastly', 90)

charizard = FirePokemon('Charizard', 1500)
