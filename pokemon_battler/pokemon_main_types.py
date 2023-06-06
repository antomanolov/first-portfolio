from pokemon_class import Pokemon

class ElectricPokemon(Pokemon):
    def __init__(self, name, hp, level=0, battles_won=0) -> None:
        super().__init__(name, 'electric', hp, level, battles_won, {'Electrify': 5, 'Fusion Bolt': 12, 'Zap Cannon': 15, 'Wildbolt Storm': 26})

class FirePokemon(Pokemon):
    def __init__(self, name, hp, level=0, battles_won=0) -> None:
        super().__init__(name, 'fire', hp, level, battles_won, {'Fiery Dance': 6, 'Fire Lash': 10, 'Eruption': 12, 'Magma Storm': 40})

class WaterPokemon(Pokemon):
    def __init__(self, name, hp, level=0, battles_won=0) -> None:
        super().__init__(name, 'water', hp, level, battles_won, {'Aqua Cutter': 6.7, 'Oceanic Operetta': 10, 'Bubble Beam': 11.5, 'Wave Crash': 27} )

class GhostPokemon(Pokemon):
    def __init__(self, name, hp, level=0, battles_won=0) -> None:
        super().__init__(name, 'ghost', hp, level, battles_won, {'Hex': 5.5, 'Ominous Wind': 7.8, 'Phantom Force': 14, 'Infernal Parade': 33})

