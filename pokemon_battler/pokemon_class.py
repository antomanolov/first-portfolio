from abc import ABC

class Pokemon(ABC):
    def __init__(self, name, type, hp, level = 0, battles_won = 0, attacks = None) -> None:
        self.name = name
        self.type = type
        self.hp = hp
        self.level = level
        self.battles_won = battles_won
        self.attacks = attacks
    
    # I will try to add properties with getters latter with other stuff
    # this problem was resolved with the use of inheritence
    # @property
    # def type(self):
    #     return self._type
    
    # @type.setter
    # def type(self, value):
    #     if value == 'lightning':
    #         self.attacks = ['electro clash']
    #         self._type = value
    
    def poke_battle(self, other):
        if self.hp > other.hp:
            print(f'{self.name} won the battle')
            self.battles_won += 1
            self.level += 1
    
    
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

