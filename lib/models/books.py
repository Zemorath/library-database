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
        if isinstance(isbn, int) and (13 >= isbn > 0):
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
    
    def save(self):
        sql = """
            INSERT INTO books (title, author, isbn, owner_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.author, self.isbn, self.owner_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        sql = """
            UPDATE books
            SET title = ?, author = ?, isbn = ?, owner_id = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.title, self.author, self.isbn, self.owner_id, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM books
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, title, author, isbn, owner_id):
        book = cls(title, author, isbn, owner_id)
        book.save()
        return book
    
    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])
        if book:
            book.title = row[1]
            book.author = row[2]
            book.isbn = row[3]
            book.owner_id = row[4]
        else:
            book = cls(row[1], row[2], row[3], row[4])
            book.id = row[0]
            cls.all[book.id] = book
        return book
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM books
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT *
            FROM books
            WHERE title is ?
        """

        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_author(cls, author):
        sql = """
            SELECT *
            FROM books
            WHERE author is ?
        """

        rows = CURSOR.execute(sql, (author,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_isbn(cls, isbn):
        sql = """
            SELECT *
            FROM books
            WHERE isbn is ?
        """

        row = CURSOR.execute(sql, (isbn,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_owner_id(cls, owner_id):
        sql = """
            SELECT *
            FROM books
            WHERE owner_id is ?
        """

        rows = CURSOR.execute(sql, (owner_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]