# Import the random library to use for the dice later
import random
import os
import platform

# Put all the functions into another file and import them
import function

# Import Hero and Monster classes
from hero import Hero
from monster import Monster

# Import Magical Ally class
from ally import Ally

# Print system information
print(f"Operating System: {os.name}")
print(f"Python Version: {platform.python_version()}")

# Instantiate Hero and Monster
hero = Hero()
monster = Monster()

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Input combat strength
i = 0
input_invalid = True
while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    if not combat_strength.isnumeric() or not m_combat_strength.isnumeric():
        print("    |    Invalid input. Enter integer numbers for Combat Strength")
        i += 1
        continue
    elif int(combat_strength) not in range(1, 7) or int(m_combat_strength) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i += 1
        continue
    else:
        input_invalid = False
        break

if not input_invalid:
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    weapon_roll = random.choice(small_dice_options)
    combat_strength = min(6, (combat_strength + weapon_roll))
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

    # Magical Ally Boost: Filter and Attack
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

    # Start the fight
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")

    while m_health_points > 0 and health_points > 0:
        print("    |", end="    ")
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)

        if attack_roll % 2 != 0:
            print("    |", end="    ")
            input("You strike (Press enter)")
            m_health_points = function.hero_attacks(combat_strength, m_health_points)
            if m_health_points == 0:
                num_stars = 3
            else:
                print("    |", end="    ")
                input("The monster strikes (Press enter)")
                health_points = function.monster_attacks(m_combat_strength, health_points)
                num_stars = 1 if health_points == 0 else 2
        else:
            print("    |", end="    ")
            input("The Monster strikes (Press enter)")
            health_points = function.monster_attacks(m_combat_strength, health_points)
            if health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                input("The hero strikes!! (Press enter)")
                m_health_points = function.hero_attacks(combat_strength, m_health_points)
                num_stars = 3 if m_health_points == 0 else 2

    winner = "Hero" if m_health_points <= 0 else "Monster"

    # Final Score
    tries = 0
    input_invalid = True
    while input_invalid and tries < 5:
        print("    |", end="    ")
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
