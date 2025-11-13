
class Entity:
    def __init__(self, name: str, hp: int, defense: int, atack: int):
        self.name = name
        self.health = hp
        self.defence = defense
        self.atack = atack


player = Entity("Player", 20, 4, 12)
player.strength = 1
# player.agility = 1

print(player.strength)