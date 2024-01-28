# lib/cli.py

# from helpers import (
#     exit_program,
#     list_items,
#     find_item_by_name,
#     find_item_by_id,
#     create_item,
#     update_item,
#     delete_item,
#     list_players,
#     find_player_by_name,
#     find_player_by_id,
#     create_player,
#     update_player,
#     delete_player,
#     list_player_items,
#     list_players_for_item,
#     find_pi_by_id,
#     create_relationship,
#     update_relation,
#     delete_relation
# )
# from models.item import Item
# from models.player import Player
# from models.player_items import Player_Items


# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             list_items()
#         elif choice == "2":
#             find_item_by_name()
#         elif choice == "3":
#             find_item_by_id()
#         elif choice == "4":
#             create_item()
#         elif choice == "5":
#             update_item()
#         elif choice == "6":
#             delete_item()
#         elif choice == "7":
#             list_players()
#         elif choice == "8":
#             find_player_by_name()
#         elif choice == "9":
#             find_player_by_id()
#         elif choice == "10":
#             create_player()
#         elif choice == "11":
#             update_player()
#         elif choice == "12":
#             delete_player()
#         elif choice == "13":
#             list_player_items()
#         elif choice == "14":
#             list_players_for_item()
#         elif choice == "15":
#             find_pi_by_id()
#         elif choice == "16":
#             create_relationship()
#         elif choice == "17":
#             update_relation()
#         elif choice == "18":
#             delete_relation()
#         elif choice == "19":
#             Item.create_table()
#         elif choice == "20":
#             Item.drop_table()
#         elif choice == "21":
#             Player.create_table()
#         elif choice == "22":
#             Player.drop_table()
#         elif choice == "23":
#             Player_Items.create_table()
#         elif choice == "24":
#             Player_Items.drop_table()
#         elif choice == "25":
#             Player.print_all()
#         else:
#             print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. List all items")
#     print("2. Find item by name")
#     print("3. Find item by id")
#     print("4. Create new item")
#     print("5. Update existing item")
#     print("6. Delete existing item")
#     print("7. List all players")
#     print("8. Find player by name")
#     print("9. Find player by id")
#     print("10. Create new player")
#     print("11. Update existing player")
#     print("12. Delete existing player")
#     print("13. List all items associated with specific player")
#     print("14. List all players associated with specific item")
#     print("15. Find Player-Item relationship by id")
#     print("16. Create new Player-Item relationship")
#     print("17. Update existing Player-Item relationship")
#     print("18. Delete existing Player-Item relationship")
#     print("19. Create new Item table")
#     print("20. Drop existing Item table")
#     print("21. Create new Player table")
#     print("22. Drop existing Player table")
#     print("23. Create new Player-Item association table")
#     print("24. Drop existing Player-Item association table")
#     print("25. Print all variable in players (TEST)")

from helper import (
        list_books,
        find_book_by_title,
        find_book_by_author,
        find_book_by_isbn,
        create_book,
        update_book,
        delete_book,
        list_owners,
        find_owner_by_name,
        create_owner,
        update_owner,
        delete_owner
    )
from models.owners import Owner
from models.books import Book

def main():
    first_choice = 0
    while first_choice != 3:
        print("-Online Library-")
        print("1: Interact with books")
        print("2: Interact with owners")
        print("3: Quit")
        first_choice = int(input())

        if first_choice == 1:
            second_choice = 0
            while second_choice != 6:
                print("--Books--")
                print("1: List books")
                print("2: Find a specific book")
                print("3: Add a new book")
                print("4: Update an existing book")
                print("5: Delete a book")
                print("6: Quit")
                second_choice = int(input())
                
                if second_choice == 1:
                    third_choice = 0
                    while third_choice != 4:
                        print("---List Books---")
                        print("1: All Books")
                        print("2: By Age")
                        print("3: By Genre")
                        print("4: Quit")
                        third_choice = int(input())

                        if third_choice == 1:
                            list_books()
                        # elif choice == 2:
                        #     fill in method
                        # elif choice == 3:
                        #     fill in method
                elif second_choice == 2:
                    third_choice = 0
                    while third_choice != 4:
                        print("---Find a Book---")
                        print("1: By Title")
                        print("2: By Author")
                        print("3: By ISBN")
                        print("4: Quit")
                        third_choice = int(input())

                        if third_choice == 1:
                            find_book_by_title()
                        elif third_choice == 2:
                            find_book_by_author()
                        elif third_choice == 3:
                            find_book_by_isbn()
                        elif third_choice == 4:
                            print("Exiting Program")
                elif second_choice == 3:
                    print("---Creating New Book---")
                    create_book()
                elif second_choice == 4:
                    print("---Updating Existing Book---")
                    update_book()
                elif second_choice == 5:
                    print("---Deleting Book---")
                    delete_book()
                elif second_choice == 6:
                    print("Exiting Program")

if __name__ == "__main__":
    main()
