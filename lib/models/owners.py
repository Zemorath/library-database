from models.__init__ import CURSOR, CONN
class Owner:

    all = {}

    def __init__(self, name, age, fav_genre, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.fav_genre = fav_genre

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and (age >= 3):
            self._age = age
        else:
            raise ValueError("Age must be an integer and greater than or equal to 3")
    
    @property
    def fav_genre(self):
        return self._fav_genre
    
    @fav_genre.setter
    def fav_genre(self, fav_genre):
        if isinstance(fav_genre, str) and len(fav_genre):
            self._fav_genre = fav_genre
        else:
            raise ValueError("Favorite genre must be a non-empty string")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            fav_genre TEXT
            )"""
        
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS owners;"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO owners (name, age, fav_genre)
            VALUEs (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age, self.fav_genre))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, age, fav_genre):
        owner = cls(name, age, fav_genre)
        owner.save()
        return owner
    
    def update(self):
        sql = """
            UPDATE owners
            SET name = ?, age = ?, fav_genre = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age, self.fav_genre))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM owners
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None