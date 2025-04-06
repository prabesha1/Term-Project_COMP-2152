import random
import sys

class DimensionTravel:
    def __init__(self):
        self.worlds = ["Fire Land", "Ice Land", "Gravity Land", "Time Land"]
        self.chosen_world = random.choice(self.worlds)

    def apply_effect(self, hero, monster):
        print("    ------------------------------------------------------------------")
        print("    |    The monster begins to glow with strange energy...")
        print("    |    It activates... DIMENSION TRAVEL!")

        [print("    |    Monster is teleporting to:", world) for world in self.worlds if world == self.chosen_world]

        if self.chosen_world == "Fire Land":
            print("    |    🔥 The monster is empowered by fire!")
            monster.combat_strength += 2

        elif self.chosen_world == "Ice Land":
            print("    |    ❄️ Ice chills the battlefield! Both lose 2 health.")
            hero.health_points -= 2
            monster.health_points -= 2

        elif self.chosen_world == "Gravity Land":
            print("    |    🌌 Gravity crushes all! Strengths decrease.")
            hero.combat_strength -= 1
            monster.combat_strength -= 1

        elif self.chosen_world == "Time Land":
            print("    |    🕒 Time freezes... The fight ends in a draw.")
            print("    |    Both combatants are teleported away.")
            sys.exit()
