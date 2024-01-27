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
        f'Book {author} not found'
    ))

def find_book_by_isbn():
    isbn = input("Enter the book's isbn: ")
    book = Book.find_by_isbn(isbn)
    print(book if book else print(
        f'Book {isbn} not found'
    ))