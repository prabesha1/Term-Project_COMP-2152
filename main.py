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
