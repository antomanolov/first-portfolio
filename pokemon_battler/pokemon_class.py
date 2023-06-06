from abc import ABC
from delay_function import delay_print

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
        delay_print('---LET THE BATTLE BEGGIN---')
        delay_print(f'---{self.name}---')
        delay_print('---VS---')
        delay_print(f'---{other.name}---')
        current_pokemon = self
        while self.hp > 0 and other.hp > 0:
            delay_print(f'GO --{current_pokemon.name}--')
            delay_print(f'{current_pokemon.name} attack list:')
            printable_attacks, list_of_attacks = choose_attack(current_pokemon)
            delay_print(printable_attacks)
            int_of_choice = int(input('Choose your attack: '))
            key = list_of_attacks[int_of_choice - 1]
            dmg_dealt = current_pokemon.attacks[key]
            delay_print(f'---{current_pokemon.name}--- DEALT {dmg_dealt} DMG')
            if current_pokemon == self:
                other.hp -= dmg_dealt
                print(f'---{other.name}--- is on {other.hp} HP')
                if other.hp <= 0:
                    delay_print(f'---{other.name}--- FAINTED ---{self.name}-- WON THE BATTLE')
                    
                else:
                    current_pokemon = other
            else:
                self.hp -= dmg_dealt
                delay_print(f'---{self.name}--- is on {self.hp} HP')
                if self.hp <= 0:
                    delay_print(f'---{self.name}--- FAINTED ---{other.name}-- WON THE BATTLE')
                    
                else:
                    current_pokemon = self

def choose_attack(pokemon):
    to_return = []
    attack_keys = []
    number = 1
    for key in pokemon.attacks:
        to_return.append(f'{number}. {key}')
        attack_keys.append(key)
        number += 1
    return '\n'.join(to_return), attack_keys

