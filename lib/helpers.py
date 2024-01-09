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

