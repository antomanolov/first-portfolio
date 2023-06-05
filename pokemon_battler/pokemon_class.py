from abc import ABC

class Pokemon(ABC):
    def __init__(self, name, type, hp, level = 0, battles_won = 0) -> None:
        self.name = name
        self.type = type
        self.hp = hp
        self.level = level
        self.battles_won = battles_won
        self.attacks = [None]
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, value):
        if value == 'lightning':
            self.attacks = ['electro clash']
            self._type = value
 
       

        

pokemon_a = Pokemon('Pikachu', 'lightning', 100)
pokemon_a.type = 'lightning'
print(pokemon_a.type)

# class Person:
#     def __init__(self, name, location):
#         self.name = name
#         self.past_locations = []
#         self.location = location

#     @property
#     def location(self):
#         return self._location

#     @location.setter
#     def location(self, location):
#         self._location = location
#         self.past_locations.append(location)

# person_a = Person('Andrei', 'Aurora')
# person_a.location = 'Serbia'
# print(person_a.past_locations)
