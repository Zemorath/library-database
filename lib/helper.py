from models.books import Book
from models.owners import Owner


def exit_program():
    print("See ya!")
    exit()

# Book model helper methods

def list_books():
    books = Book.get_all()
    for book in books:
        print(book)

def find_book_by_title():
    title = input("Enter the book's name: ")
    book = Book.find_by_title(title)
    print(book if book else print(
        f'Book {title} not found'
    ))

def find_book_by_author():
    author = input("Enter the book's author: ")
    book = Book.find_by_author(author)
    print(book if book else print(
        f'Author {author} not found'
    ))

def find_book_by_isbn():
    isbn = input("Enter the book's isbn: ")
    book = Book.find_by_isbn(isbn)
    print(book if book else print(
        f'ISBN {isbn} not found'
    ))

def create_book():
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    isbn = input("Enter the book's ISBN: ")
    owner_id = input("Enter the owner's ID: ")
    try:
        book = Book.create(title, author, int(isbn), int(owner_id))
        print(f'Succes: {book}')
    except Exception as exc:
        print("Error creating book: ", exc)

def update_book():
    title = input("Enter the book's title: ")
    if book := Book.find_by_title(title):
        try:
            title = input("Enter the new title: ")
            book.title = title

            author = input("Enter the new author: ")
            book.author = author

            isbn = input("Enter the new ISBN: ")
            book.isbn = isbn

            book.update()
            print(f'Success: {book}')
        except Exception as exc:
            print("Error updating book: ", exc)
    else:
        print(f'Book {title} not found')

def delete_book():
    title = input("Enter the book's title: ")
    if book := Book.find_by_title(title):
        book.delete()
        print(f'Book {title} deleted')
    else:
        print(f'Book {title} not found')


# Owner model helper methods
    
def list_owners():
    owners = Owner.get_all()
    for owner in owners:
        print(owner)

def find_owner_by_name():
    name = input("Enter the owner's name: ")
    owner = Owner.find_by_name(name)
    print(owner) if owner else print(f'Owner {name} not found')

def list_owners_by_age():
    age = input("Enter the age to filter by: ")
    owners = Owner.get_all_by_age(age)
    for owner in owners:
        print(owner)

def list_owners_by_fav_genre():
    fav_genre = input("Enter the genre to filter by: ")
    owners = Owner.get_all_by_fav_genre(fav_genre)
    for owner in owners:
        print(owner)

def create_owner():
    name = input("Enter the owner's name: ")
    age = input("Enter the owner's age: ")
    fav_genre = input("Enter the owner's favorite genre: ")
    try:
        owner = Owner.create(name, int(age), fav_genre)
        print(f"Success: {owner}")
    except Exception as exc:
        print("Error create Owner: ", exc)

def update_owner():
    name = input("Enter the owner's name: ")
    if owner := Owner.find_by_name(name):
        try:
            name = input("Enter the new name: ")
            owner.name = name

            age = input("Enter the owner's age: ")
            owner.age = age

            fav_genre = input("Enter the owner's favorite genre: ")
            owner.fav_genre = fav_genre

            owner.update()
            print(f'Success: {owner}')
        except Exception as exc:
            print("Error updating owner: ", exc)
    else:
        print(f"Owner {name} not found")

def delete_owner():
    name = input("Enter the owner's name: ")
    if owner := Owner.find_by_name(name):
        owner.delete()
        print(f'Owner {name} has been deleted')
    else:
        print(f'Owner {name} not found')