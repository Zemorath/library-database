from models.__init__ import CURSOR, CONN
from models.owners import Owner

class Book:

    all = {}

    def __init__(self, title, author, isbn, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, str) and len(author):
            self._author = author
        else:
            raise ValueError("Author must be a non-empty string")
        
    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, isbn):
        if isinstance(isbn, int) and (isbn > 0):
            self._isbn = isbn
        else:
            raise ValueError("ISBN must be an integer and 10 or 13 characters long")