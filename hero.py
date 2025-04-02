import random
from character import Character

class Hero(Character):
    def __init__(self):
        combat_strength = random.choice(range(1, 7))
        health_points = random.choice(range(1, 21))
        super().__init__(combat_strength, health_points)

    def hero_attacks(self, monster):
        print(f"Hero attacks with strength {self.combat_strength}")
        monster.health_points -= self.combat_strength 