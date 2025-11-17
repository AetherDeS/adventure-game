# entities.py

import random

class Entity:
    def __init__(self, name, health=100, armor=0, base_attack_power=10):
        self.name = name
        self.health = health
        self.armor = armor
        self.base_attack_power = base_attack_power

    def is_alive(self):
        return self.health > 0

    def calculate_damage(self):
        """Возвращает случайный урон в диапазоне от (базового_урона - 10) до (базового_урона + 10)"""
        return random.randint(max(self.base_attack_power - 10, 0), self.base_attack_power + 10)

    def take_damage(self, damage):
        effective_damage = max(damage - self.armor, 0)
        self.health -= effective_damage
        print(f"{self.name} получил {effective_damage} урона. Текущее здоровье: {self.health}/100.")


class Player(Entity):
    def __init__(self, name="Игрок"):
        super().__init__(name=name, health=100, armor=10, base_attack_power=15)


class Rat(Entity):
    def __init__(self):
        super().__init__(name="Крыса", health=30, armor=0, base_attack_power=8)


class Ent(Entity):
    def __init__(self):
        super().__init__(name="Энт", health=80, armor=5, base_attack_power=12)