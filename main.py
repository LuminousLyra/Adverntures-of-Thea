import os
import time




rooms = ["Room 1","Room 2", "Room 3"]

global current_room

game_active = True

class Game:
    current_room = 0

class Player:
    health = 20
    mana = 10
    defense = 1
    attack = 1
    mg_attack_1 = 0
    mg_attack_2 = 0

def ClearCLI():
    os.system('cls' if os.name == 'nt' else 'clear')

def Startup():
    print("==========\nAdventures of Thea\n==========\n"
        "\n"
        "Do you want to skip the tutorial?\n"
        "[1] Yes     [2] No\n"
        "Type the number here: ")
    
    startup_input = input()
    if startup_input == "1":
        Tutorial()
    elif startup_input == "2": 
        Game.current_room = 2
    else:
        print("\n"
              "You haven't entered a correct answer. Please type either 1 or 2 and press Enter.")
        time.sleep(3)
    ClearCLI()
       

def Tutorial():
    ClearCLI()
    print ("This is a textbased adventure RPG about a heroine called Thea. It is your job to use her \n" \
        "abilities and guide her to safety out of the cursed woods. Be careful! \nStrong monsters are everywhere around!\n" \
        "\n" \
        "(1/5)" \
        "\n" \
        "Type any key to continue...")
    if input() != "":
        ClearCLI()
    print ("Stats\n\n"
        "[[ HP: 20/20    MP: 10/10    -Poison +Strength ]]\n\n" \
        "These are your character stats. HP stands for your health. MP stands for the point you can use \n"
        "your magical abilities with. At the end theres Buffs +(positive effects) and Debuffs -(negative effects)\n\n\n"
        "(( THE PUPPET // HP: 10/10    -Burning +Unlimited Stuffing ))\n\n"
        "This is your enemies stats. Again, HP stands for their health. They can aswell have Buffs and Debuffs.\n\n"
        "(2/5)\n\n" \
        "\n" \
        "Type any key to continue...")
    if input() != "":
            ClearCLI()
    print ("Actions\n\n"
        "[1] Attack   [2] Inspect   [3] Beg for Mercy   [4] Flee   [5] Items\n\n" \
        "These are the actions you can take per turn. For options [Attack] and [Items] a submenu opens.\n"
        "From there you choose in which way you want to attack, or which item to use. \n\n\n"
        "(( THE PUPPET // HP: 10/10    -Burning +Unlimited Stuffing ))\n\n"
        "This is your enemies stats. Again, HP stands for their health. They can aswell have Buffs and Debuffs.\n\n"
        "(2/5)\n\n" \
         "\n" \
         "Type any key to continue...")
    if input() != "":
        ClearCLI()
    
      

  



while game_active:

    if Game.current_room == 0:
        Startup()
    
    if Game.current_room == 2:
        game_active = False
        print ("You win! \nc:")



interactions = [""]

