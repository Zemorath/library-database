# lib/helpers.py
from models.item import Item
from models.player import Player
from models.player_items import Player_Items

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

# Item model helper methods

def list_items():
    items = Item.get_all()
    for item in items:
        print(item)

def find_item_by_name():
    name = input("Enter the item's name: ")
    item = Item.find_by_name(name)
    print(item if item else print(
        f'Item {name} not found'
    ))

def find_item_by_id():
    id_ = input("Enter the item's id: ")
    item = Item.find_by_id(id_)
    print(item) if item else print(f'Item {id_} not found')

def create_item():
    name = input("Enter the item's name: ")
    health = input("Enter the item's health: ")
    defense = input("Enter the item's defense: ")
    attack = input("Enter the item's attack: ")
    crit_dmg = input("Enter the item's crit damage: ")
    crit_chance = input("Enter the item's crit chance: ")
    speed = input("Enter the item's speed: ")
    try:
        item = Item.create(name, int(health), int(defense), int(attack), int(crit_dmg), int(crit_chance), int(speed))
        print(f'Success: {item}')
    except Exception as exc:
        print("Error creating item: ", exc)

def update_item():
    id_ = input("Enter the item's id: ")
    if item := Item.find_by_id(id_):
        try:
            name = input("Enter the item's new name: ")
            item.name = name

            health = input("Enter the item's new health: ")
            item.health = int(health)

            defense = input("Enter the item's new defense: ")
            item.defense = int(defense)

            attack = input("Enter the item's new attack: ")
            item.attack = int(attack)

            crit_dmg = input("Enter the item's new crit_dmg: ")
            item.crit_dmg = int(crit_dmg)

            crit_chance = input("Enter the item's new crit_chance: ")
            item.crit_chance = int(crit_chance)

            speed = input("Enter the item's new speed: ")
            item.speed = int(speed)
            
            item.update()
            print(f'Success: {item}')
        except Exception as exc:
            print("Error updating item: ", exc)
    else:
        print(f'Item {id_} not found')

def delete_item():
    id_ = input("Enter the item's id: ")
    if item := Item.find_by_id(id_):
        item.delete()
        print(f'Item {id_} deleted')
    else:
        print(f'Item {id_} not found')

# Player model helper methods
        
def list_players():
    players = Player.get_all()
    for player in players:
        print(player)

def find_player_by_name():
    name = input("Enter the player's name: ")
    player = Player.find_by_name(name)
    print(player if player else print(
        f'Player {name} not found'
    ))

def find_player_by_id():
    id_ = input("Enter the Player's ID: ")
    player = Player.find_by_id(id_)
    print(player) if player else print(f'Player {id_} not found')

def create_player():
    name = input("Enter the player's name: ")
    class_ = input("Enter the player's class: ")
    try:
        player = Player.create(name, class_)
        print(f'Success: {player}')
    except Exception as exc:
        print("Error creating Player: ", exc)

def update_player():
    id_ = input("Enter the player's ID: ")
    if player := Player.find_by_id(id_):
        try:
            name = input("Enter the player's new name: ")
            player.name = name
            class_ = input("Enter the player's new class: ")
            player.player_class = class_

            player.update()
            print(f'Success: {player}')
        except Exception as exc:
            print("Error updating player: ", exc)
    else:
        print(f'Player {id_} not found')

def delete_player():
    id_ = input("Enter the player's ID: ")
    if player := Player.find_by_id(id_):
        player.delete()
        print(f'Player {id_} deleted')
    else:
        print(f'Player {id_} not found')

# Player_Items model helper methods
        
def list_player_items():
    player_items = Player_Items.get_all()
    for pi in player_items:
        print(pi)

def find_pi_by_id():
    id_ = input("Enter the Player_Items' ID: ")
    pi = Player_Items.find_by_id(id_)
    print(pi) if pi else print(f'Player Items {id_} not found')

