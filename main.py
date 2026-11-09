import os
import time




room_types = {
            "start": "A new adventure begins",
            "fog": "The dense fog",
            "grass": "Plain grass", 
            "chest": "Cleaning with a chest",
            "tall_grass": "Tall grass",
            "archway": "Stone archway",
            "end_fight":"The end?",
            "freedom": "The end."
            }

game_active = True

turn_input = ""

class Rooms:
    room_event = {}

class TextData:
    room_descripton = {
        "start": "You find yourself in some mystical woods with fog all around, dense trees and seemingly no easy way out. \nYour options are simple, give up and starve here, or go explore this area. \nDetermined, Thea looks around, explores her surroundings and ultimatively decides for the less tragic ending\n",
        "tall_grass": "",
        "grass": "You find nothing really here, just some clovers, flowers and other foliages spread around. \nYou could search for a 4-leaf clover here and pick it up, if you're lucky enough to find one.\n\n"
    }   
    room_directions = {
        "fog": ", there is dense fog blocking your sight",
        "fallen_tree": ", there is a fallen down tree, you can't go this way.",
        "grass":", there is nothing but grass",
        "tall_grass": ", there is some tall grass that hinders your visibility.",
        "chest": ", there is a clearing where sunlight shines onto a very shiny chest."
        ""
    }

class Game:
    current_game_state = 0
    current_room_type = "start"
    directions = [
        ["fallen_tree", "grass", "fallen_tree"],
        ["grass", "tall_grass", "grass"],
        []
        ]
    locations = [
        ["",1,""],
        [2,3,4],
        []
    ]
    current_location = 0
    location_history = [current_location]
    room_type_history = [current_room_type]
    blocked_directions = []
    fight_active = False

class Player:
    health = 20
    mana = 10
    defense = 1
    attack = 1
    mg_attack_1 = 0
    mg_attack_2 = 0
    inventory = []

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
        GameStart()
    elif startup_input == "2": 
        Tutorial()
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
        "(1/5)\n\n" \
        "\n" \
        "Type any key to continue...")
    input()
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
    input()
    ClearCLI()
    print ("Actions\n\n"
        "[1] Attack   [2] Inspect   [3] Beg for Mercy   [4] Flee   [5] Items\n\n" \
        "These are the actions you can take per turn. For options [Attack] and [Items] a submenu opens.\n"
        "From there you choose in which way you want to attack, or which item to use, by typing the number and pressing Enter. \n\n"
        "(3/5)\n\n" \
         "\n" \
         "Type any key to continue...")
    input()
    ClearCLI()
    print ("Movement\n\n"
        "> To your left, there is a fallen down tree, you can't go this way.\n" \
        "> In front of you, there is nothing but grass \n"
        "> To your right, theres a fallem down tree, you can't go this way. \n\n"
        "[2] Go Straight [4] Go Back \n\n\n"
        "This is an example for the current location you're at. You will always get a short description of whats in the location ahead. \n" \
        "You can move to your left, your right, to the location straight in front of you, or back to the location you've came from.. Your available options are listed below the descriptions.\n" \
        "Type the number corresponding to the direction you want to go and press Enter to confirm.\n\n"
        "(4/5)\n\n" \
        "\n" \
        "Type any key to continue...")
    input()
    ClearCLI()
    print ("You've encountered the end of the tutorial\n\n"
        "Got what you've need to go on this adventure? Great. Take this.\n\n" \
        "+1 Apple \n\n"
        "You can use it in a fight to restore HP.\n\n"
        "(5/5)\n\n" \
        "\n" \
        "Type any key to continue...")
    Player.inventory.append("Apple")
    input()
    ClearCLI()
    GameStart()

def DrawLocation():

    ClearCLI()
    print(f"{room_types[Game.current_room_type]}\n\n\n"
        f"{TextData.room_descripton[Game.current_room_type]}\n"
        f">To your left{TextData.room_directions[Game.directions[Game.current_location][0]]}\n"
        f">In front of you{TextData.room_directions[Game.directions[Game.current_location][1]]}\n"
        f">To your right{TextData.room_directions[Game.directions[Game.current_location][2]]}\n")
    
    if Game.blocked_directions[0] == False:
        print("[1] Go to the Left    ", end=" ")
    if Game.blocked_directions[1] == False:
        print("[2] Go Straight    ", end=" ")
    if Game.blocked_directions[2] == False:
        print("[3] Go to the Right    ", end=" ")
    if Game.current_location != 0:
        print("[4] Go Back    ", end=" ")
    print("\n")

def MoveLocation():
    turn_input = input()
    
    if Game.blocked_directions[0] == False and turn_input == "1":
        Game.current_room_type = Game.directions[Game.current_location][0]
        Game.current_location = Game.locations[Game.current_location][0]
        Game.location_history.append(Game.current_location)
        Game.room_type_history.append(Game.current_room_type)
    elif Game.blocked_directions[1] == False and turn_input == "2":
        Game.current_room_type = Game.directions[Game.current_location][1]
        Game.current_location = Game.locations[Game.current_location][1]
        Game.location_history.append(Game.current_location)
        Game.room_type_history.append(Game.current_room_type)
    elif Game.blocked_directions[2] == False and turn_input == "3":
        Game.current_room_type = Game.directions[Game.current_location][2]
        Game.current_location = Game.locations[Game.current_location][2]
        Game.location_history.append(Game.current_location)
        Game.room_type_history.append(Game.current_room_type)
    elif Game.current_location != 0 and turn_input == "4":
        Game.location_history.pop()
        Game.room_type_history.pop()
        Game.current_location = Game.location_history[-1]
        Game.current_room_type = Game.room_type_history[-1]
      
def GameStart():
    Game.current_game_state = 1

def EnvironmentEvent():

   #Check for valid directions 
    Game.blocked_directions.clear()
    for x in Game.directions[Game.current_location]:
        if x == "fallen_tree":
            Game.blocked_directions.append(True)
        else:
            Game.blocked_directions.append(False)   

def GameTurn():
    #print(Game.room_type_history)
    EnvironmentEvent()
    if Game.fight_active == False:
        DrawLocation()
        MoveLocation()
    else:
        FightTurn()
        DrawFight()





while game_active:

    if Game.current_game_state == 0:
        Startup()

    if Game.current_game_state == 1:
        GameTurn()
    
    if Game.current_game_state == 2:
        game_active = False
        print ("You win! \nc:")



