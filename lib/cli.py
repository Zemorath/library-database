from helper import (
        list_books,
        find_book_by_title,
        find_book_by_author,
        find_book_by_isbn,
        create_book,
        update_book,
        delete_book,
        list_owners,
        list_owners_by_age,
        list_owners_by_fav_genre,
        find_owner_by_name,
        create_owner,
        update_owner,
        delete_owner
    )
from models.owners import Owner
from models.books import Book

def main():
    first_choice = 0
    while first_choice != "x":
        print("-Online Library-")
        print("1: Interact with books")
        print("2: Interact with owners")
        print("3: Settings")
        print("4: Quit")
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
                print("6: Back")
                second_choice = int(input())
                
                if second_choice == 1:
                    third_choice = 0
                    while third_choice != 3:
                        print("---List Books---")
                        print("1: All Books")
                        print("2: By Author")
                        print("3: Back")
                        third_choice = int(input())

                        if third_choice == 1:
                            list_books()
                        elif third_choice == 2:
                            find_book_by_author()
                        elif third_choice == 3:
                            print("Moving Back!")
                    second_choice = 0
                elif second_choice == 2:
                    third_choice = 0
                    while third_choice != 4:
                        print("---Find a Book---")
                        print("1: By Title")
                        print("2: By Author")
                        print("3: By ISBN")
                        print("4: Back")
                        third_choice = int(input())

                        if third_choice == 1:
                            find_book_by_title()
                        elif third_choice == 2:
                            find_book_by_author()
                        elif third_choice == 3:
                            find_book_by_isbn()
                        elif third_choice == 4:
                            print("Moving Back!")
                    second_choice = 0
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
                    print("Moving Back!")
            first_choice = 0
        if first_choice == 2:
            second_choice = 0
            while second_choice != 6:
                print("--Owners--")
                print("1: List Owners")
                print("2: Find a specific owner")
                print("3: Add a new owner")
                print("4: Update an existing owner")
                print("5: Delete a owner")
                print("6: Back")
                second_choice = int(input())
                
                if second_choice == 1:
                    third_choice = 0
                    while third_choice != 4:
                        print("---List Owners---")
                        print("1: All Owners")
                        print("2: By Age")
                        print("3: By Favorite Genre")
                        print("4: Back")
                        third_choice = int(input())

                        if third_choice == 1:
                            print("Listing all owners")
                            list_owners()
                        elif third_choice == 2:
                            print("Listing owners by age")
                            list_owners_by_age()
                        elif third_choice == 3:
                            print("Listing owners by favorite genre")
                            list_owners_by_fav_genre()
                        elif third_choice == 4:
                            print("Moving Back")
                    second_choice = 0
                elif second_choice == 2:
                    print("---Finding Owner by Name---")
                    find_owner_by_name()
                elif second_choice == 3:
                    print("---Creating New owner---")
                    create_owner()
                elif second_choice == 4:
                    print("---Updating Existing owner---")
                    update_owner()
                elif second_choice == 5:
                    print("---Deleting owner---")
                    delete_owner()
                elif second_choice == 6:
                    print("Moving Back!")
            first_choice = 0
        if first_choice == 3:
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
        if first_choice == 4:
            print("Exiting Program!")
            exit()

if __name__ == "__main__":
    main()
