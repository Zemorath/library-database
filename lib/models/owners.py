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
        if isinstance(age, int) and (105 >= age >= 3):
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
        CURSOR.execute(sql, (self.name, self.age, self.fav_genre, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM owners
            WHERE name = ?
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        print(self)
        self.id = None
        
        # if {self.name} in all:
        #     all.pop({self.name})
        # else:
        #     print("Owner not found")

        

    @classmethod
    def instance_from_db(cls, row):
        owner = cls.all.get(row[0])
        if owner:
            owner.name = row[1]
            owner.age = row[2]
            owner.fav_genre = row[3]
        else:
            owner = cls(row[1], row[2], row[3])
            owner.id = row[0]
            cls.all[owner.id] = owner
        return owner

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM owners
        """

        rows = CURSOR.execute(sql).fetchall()
        
        return [cls.instance_from_db(row) for row in rows]
    

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM owners
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM owners
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_all_by_age(cls, age):
        sql = """
            SELECT *
            FROM owners
            WHERE age = ?
        """

        rows = CURSOR.execute(sql, (age,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def get_all_by_fav_genre(cls, fav_genre):
        sql = """
            SELECT *
            FROM owners
            WHERE fav_genre = ?
        """

        rows = CURSOR.execute(sql, (fav_genre,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    def books(self):
        from models.books import Book
        sql = """
            SELECT * FROM books
            WHERE owner_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Book.instance_from_db(row) for row in rows
        ]
    