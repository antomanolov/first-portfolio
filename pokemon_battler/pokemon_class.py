class Pokemon:
    def __init__(self, name, type, hp, level = 0, battles_won = 0) -> None:
        self.name = name
        self.type = type
        self.hp = hp
        self.level = level
        self.battles_won = battles_won
    

pokemon_a = Pokemon('Pikachu', 'lightning', 100)
print(pokemon_a.name)