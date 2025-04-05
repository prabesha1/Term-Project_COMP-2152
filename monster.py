import random
from character import Character
from taunt import MonsterTaunt

class Monster(Character):
    def __init__(self):
        combat_strength = random.choice(range(1, 7))
        health_points = random.choice(range(1, 21))
        super().__init__(combat_strength, health_points)
        # Create taunt system
        self.taunt_system = MonsterTaunt()

    def monster_attacks(self, hero):
        # Using nested conditional statements to check if both are alive
        if self.health_points > 0:
            if hero.health_points > 0:
                # Get and display a random taunt before attacking
                taunt = self.taunt_system.taunt_hero(self.health_points, hero.health_points)
                formatted_taunt = self.taunt_system.format_taunt(taunt)
                print(formatted_taunt)
                print(f"Monster attacks with strength {self.combat_strength}")
                hero.health_points -= self.combat_strength 