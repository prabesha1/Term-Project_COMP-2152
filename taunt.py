import random

class MonsterTaunt:
    """
    The "Monster Taunt" feature adds a layer of interaction and engagement to
    the game by having the monster deliver a short, pre-defined taunt message
    before attacking the hero. This makes the fight sequence more dynamic
    and immersive.
    """
    
    def __init__(self):
        """
        Initialize the taunt system with a list of taunts created using list comprehension.
        """
        # Creating initial taunts using list comprehension
        self.basic_taunts = [f"Taunt {i}" for i in range(1, 6)]
        
        # Replace with a more comprehensive list of actual taunts
        self.monster_taunts = [
            "Grrr! You'll never defeat me!",
            "Is that all you've got?",
            "I'll crush you like a bug!",
            "Your weapons are no match for me!",
            "Prepare to meet your doom!",
            "Your courage is foolish!",
            "Your fate is sealed, hero!",
            "I'll enjoy watching you fall!",
            "Many have tried, all have failed!",
            "Your blood will paint these walls!",
            "You're nothing but a snack to me!",
            "Today is your last day, hero!",
            "I will add your bones to my collection!",
            "There's no escape from my wrath!",
            "Your quest ends here!"
        ]
    
    def get_taunt(self):
        """
        Randomly select a taunt from the list.
        
        Returns:
            str: A randomly selected taunt message.
        """
        return random.choice(self.monster_taunts)
    
    def taunt_hero(self, monster_health, hero_health):
        """
        Using nested conditional statements to check game state before taunting.
        
        Args:
            monster_health (int): Current health points of the monster
            hero_health (int): Current health points of the hero
            
        Returns:
            str or None: A taunt message if conditions are met, None otherwise
        """
        # Using nested conditional statements to check the state
        if monster_health > 0:
            if hero_health > 0:
                taunt = self.get_taunt()
                return taunt
            else:
                # Hero is defeated, use victory taunt
                return "Ha! I knew you were weak! Victory is mine!"
        else:
            # Monster is defeated, no taunt
            return None
            
    def format_taunt(self, taunt):
        """
        Format the taunt message for display.
        
        Args:
            taunt (str): The taunt message to format
            
        Returns:
            str: Formatted taunt message
        """
        if taunt:
            return f"Monster says: '{taunt}'"
        return ""


# Example usage:
# taunt_system = MonsterTaunt()
# 
# # During battle when monster attacks:
# if monster.health_points > 0 and hero.health_points > 0:
#     taunt = taunt_system.taunt_hero(monster.health_points, hero.health_points)
#     formatted_message = taunt_system.format_taunt(taunt)
#     print(formatted_message)
#     monster.monster_attacks(hero) 