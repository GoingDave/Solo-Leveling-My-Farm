import time
import os
import pygame

pygame.mixer.init()

Main_Music = "SalmonLikeTheFish - Zion.mp3"
Night_Music = "559100__saralana__owl-at-night.wav"

def spiele_main():
    pygame.mixer.music.load(Main_Music)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

Day_Count = 1
Pflanzen = 0
Aktueller_Wasserverbrauch = 0
Coins = 100
Generator_Count = 1
Water_Tank_Count = 1
Max_Wasserverbrauch = Water_Tank_Count * 100
generated_energy = Generator_Count * 50
used_energy = 0
today_harvested = 0

def Stats():
    global today_harvested
    print("\n-----------------------------------------------------------------------")
    print("Your stats:")
    print(f"Days ☀️:: {Day_Count}")
    print(f"Plants 🌱: {Pflanzen}")
    print(f"Water consumption 💧: {Aktueller_Wasserverbrauch}/{Max_Wasserverbrauch}L")
    print(f"Energy consumption ⚡: {used_energy}/{generated_energy}W")
    print(f"Coins 💰: {Coins}")
    print(f"Total Harvested today: {today_harvested} Coins")
    stats_back = input("To go Back, press 1\n")
    if stats_back in ["1"]:
        Day_Task()

def Night_Animation():
    sleep_frames = [
        "Zzz... 🌙💤               ",
        "Zzz... 🌙💤 💤            ",
        "Zzz... 🌙💤 💤 💤         ",
        "Zzz... 🌙💤 💤 💤 💤      ",
        "Zzz... 🌙💤 💤 💤 💤 💤  ",
        "                            "
    ]
    print("\n\n\n")
    print("                            ")
    print("\n\n\n")
    for i in range(3):
        for frame in sleep_frames:
            print(frame, end="\r\n\n\n\n")
            time.sleep(0.5)
    print("\n\n")


Harvest_Done = False
Ertrag = 0
Wheat_Count = 0
Corn_Count = 0
Potato_Count = 0
Sunflower_Count = 0
Apple_Tree_Count = 0
Cherry_Tree_Count = 0
Pear_Tree_Count = 0
Orange_Tree_Count = 0
Strawberry_Bush_Count = 0
Raspberry_Bush_Count = 0
Blueberry_Bush_Count = 0
Blackberry_Bush_Count = 0

water_consumption = {
    "wheat": 5,
    "corn": 10,
    "potatoes": 50,
    "sunflowers": 100,
    "apple_tree": 8,
    "cherry_tree": 16,
    "pear_tree": 32,
    "orange_tree":64,
    "strawberry_bush": 12,
    "raspberry_bush": 24,
    "blueberry_bush": 48,
    "blackberry_bush": 96
}
Infrastructure_prices = {
    "generator": 50,
    "water_tank": 300
}

plant_prices = {
    "wheat": 25,
    "corn": 50,
    "potatoes": 100,
    "sunflowers": 200,
    "apple_tree": 40,
    "cherry_tree": 80,
    "pear_tree": 160,
    "orange_tree":320,
    "strawberry_bush": 60,
    "raspberry_bush": 120,
    "blueberry_bush": 240,
    "blackberry_bush": 480
}

crop_yield = {
    "wheat": 2.5,
    "corn": 5,
    "potatoes": 10,
    "sunflowers": 20,
    "apple_tree": 4,
    "cherry_tree": 8,
    "pear_tree": 16,
    "orange_tree": 32,
    "strawberry_bush": 6,
    "raspberry_bush": 12,
    "blueberry_bush": 24,
    "blackberry_bush": 48
}

plant_unlock_day = {
    "wheat": 1,
    "corn": 20,
    "potatoes": 40,
    "sunflowers": 80,
    "apple_tree": 16,
    "cherry_tree": 32,
    "pear_tree": 64,
    "orange_tree": 128,
    "strawberry_bush": 24,
    "raspberry_bush": 48,
    "blueberry_bush": 96,
    "blackberry_bush": 198
}

def Field_Crops():
    global Coins, Wheat_Count, Corn_Count, Potato_Count, Sunflower_Count, Ertrag, Pflanzen, Max_Wasserverbrauch, Aktueller_Wasserverbrauch, used_energy
    
    print("\n-----------------------------------------------------------------------")
    Field_Crops_Choice = input(f"Which Field Crop do you want to plant?\nYou have {Coins} Coins\n1. Wheat 🌾 (20 Coins)\n2. Corn 🌽 (50 Coins)\n3. Potatoes 🥔 (100 Coins)\n4. Sunflowers 🌻 (200 Coins)\n\n").lower().strip()

    if Field_Crops_Choice in ["1", "wheat"]:    
        crop_name = "wheat"
        crop_count = "Wheat_Count"
    elif Field_Crops_Choice in ["2", "corn"]:
        crop_name = "corn"
        crop_count = "Corn_Count"
    elif Field_Crops_Choice in ["3", "potatoes"]:
        crop_name = "potatoes"
        crop_count = "Potato_Count"
    elif Field_Crops_Choice in ["4", "sunflowers"]:
        crop_name = "sunflowers"
        crop_count = "Sunflower_Count"
    else:
        print("Invalid choice. Please try again.")
        return

    if Day_Count < plant_unlock_day[crop_name]:
        print(f"You have to reach day {plant_unlock_day[crop_name]} to buy {crop_name.replace('_', ' ').capitalize()}")
        time.sleep(2)
        return
    if Max_Wasserverbrauch < Aktueller_Wasserverbrauch + water_consumption[crop_name]:
        print("You don't have enough water to plant this crop.")
        time.sleep(2)
        return

    if generated_energy < used_energy + 25:
        print(f"You have to build a new generator to power the water pump.")
        time.sleep(2)
        return

    if Coins >= int(plant_prices[crop_name]):
        Coins -= plant_prices[crop_name]
        globals()[crop_count] += 1
        Pflanzen +=1
        used_energy += 25
        Aktueller_Wasserverbrauch += water_consumption[crop_name]
        Ertrag += crop_yield[crop_name]
        
        print(f"You planted 1 {crop_name.capitalize()}! 🌱 (Remaining Coins: {Coins})")
    else:
        print(f"Not enough Coins! You need {plant_prices[crop_name] - Coins} more. ❌")

def Fruit_Trees():
    global Coins, Apple_Tree_Count, Cherry_Tree_Count, Pear_Tree_Count, Orange_Tree_Count, Ertrag, Pflanzen, Max_Wasserverbrauch, Aktueller_Wasserverbrauch, used_energy
    
    print("\n-----------------------------------------------------------------------")
    Fruit_Tree_Choice = input(f"Which Fruit Tree do you want to plant?\nYou have {Coins} Coins\n1. Apple Tree 🍏 (30 Coins)\n2. Cherry Tree 🍒 (80 Coins)\n3. Pear Tree 🍐 (150 Coins) \n4. Orange Tree 🍊 (300 Coins)\n\n").lower().strip()

    if Fruit_Tree_Choice in ["1", "appletree"]:   
        tree_name = "apple_tree"
        tree_count = "Apple_Tree_Count"
    elif Fruit_Tree_Choice in ["2", "cherrytree"]:
        tree_name = "cherry_tree"
        tree_count = "Cherry_Tree_Count"
    elif Fruit_Tree_Choice in ["3", "peartree"]:
        tree_name = "pear_tree"
        tree_count = "Pear_Tree_Count"
    elif Fruit_Tree_Choice in ["4", "orangetree"]:
            tree_name = "orange_tree"
            tree_count = "Orange_Tree_Count"
    else:
        print("Invalid choice. Please try again.")
        return

    if Day_Count < plant_unlock_day[tree_name]:
        print(f"You have to reach day {plant_unlock_day[tree_name]} to buy {tree_name.replace('_', ' ').capitalize()}")
        time.sleep(2)
        return
    
    if Max_Wasserverbrauch < Aktueller_Wasserverbrauch + water_consumption[tree_name]:
        print("You don't have enough water to plant this tree.")
        time.sleep(2)
        return
    
    if generated_energy < used_energy + 25:
        print(f"You have to build a new generator to power the water pump.")
        time.sleep(2)
        return
    
    if Coins >= plant_prices[tree_name]:
        Coins -= plant_prices[tree_name]
        globals()[tree_count] += 1
        Pflanzen +=1
        used_energy += 25
        Aktueller_Wasserverbrauch += water_consumption[tree_name]
        Ertrag += crop_yield[tree_name]
        print(f"You planted 1 {tree_name.replace('_', ' ').capitalize()}! 🌳 (Remaining Coins: {Coins})")
    else:
        print(f"Not enough Coins! You need {plant_prices[tree_name] - Coins} more. ❌")

def Berry_Bushes():
    global Coins, Strawberry_Bush_Count, Raspberry_Bush_Count, Blueberry_Bush_Count, Blackberry_Bush_Count, Ertrag, Pflanzen, Max_Wasserverbrauch, Aktueller_Wasserverbrauch, used_energy
    
    print("\n-----------------------------------------------------------------------")
    Berry_Bushes_Choice = input(f"Which Berry Bush do you want to plant?\nYou have {Coins} Coins\n1. Strawberry Bush 🍓 (25 Coins)\n2. Raspberry Bush 🍇 (60 Coins)\n3. Blueberry Bush 🫐 (120 Coins)\n4. Blackberry Bush 🖤🍇 (250 Coins)\n\n").lower().strip()

    if Berry_Bushes_Choice in ["1", "strawberrybush"]:
        bush_name = "strawberry_bush"
        bush_count = "Strawberry_Bush_Count"
    elif Berry_Bushes_Choice in ["2", "raspberrybush"]:
        bush_name = "raspberry_bush"
        bush_count = "Raspberry_Bush_Count"
    elif Berry_Bushes_Choice in ["3", "blueberrybush"]:
        bush_name = "blueberry_bush"
        bush_count = "Blueberry_Bush_Count"
    elif Berry_Bushes_Choice in ["4", "blackberrybush"]:
        bush_name = "blackberry_bush"
        bush_count = "Blackberry_Bush_Count"
    else:
        print("Invalid choice. Please try again.")
        return

    if Day_Count < plant_unlock_day[bush_name]:
        print(f"You have to reach day {plant_unlock_day[bush_name]} to buy {bush_name.replace('_', ' ').capitalize()}")
        time.sleep(2)
        return
    
    if Max_Wasserverbrauch < Aktueller_Wasserverbrauch + water_consumption[bush_name]:
        print("You don't have enough water to plant this bush.")
        time.sleep(2)
        return
    
    if generated_energy < used_energy + 25:
        print(f"You have to build a new generator to power the water pump.")
        time.sleep(2)
        return
    
    if Coins >= plant_prices[bush_name]:
        Coins -= plant_prices[bush_name]
        globals()[bush_count] += 1
        Pflanzen +=1
        used_energy += 25
        Aktueller_Wasserverbrauch += water_consumption[bush_name]
        Ertrag += crop_yield[bush_name]
        print(f"You planted 1 {bush_name.replace('_', ' ').capitalize()}! 🍇 (Remaining Coins: {Coins})") 
    else:
        print(f"Not enough Coins! You need {plant_prices[bush_name] - Coins} more. ❌")

def Crops_Menu():
    print("\n-----------------------------------------------------------------------\nCrops Menu:")
    Crop_Type_Choice = input("What do you want to plant?\n\n1. 🌾 Field Crops\n\n2. 🍎 Fruit Trees\n\n3. 🍓 Berry Bushes\n").lower().strip()
    if Crop_Type_Choice in ["1", "fieldcrops"]:
        Field_Crops()
    elif Crop_Type_Choice in ["2", "fruittrees"]:
        Fruit_Trees()
    elif Crop_Type_Choice in ["3", "berrybushes"]:
        Berry_Bushes()

def Harvest():
    global Ertrag, Coins, Harvest_Done, today_harvested
    if Harvest_Done:
        print("You've already harvested today. Come back tomorrow!")
        return
    
    
    total_earnings = 0
    total_earnings += Wheat_Count * crop_yield["wheat"]
    total_earnings += Corn_Count * crop_yield["corn"]
    total_earnings += Potato_Count * crop_yield["potatoes"]
    total_earnings += Sunflower_Count * crop_yield["sunflowers"]
    total_earnings += Apple_Tree_Count * crop_yield["apple_tree"]
    total_earnings += Cherry_Tree_Count * crop_yield["cherry_tree"]
    total_earnings += Pear_Tree_Count * crop_yield["pear_tree"]
    total_earnings += Orange_Tree_Count * crop_yield["orange_tree"]
    total_earnings += Strawberry_Bush_Count * crop_yield["strawberry_bush"]
    total_earnings += Raspberry_Bush_Count * crop_yield["raspberry_bush"]
    total_earnings += Blueberry_Bush_Count * crop_yield["blueberry_bush"]
    total_earnings += Blackberry_Bush_Count * crop_yield["blackberry_bush"]

    earned_coins = total_earnings * 20
    if earned_coins == 0:
        print("You don't have anything to harvest")
        return
    
    Coins += earned_coins
    today_harvested = earned_coins
    
    print(f"You harvested your crops! 🌾You earned {earned_coins} Coins today from your crops! (Total Coins: {Coins})")

    Harvest_Done = True
    
def Infrastructure():
    global Coins, Generator_Count, Water_Tank_Count, generated_energy
    Answer_Infrastructure = input(f"What do you want to buy?\nYou have {Coins} Coins.\n1. Generator (+50W), 50 Coins⚡\n2. Water tank(+100L), 300 Coins💧\n").lower().strip()
    if Answer_Infrastructure in ["1", "generator"]:
        infrastructure_name = "generator"
        infrastructure_count = "Generator_Count"
    elif Answer_Infrastructure in ["2", "watertank"]:
        infrastructure_name = "water_tank"
        infrastructure_count = "Water_Tank_Count"
    else:
        print("Invalid choice. Please try again.")
        return

    if Coins >= Infrastructure_prices[infrastructure_name]:
        Coins -= Infrastructure_prices[infrastructure_name]
    globals()[infrastructure_count] += 1
    generated_energy = Generator_Count * 50


    print(f"You've bought 1 {infrastructure_name.replace('_', ' ').capitalize()}")

def New_Day():
    global Day_Count, Harvest_Done, Ertrag, today_harvested
    
    today_harvested = 0

    Day_Count += 1
    
    Harvest_Done = False
    
    print(f"Starting Day {Day_Count}... 🌞\n\n\n")
    time.sleep(2)
    Day_Task()

def New_Day_Line():
    print("-----------------------------------------------------------------------\n\n-----------------------------------------------------------------------")

def Do_Day_Count():
    print(f"\n\n\nToday is your {Day_Count}. day.\n\n\n-----------------------------------------------------------------------")

def Day_Task():
    Answer_Day_Task = input("What do you want to do today?\n1. Stats 📜\n2. Plant 🌱\n3. Infrastructure ⚡💧\n4. Harvest 🌾\n5. Sleep 🌙\n6. Quit 👋\n\n").lower().strip()
    if Answer_Day_Task in ["1", "stats"]:
        Stats()
    elif Answer_Day_Task in ["2", "plant"]:
        Crops_Menu()
        time.sleep(3)
        Day_Task()
    elif Answer_Day_Task in ["3", "infrastructure"]:
        Infrastructure()
        time.sleep(3)
        Day_Task()
    elif Answer_Day_Task in ["4", "harvest"]:
        Harvest()
        time.sleep(3)
        Day_Task()
    elif Answer_Day_Task in ["5", "sleep"]:
        Night_Animation()
        New_Day()
        time.sleep(3)
    elif Answer_Day_Task in ["6", "quit", "exit"]:
        print("Goodbye, Farmer! 👋")
        pygame.mixer.music.stop()
    else:
        print("Invalid action. Try again!")
        time.sleep(2)
        Day_Task()


game_start = False
try:
    answer1 = input("Do you want to start a new game?\n1. Yes\n2. No\n   ").strip().lower()

    if answer1 in ["1", "yes"]:
        print("You've chosen 'Yes'.")
        game_start = True
    elif answer1 in ["2", "no"]:
        print("You've chosen 'No'.")
    else:
        print("Error. Try again.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

if game_start:
    spiele_main()
    print("Starting new game...")
    New_Day_Line()
    Do_Day_Count()
    time.sleep(2)
    Day_Task()
else:
    print("No Game has been started.")
