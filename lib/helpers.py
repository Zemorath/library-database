# lib/helpers.py
from models.item import Item
from models.player import Player
from models.player_items import Player_Items

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_items():
    items = Item.get_all()
    for item in items:
        print(item)