from helper import (
        list_books,
        create_book,
        update_book,
        delete_book,
        list_owners,
        list_owners_by_age,
        list_owners_by_fav_genre,
        create_owner,
        update_owner,
        delete_owner,
        list_owners_books,
        grab_owners_books
    )
from models.owners import Owner
from models.books import Book

def main():
    first_choice = 0
    while first_choice != 3:
        print("-Online Library-")
        print("1. Interact with owners")
        print("2. Settings")
        print("3. Quit")
        first_choice = int(input())

        if first_choice == 1:
            second_choice = 0
            while second_choice != 4:
                print("---List Owners---")
                print("1: All Owners")
                print("2: By Age")
                print("3: By Favorite Genre")
                print("4: Back")
                second_choice = int(input())

                while second_choice == 1:
                    print("Here is a list of all owners! Choose one to see more information or edit")
                    owner_choice = 0
                    owners = list_owners()
                    while owner_choice != len(owners) + 2:
                        for i, owner in enumerate(owners, start=1):
                            print(f"{i}. {owner.name}")
                        print("---------")
                        print(f'{(len(owners) + 1)}. Add new owner')
                        print("---------")
                        print(f"{(len(owners) + 2)}. Back")
                        owner_choice = int(input())
                        if owner_choice == len(owners) + 2:
                            print("Moving back")
                            second_choice = 0
                        elif owner_choice == len(owners) + 1:
                            print("Let's add a new owner!")
                            create_owner()
                            owner_choice = len(owners) + 2
                            second_choice = 0
                        elif owner_choice in range(1, len(owners) + 1):
                            book_choice = 0
                            chosen_owner = owners[owner_choice-1]
                            list = grab_owners_books(chosen_owner.id)
                            while book_choice != (len(list) + 4):
                                print("OWNER")
                                print("---------")
                                print(f"{chosen_owner.name} || Age: {chosen_owner.age} || Favorite Genre: {chosen_owner.fav_genre}")
                                print(" ")
                                print("BOOKS: Select one to edit")
                                print("---------")
                                list_owners_books(chosen_owner.id)
                                print(" ")
                                print("Options")
                                print("---------")
                                print(f"{len(list) + 1}: Add a new book")
                                print(f"{len(list) + 2}: Update owner")
                                print(f"{len(list) + 3}: Delete Owner")
                                print(f"{len(list) + 4}: Back")
                                book_choice = int(input())
                                if book_choice == (len(list) + 4):
                                    print("Moving Back!")
                                elif book_choice == (len(list) + 1):
                                    print(f"Adding new book to {chosen_owner.name}")
                                    create_book(chosen_owner.id)
                                    book_choice = len(list) + 4
                                    owner_choice = 0
                                
                                elif book_choice == (len(list) + 2):
                                    print(f"Updating {chosen_owner.name}!")
                                    update_owner(chosen_owner.id)
                                    book_choice = len(list) + 4
                                    owner_choice = 0
                                
                                elif book_choice == (len(list) + 3):
                                    print(f"Deleting {chosen_owner.name}")
                                    delete_owner(chosen_owner.id)
                                    second_choice = 0
                                    owner_choice = len(owners) + 2
                                    book_choice = len(list) + 4
                                    
                                    

                                elif book_choice in range(1, len(list) + 1):
                                    option_choice = 0
                                    while option_choice != 3:
                                        chosen_book = list[book_choice-1]
                                        print(" ")
                                        print("BOOK")
                                        print("---------")
                                        print(f"{chosen_book.title} || Author: {chosen_book.author} || ISBN: {chosen_book.isbn}")
                                        print("---------")
                                        print("1. Update Book")
                                        print("2. Delete Book")
                                        print("3. Back")
                                        option_choice = int(input())
                                        if option_choice == 3:
                                            print("Moving back.")
                                        elif option_choice == 1:
                                            print("Let's Update the Book!")
                                            update_book(chosen_book.id)
                                        elif option_choice == 2:
                                            print("Let's delete the book!")
                                            delete_book(chosen_book.id, chosen_book.title)
                                            option_choice = 3
                                    book_choice = 0
                if second_choice == 2:
                    owner_choice = 0
                    owners = list_owners_by_age()
                    while owner_choice != len(owners) + 1:
                        for i, owner in enumerate(owners, start=1):
                            print(f"{i}. {owner.name}")
                        print("---------")
                        print(f"{(len(owners) + 1)}. Back")
                        owner_choice = int(input())
                        if owner_choice == len(owners) + 1:
                            print("Moving back")
                        else:
                            book_choice = 0
                            chosen_owner = owners[owner_choice-1]
                            list = grab_owners_books(chosen_owner.id)
                            while book_choice != (len(list) + 2):
                                print("OWNER")
                                print("---------")
                                print(f"{chosen_owner.name} || Age: {chosen_owner.age} || Favorite Genre: {chosen_owner.fav_genre}")
                                print(" ")
                                print("BOOKS: Select one to edit")
                                print("---------")
                                list_owners_books(chosen_owner.id)
                                print(" ")
                                print("Options")
                                print("---------")
                                print(f"{len(list) + 1}: Add a new book")
                                print(f"{len(list) + 2}: Back")
                                book_choice = int(input())
                                if book_choice == (len(list) + 2):
                                    print("Moving Back!")

                                elif book_choice == (len(list) + 1):
                                    print(f"Adding new book to {chosen_owner.name}")
                                    create_book(chosen_owner.id)
                                else:
                                    option_choice = 0
                                    while option_choice != 3:
                                        chosen_book = list[book_choice-1]
                                        print(" ")
                                        print("BOOK")
                                        print("---------")
                                        print(f"{chosen_book.title} || Author: {chosen_book.author} || ISBN: {chosen_book.isbn}")
                                        print("---------")
                                        print("1. Update Book")
                                        print("2. Delete Book")
                                        print("3. Back")
                                        option_choice = int(input())
                                        if option_choice == 3:
                                            print("Moving back.")
                                        elif option_choice == 1:
                                            print("Let's Update the Book!")
                                            update_book(chosen_book.id)
                                        elif option_choice == 2:
                                            print("Let's delete the book!")
                                            delete_book(chosen_book.id, chosen_book.title)
                                    book_choice = 0
                            owner_choice = 0
                    second_choice = 0
                if second_choice == 3:
                    owner_choice = 0
                    owners = list_owners_by_fav_genre()
                    while owner_choice != len(owners) + 1:
                        for i, owner in enumerate(owners, start=1):
                            print(f"{i}. {owner.name}")
                        print("---------")
                        print(f"{(len(owners) + 1)}. Back")
                        owner_choice = int(input())
                        if owner_choice == len(owners) + 1:
                            print("Moving back")
                        else:
                            book_choice = 0
                            chosen_owner = owners[owner_choice-1]
                            list = grab_owners_books(chosen_owner.id)
                            while book_choice != (len(list) + 2):
                                print("OWNER")
                                print("---------")
                                print(f"{chosen_owner.name} || Age: {chosen_owner.age} || Favorite Genre: {chosen_owner.fav_genre}")
                                print(" ")
                                print("BOOKS: Select one to edit")
                                print("---------")
                                list_owners_books(chosen_owner.id)
                                print(" ")
                                print("Options")
                                print("---------")
                                print(f"{len(list) + 1}: Add a new book")
                                print(f"{len(list) + 2}: Back")
                                book_choice = int(input())
                                if book_choice == (len(list) + 2):
                                    print("Moving Back!")

                                elif book_choice == (len(list) + 1):
                                    print(f"Adding new book to {chosen_owner.name}")
                                    create_book(chosen_owner.id)
                                else:
                                    option_choice = 0
                                    while option_choice != 3:
                                        chosen_book = list[book_choice-1]
                                        print(" ")
                                        print("BOOK")
                                        print("---------")
                                        print(f"{chosen_book.title} || Author: {chosen_book.author} || ISBN: {chosen_book.isbn}")
                                        print("---------")
                                        print("1. Update Book")
                                        print("2. Delete Book")
                                        print("3. Back")
                                        option_choice = int(input())
                                        if option_choice == 3:
                                            print("Moving back.")
                                        elif option_choice == 1:
                                            print("Let's Update the Book!")
                                            update_book(chosen_book.id)
                                        elif option_choice == 2:
                                            print("Let's delete the book!")
                                            delete_book(chosen_book.id, chosen_book.title)
                                    book_choice = 0
                            owner_choice = 0
                    second_choice = 0
                    
        elif first_choice == 2:
            second_choice = 0
            while second_choice != 3:
                print("--Settings--")
                print("1: Modify Book Table")
                print("2: Modify Owner Table")
                print("3: Back")
                second_choice = int(input())

                if second_choice == 1:
                    third_choice = 0
                    while third_choice != 3:
                        print("---Modifying Book Table---")
                        print("1: Add Table")
                        print("2: Drop Table")
                        print("3: Back")
                        third_choice = int(input())

                        if third_choice == 1:
                            print("Creating Book Table")
                            Book.create_table()
                        elif third_choice == 2:
                            print("Dropping Book Table")
                            Book.drop_table()
                        elif third_choice == 3:
                            print("Moving Back!")
                    second_choice = 0
                if second_choice == 2:
                    owner_table_choice = 0
                    while owner_table_choice != 3:
                        print("---Modifying Owner Table---")
                        print("1: Add Table")
                        print("2: Drop Table")
                        print("3: Back")
                        owner_table_choice = int(input())

                        if owner_table_choice == 1:
                            print("Creating Owner Table")
                            Owner.create_table()
                        elif owner_table_choice == 2:
                            print("Dropping Owner Table")
                            Owner.drop_table()
                        elif owner_table_choice == 3:
                            print("Moving Back!")
                    second_choice = 0
                if second_choice == 3:
                    print("Moving Back!")
            first_choice = 0
        else:
            print("Exiting program!")
            exit()

if __name__ == "__main__":
    main()
