# lib/cli.py

from helpers import (
    exit_program,
    list_items,
    find_item_by_name,
    find_item_by_id,
    create_item,
    update_item,
    delete_item,
    list_players,
    find_player_by_name,
    find_player_by_id,
    create_player,
    update_player,
    delete_player,
    list_player_items,
    find_pi_by_id,
    create_relationship,
    update_relation,
    delete_relation
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_items()
        elif choice == "2":
            find_item_by_name()
        elif choice == "3":
            find_item_by_id()
        elif choice == "4":
            create_item()
        elif choice == "5":
            update_item()
        elif choice == "6":
            delete_item()
        elif choice == "7":
            list_players()
        elif choice == "8":
            find_player_by_name()
        elif choice == "9":
            find_player_by_id()
        elif choice == "10":
            create_player()
        elif choice == "11":
            update_player()
        elif choice == "12":
            delete_player()
        elif choice == "13":
            list_player_items()
        elif choice == "14":
            find_pi_by_id()
        elif choice == "15":
            create_relationship()
        elif choice == "16":
            update_relation()
        elif choice == "17":
            delete_relation()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
