from abc import ABC

#main abstract pokemon class from which every other class is made
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
