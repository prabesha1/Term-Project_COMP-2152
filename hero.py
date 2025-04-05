import random
from character import Character

class Hero(Character):
    def __init__(self):
        combat_strength = random.choice(range(1, 7))
        health_points = random.choice(range(1, 21))
        super().__init__(combat_strength, health_points)
        self._gold = 20  # Starting gold for the hero
        self._inventory = []  # Hero's inventory of items
    
    def hero_attacks(self, monster):
        print(f"Hero attacks with strength {self.combat_strength}")
        monster.health_points -= self.combat_strength
    
    @property
    def gold(self):
        return self._gold
    
    @gold.setter
    def gold(self, value):
        self._gold = value
    
    @property
    def inventory(self):
        return self._inventory
    
    def add_to_inventory(self, item):
        self._inventory.append(item)
        self._inventory.sort()  # Keep inventory organized
    
    def remove_from_inventory(self, item_index):
        if 0 <= item_index < len(self._inventory):
            return self._inventory.pop(item_index)
        return None 