# Import the random library to use for the dice later
import random
import os
import platform

# Put all the functions into another file and import them
import function

# Import Hero and Monster classes
from hero import Hero
from monster import Monster


# Import the Shop class from dynamic_shop.py instead of shop.py
from dynamic_shop import DynamicItemShop

# Import Magical Ally class
from ally import Ally

# Import from Dimension_travel class
from Dimension_travel import DimensionTravel



# Print system information
print(f"Operating System: {os.name}")
print(f"Python Version: {platform.python_version()}")

# Instantiate Hero and Monster
hero = Hero()
monster = Monster()

# Define Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = [
    "Health Potion", "Poison Potion", "Secret Note", "Leather Boots",
    "Flimsy Gloves", "King’s Will", "Emperor's Cape"
]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

num_stars = 0

# Create shop instance
shop = DynamicItemShop()

# Create game board
hero_position = [2, 3]  # Start at Row 3, Column D (2,3 in array)
game_board = shop.generate_game_board(hero_position)
current_location = "Wilderness"  # Starting location

# Player loot value
loot_value = 0

# Loop to get valid input for Hero and Monster's Combat Strength

# Input combat strength

i = 0
input_invalid = True
while input_invalid and i < 5:
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    if not combat_strength.isnumeric() or not m_combat_strength.isnumeric():
        print("    |    Invalid input. Enter numbers.")
        i += 1
        continue

    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)
    
    # Update hero's combat strength
    hero.combat_strength = combat_strength
    monster.combat_strength = m_combat_strength


    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    combat_strength = min(6, (combat_strength + weapon_roll))
    hero.combat_strength = combat_strength
    print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

    # Lab 06 - Question 5b
    function.adjust_combat_strength(combat_strength, m_combat_strength)

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Roll for player health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")
    
    # Update hero's health points
    hero.health_points = health_points

    # Roll for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")
    
    # Update monster's health points
    monster.health_points = m_health_points

    if 1 <= combat_strength <= 6 and 1 <= m_combat_strength <= 6:
        input_invalid = False
    else:
        print("    |    Values must be between 1 and 6.")
        i += 1

print("    |", end="    ")
input("Roll the dice for your weapon (Press enter)")
weapon_roll = random.choice(small_dice_options)
combat_strength = min(6, combat_strength + weapon_roll)
print("    |    The hero's weapon is " + str(weapons[weapon_roll - 1]))

function.adjust_combat_strength(combat_strength, m_combat_strength)

print("    |", end="    ")
input("Roll the dice for your health points (Press enter)")
health_points = random.choice(big_dice_options)
print("    |    Player rolled " + str(health_points) + " health points")

print("    |", end="    ")
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(big_dice_options)
print("    |    Player rolled " + str(m_health_points) + " health points for the monster")



print("    |", end="    ")
input("Roll for first loot (enter)")
loot_options, belt = function.collect_loot(loot_options, belt)

print("    |", end="    ")
input("Roll for second loot (enter)")
loot_options, belt = function.collect_loot(loot_options, belt)

belt.sort()
print("    |    Your belt: ", belt)
belt, health_points = function.use_loot(belt, health_points)

print("    |", end="    ")
input("Roll for Monster's Magic Power (Press enter)")
power_roll = random.choice(list(monster_powers.keys()))
m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
print(f"    |    The monster's combat strength is now {m_combat_strength} using {power_roll}")

# 🌌 Dimension Travel Feature
print("    ------------------------------------------------------------------")
print("    |    The monster begins to glow with strange energy...")
print("    |    It activates... DIMENSION TRAVEL!")
worlds = ["Fire Land", "Ice Land", "Gravity Land", "Time Land"]
chosen_world = random.choice(worlds)

# Use list comprehension to show teleport destination
[print("    |    Monster is teleporting to:", world) for world in worlds if world == chosen_world]

# Apply effects based on world
if chosen_world == "Fire Land":
    print("    |    🔥 The monster is empowered by fire!")
    monster.combat_strength += 2

elif chosen_world == "Ice Land":
    print("    |    ❄️ Ice chills the battlefield! Both lose 2 health.")
    hero.health_points -= 2
    monster.health_points -= 2

elif chosen_world == "Gravity Land":
    print("    |    🌌 Gravity crushes all! Strengths decrease.")
    hero.combat_strength -= 1
    monster.combat_strength -= 1

elif chosen_world == "Time Land":
    print("    |    🕒 Time freezes... The fight ends in a draw.")
    print("    |    Both combatants are teleported away.")
    exit()


# ✅ Magical Ally Boost (untouched)
allies = [
    Ally("Fire Spirit", 3, 30),
    Ally("Wind Archer", 2, 20),
    Ally("Stone Golem", 1, 10)
]
eligible_allies = [a for a in allies if m_health_points > a.threshold]

for ally in eligible_allies:
    if m_combat_strength > 10:
        if ally.name == "Fire Spirit":
            print(f"🔥 {ally.name} launches a powerful double attack!")
            m_health_points -= ally.boost * 2
        else:
            print(f"💨 {ally.name} strikes the monster!")
            m_health_points -= ally.boost
    else:
        print(f"🪨 {ally.name} assists the hero.")
        m_health_points -= ally.boost

m_health_points = max(0, m_health_points)
print(f"Monster's health after ally boost: {m_health_points}")

# ✅ Presence of the King — only if ally boost ran
if eligible_allies and combat_strength >= 8 and m_health_points > 0:
    king_items = ["King’s Will", "Emperor's Cape"]
    haki_items = [item for item in belt if item in king_items]

    if haki_items:
        function.show_presence_of_king_animation()

        if m_combat_strength <= 3 or m_health_points <= 3:
            print("💥 The monster collapses instantly from the King's pressure!")
            m_health_points = 0
        elif 4 <= m_combat_strength <= 6:
            print("😨 The monster is weakened. Its strength is halved.")
            m_combat_strength //= 2
        else:
            print("🧿 The monster resists the King's presence.")

        belt.remove(haki_items[0])


# FIGHT STARTS
print("    ------------------------------------------------------------------")
print("    |    You meet the monster. FIGHT!!")


    # Collect Loot First time
loot_options, belt = function.collect_loot(loot_options, belt)
    # Add to hero's inventory
for item in belt:
    if item not in hero.inventory:
            hero.add_to_inventory(item)
            
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")

    # Collect Loot Second time
    loot_options, belt = function.collect_loot(loot_options, belt)
    # Add new items to hero's inventory
    for item in belt:
        if item not in hero.inventory:
            hero.add_to_inventory(item)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)
    print("    |    Your inventory: ", hero.inventory)
    print("    |    Your gold: ", hero.gold)

    # Use Loot
    belt, health_points = function.use_loot(belt, health_points)
    hero.health_points = health_points
    
    # Remove used item from inventory if it was in the belt
    if len(belt) < len(hero.inventory):
        # The first item was used from belt
        used_item = hero.inventory[0]
        hero.inventory.pop(0)

    # Add immediate shop access option
    print("    ------------------------------------------------------------------")
    print("    |    A traveling merchant approaches you!")
    print("    |    Your current loot value is: " + str(min(20, (hero.health_points + hero.combat_strength) // 2)))
    print("    |    Your gold: " + str(hero.gold))
    
    enter_shop = input("    |    Would you like to access the merchant's Dynamic Item Shop? (yes/no): ").lower()
    if enter_shop == "yes":
        # For merchant, we'll use "Traveling Merchant" as location - this allows selling but not Town 2 exclusive items
        loot_value = min(20, (hero.health_points + hero.combat_strength) // 2)
        belt = shop.enter_shop(hero, "Traveling Merchant", belt, loot_value)

    # Display the game board
    print("    ------------------------------------------------------------------")
    print("    |    Game World Map:")
    shop.display_board(game_board)
    print("    |    You are currently at position Row 3, Column D (marked as H)")
    print("    |    Town 1 is at Row 1, Column A (marked as T1)")
    print("    |    Town 2 is at Row 4, Column E (marked as T2)")

    # Allow player to move on the game board
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Would you like to move on the board? (Press enter)")
    
    move_direction = input("    |    Choose a direction (N/E/S/W): ").upper()
    
    # Process movement using dictionary to map directions to coordinate changes
    directions = {
        "N": (-1, 0),
        "E": (0, 1),
        "S": (1, 0),
        "W": (0, -1)
    }
    
    if move_direction in directions:
        # Calculate new position
        delta_row, delta_col = directions[move_direction]
        new_row = hero_position[0] + delta_row
        new_col = hero_position[1] + delta_col
        
        # Check if the new position is valid (within the 5x5 board)
        if 0 <= new_row < 5 and 0 <= new_col < 5:
            # Update hero position
            hero_position = [new_row, new_col]
            
            # Check if hero has arrived at a town
            if new_row == 0 and new_col == 0:
                current_location = "Town 1"
                print("    |    You have arrived at Town 1!")
            elif new_row == 3 and new_col == 4:
                current_location = "Town 2"
                print("    |    You have arrived at Town 2!")
            else:
                current_location = "Wilderness"
                print("    |    You are in the wilderness.")
                
            # Update the game board with the new hero position
            game_board = shop.generate_game_board(hero_position)
            shop.display_board(game_board)
        else:
            print("    |    You cannot move outside the game board!")
    else:
        print("    |    Invalid direction! Please choose N, E, S, or W.")

    # Enter the shop if in a town
    if current_location in ["Town 1", "Town 2"]:
        print("    ------------------------------------------------------------------")
        print(f"    |    You are in {current_location}. There's a DYNAMIC ITEM SHOP here!")
        print("    |    " + "="*50)
        print("    |    DYNAMIC ITEM SHOP - Special Items Available!")
        print("    |    " + "="*50)
        
        # For demonstration, let's assign a loot value based on the hero's strength and health
        loot_value = min(20, (hero.health_points + hero.combat_strength) // 2)
        print(f"    |    Your current loot value is: {loot_value}")
        print(f"    |    Your gold: {hero.gold}")
        print(f"    |    Your inventory: {hero.inventory}")
        
        # Explain the town-specific shop rules
        if current_location == "Town 2":
            print("    |    Town 2 Special: This shop allows you to BUY premium armor!")
            print("    |    High loot value (10+) will give you a 20% discount!")
        else:
            print("    |    Town 1 Special: This shop allows you to SELL items for better prices!")
        
        enter_shop = input("    |    Would you like to enter the Dynamic Item Shop? (yes/no): ").lower()
        if enter_shop == "yes":
            # Enter the shop with the current hero stats and location
            belt = shop.enter_shop(hero, current_location, belt, loot_value)

while m_health_points > 0 and health_points > 0:
    print("    |", end="    ")
    input("Roll to see who strikes first (Press Enter)")
    attack_roll = random.choice(small_dice_options)

    if attack_roll % 2 != 0:
        input("You strike (Press enter)")
        m_health_points = function.hero_attacks(combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
            break
        input("The monster strikes (Press enter)")
        health_points = function.monster_attacks(m_combat_strength, health_points)
    else:
        input("The Monster strikes (Press enter)")
        health_points = function.monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
            break
        input("The hero strikes!! (Press enter)")
        m_health_points = function.hero_attacks(combat_strength, m_health_points)

    if m_health_points > 0 and health_points > 0:
        num_stars = 2

winner = "Hero" if m_health_points <= 0 else "Monster"


# Final Score
tries = 0
input_invalid = True
while input_invalid and tries < 5:
    print("    |", end="    ")

    input("Analyze the roll (Press enter)")
    # Compare Player vs Monster's strength
    print("    |    --- You are matched in strength: " + str(hero.combat_strength == monster.combat_strength))

    # Check the Player's overall strength and health
    print("    |    --- You have a strong player: " + str((hero.combat_strength + hero.health_points) >= 15))

    # Roll for the monster's power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                

                                      """
    print(ascii_image4)
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

    # Increase the monster's combat strength by its power
    monster.combat_strength += min(6, monster.combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(
        monster.combat_strength) + " using the " + power_roll + " magic power")

    # Lab Week 06 - Question 6
    num_dream_lvls = -1 # Initialize the number of dream levels
    while (num_dream_lvls < 0 or num_dream_lvls > 3):
        # Call Recursive function
        print("    |", end="    ")
        num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3)")
        # If the value entered was not an integer, set the number of dream levels to -1 and loop again 
        if ((num_dream_lvls == "")):
            num_dream_lvls = -1
            print("Number entered must be a whole number between 0-3 inclusive, try again")
    
        else:
            num_dream_lvls = int(num_dream_lvls)

            if ((num_dream_lvls < 0) or (num_dream_lvls > 3)):
                num_dream_lvls = -1
                print("Number entered must be a whole number between 0-3 inclusive, try again")
            elif (not num_dream_lvls == 0):
                hero.health_points -= 1
                crazy_level = function.inception_dream(num_dream_lvls)
                hero.combat_strength += crazy_level
                print("combat strength: " + str(hero.combat_strength))
                print("health points: " + str(hero.health_points))
        print("num_dream_lvls: ", num_dream_lvls)

    # Fight Sequence
    # Loop while the monster and the player are alive. Call fight sequence functions
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while monster.health_points > 0 and hero.health_points > 0:
        # Fight Sequence
        print("    |", end="    ")

        # Lab 5: Question 5:
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)
        if not (attack_roll % 2 == 0):
            print("    |", end="    ")
            input("You strike (Press enter)")
            monster.health_points = function.hero_attacks(hero.combat_strength, monster.health_points)
            if monster.health_points == 0:
                num_stars = 3
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The monster strikes (Press enter)!!!")
                hero.health_points = function.monster_attacks(monster.combat_strength, hero.health_points)
                if hero.health_points == 0:
                    num_stars = 1
                else:
                    num_stars = 2
        else:
            print("    |", end="    ")
            input("The Monster strikes (Press enter)")
            hero.health_points = function.monster_attacks(monster.combat_strength, hero.health_points)
            if hero.health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("The hero strikes!! (Press enter)")
                monster.health_points = function.hero_attacks(hero.combat_strength, monster.health_points)
                if monster.health_points == 0:
                    num_stars = 3
                else:
                    num_stars = 2

    if(monster.health_points <= 0):
        winner = "Hero"

    hero_name = input("Enter your Hero's name (in two words): ")
    name = hero_name.split()

    if len(name) != 2 or not all(part.isalpha() for part in name):
        print("    |    Invalid name. Use two alphabetic words.")
        tries += 1

    else:
        short_name = name[0][:2] + name[1][0]
        print("    |    I'm going to call you " + short_name + " for short")
        input_invalid = False

if not input_invalid:
    stars_display = "*" * num_stars
    print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")
    function.save_game(winner, hero_name=short_name, num_stars=num_stars)
