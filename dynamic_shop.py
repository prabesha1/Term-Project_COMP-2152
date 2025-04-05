import random

class DynamicItemShop:
    def __init__(self):
        # Available armor items with their prices and requirements
        self.armor_items = {
            "Leather Vest": {"price": 5, "min_health": 5, "min_strength": 1},
            "Chain Mail": {"price": 10, "min_health": 8, "min_strength": 2},
            "Plate Armor": {"price": 15, "min_health": 10, "min_strength": 3},
            "Dragon Scale": {"price": 25, "min_health": 15, "min_strength": 4},
            "Mythril Coat": {"price": 35, "min_health": 12, "min_strength": 5}
        }
        
        # Available weapons
        self.weapon_items = {
            "Dagger": {"price": 3, "min_strength": 1},
            "Short Sword": {"price": 7, "min_strength": 2},
            "Battle Axe": {"price": 12, "min_strength": 3},
            "War Hammer": {"price": 18, "min_strength": 4},
            "Enchanted Bow": {"price": 22, "min_strength": 3, "min_health": 10}
        }
        
        # Town-specific items
        self.town2_armor = ["Plate Armor", "Dragon Scale", "Mythril Coat"]
    
    def get_available_items(self, hero_health, hero_strength, hero_loot):
        """
        Use list comprehension to generate a list of items the hero can purchase
        based on their current stats
        """
        available_armor = [
            (item_name, details["price"] * 0.8 if hero_loot >= 10 else details["price"])
            for item_name, details in self.armor_items.items()
            if hero_health >= details.get("min_health", 0) and hero_strength >= details.get("min_strength", 0)
        ]
        
        available_weapons = [
            (item_name, details["price"] * 0.8 if hero_loot >= 15 else details["price"])
            for item_name, details in self.weapon_items.items()
            if hero_strength >= details.get("min_strength", 0) and hero_health >= details.get("min_health", 0)
        ]
        
        return {"armor": available_armor, "weapons": available_weapons}
    
    def enter_shop(self, hero, current_location, belt=None, loot_value=0):
        """
        Main shop interaction method that implements the nested conditional logic
        for buying/selling based on hero's location
        """
        print("\n--- You've entered the Dynamic Item Shop marketplace ---")
        print(f"Your gold: {hero.gold}")
        
        # Check if hero is in Town 2
        if current_location == "Town 2":
            print("Welcome to Town 2's Exclusive Armor Shop!")
            buy_choice = input("Would you like to buy armor? (yes/no): ").lower()
            
            if buy_choice == "yes":
                # Nested if: Check if hero qualifies for a discount
                has_discount = loot_value >= 10
                
                if has_discount:
                    print("You qualify for a 20% discount due to your valuable loot!")
                
                # Display armor options available only in Town 2
                print("\nArmor available in Town 2:")
                
                # Using list comprehension to filter items specific to Town 2
                town2_available_armor = [
                    (item_name, details["price"] * 0.8 if has_discount else details["price"])
                    for item_name, details in self.armor_items.items()
                    if item_name in self.town2_armor 
                    and hero.health_points >= details.get("min_health", 0) 
                    and hero.combat_strength >= details.get("min_strength", 0)
                    and details["price"] <= hero.gold  # Only show items the hero can afford
                ]
                
                if town2_available_armor:
                    for idx, (item, price) in enumerate(town2_available_armor, 1):
                        print(f"{idx}. {item} - {price} gold")
                    
                    buy_item = input("Enter the number of the armor you wish to purchase (or 0 to cancel): ")
                    if buy_item.isdigit() and 1 <= int(buy_item) <= len(town2_available_armor):
                        item_idx = int(buy_item) - 1
                        selected_item, price = town2_available_armor[item_idx]
                        
                        # Update hero's gold and add item to inventory
                        hero.gold -= price
                        hero.add_to_inventory(selected_item)
                        
                        print(f"You purchased {selected_item} for {price} gold!")
                        print(f"Remaining gold: {hero.gold}")
                        print(f"Your inventory now contains: {hero.inventory}")
                        
                        # Also update belt if provided
                        if belt is not None:
                            belt.append(selected_item)
                            belt.sort()
                    else:
                        print("Purchase cancelled or invalid selection.")
                else:
                    print("Sorry, you don't qualify for any of the available armor or can't afford them.")
            else:
                print("Perhaps another time then.")
        else:
            # Not in Town 2, can only sell
            print(f"Welcome to the Dynamic Item Shop in {current_location}!")
            sell_choice = input("Would you like to sell items? (yes/no): ").lower()
            
            if sell_choice == "yes":
                if hero.inventory:
                    print("\nYour inventory contains the following items you can sell:")
                    for idx, item in enumerate(hero.inventory, 1):
                        # Generate a random value for the item
                        sell_value = random.randint(3, 8)
                        print(f"{idx}. {item} - {sell_value} gold")
                    
                    sell_item = input("Enter the number of the item you wish to sell (or 0 to cancel): ")
                    if sell_item.isdigit() and 1 <= int(sell_item) <= len(hero.inventory):
                        item_idx = int(sell_item) - 1
                        sold_item = hero.remove_from_inventory(item_idx)
                        sell_value = random.randint(3, 8)
                        
                        # Update hero's gold
                        hero.gold += sell_value
                        
                        print(f"You sold {sold_item} for {sell_value} gold!")
                        print(f"Your gold: {hero.gold}")
                        print(f"Your inventory now contains: {hero.inventory}")
                        
                        # Also update belt if provided and item is in belt
                        if belt is not None and sold_item in belt:
                            belt.remove(sold_item)
                    else:
                        print("Sale cancelled or invalid selection.")
                else:
                    print("You don't have any items to sell.")
            else:
                print("Perhaps another time then.")
        
        return belt if belt is not None else []

    def generate_game_board(self, hero_position):
        """
        Create a 2D array representing the game board with the hero's position
        and static town positions.
        """
        # Create a 5x5 board (rows A-E, columns 1-5)
        board = [['•' for _ in range(5)] for _ in range(5)]
        
        # Set static town positions
        board[0][0] = 'T1'  # Town 1 at Row 1, Column A (0,0 in array)
        board[3][4] = 'T2'  # Town 2 at Row 4, Column E (3,4 in array)
        
        # Set hero position using list comprehension
        board = [
            ['H' if i == hero_position[0] and j == hero_position[1] else cell 
             for j, cell in enumerate(row)]
            for i, row in enumerate(board)
        ]
        
        return board
    
    def display_board(self, board):
        """Display the game board in a readable format"""
        print("\n  1 2 3 4 5")  # Column headers
        for i, row in enumerate(board):
            row_letter = chr(65 + i)  # A, B, C, D, E
            print(f"{row_letter} {' '.join(row)}") 