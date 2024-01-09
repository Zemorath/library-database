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
        item = Item.create(name, health, defense, attack, crit_dmg, crit_chance, speed)
        print(f'Success: {item}')
    except Exception as exc:
        print("Error creating item: ", exc)