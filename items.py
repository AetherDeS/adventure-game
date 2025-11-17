# items.py

import random

class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, player):
        if isinstance(self.effect, int):
            player.health += self.effect
            print(f"{player.name} съел {self.name}. Здоровье изменилось на {self.effect}")
        else:
            print("Ошибка эффекта предмета")


class Food(Item):
    pass


class PoisonousFood(Food):
    pass


berries = Food(name="ягоды", effect=-random.randint(-5, 5))
apples = Food(name="яблоки", effect=+random.randint(5, 10))
poison_mushrooms = PoisonousFood(name="ядовитые грибы", effect=-random.randint(2, 5))