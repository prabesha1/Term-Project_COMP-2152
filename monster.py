import random
from character import Character

class Monster(Character):
    def __init__(self):
        combat_strength = random.choice(range(1, 7))
        health_points = random.choice(range(1, 21))
        super().__init__(combat_strength, health_points)

    def monster_attacks(self, hero):
        print(f"Monster attacks with strength {self.combat_strength}")
        hero.health_points -= self.combat_strength 