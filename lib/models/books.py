from models.__init__ import CURSOR, CONN
from models.owners import Owner

class Book:

    all = {}

    def __init__(self, title, author, isbn, owner_id, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.owner_id = owner_id

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
    
    @property
    def owner_id(self):
        return self._owner_id
    
    @owner_id.setter
    def owner_id(self, owner_id):
        if type(owner_id) is int and Owner.find_by_id(owner_id):
            self._owner_id = owner_id
        else:
            raise ValueError("owner_id must reference an owner in the database")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            isbn INTEGER,
            owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES owners(id)
        )"""

        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books
        """
        CURSOR.execute(sql)
        CONN.commit()