from models.__init__ import CURSOR, CONN

class Player:

    all = {}

    def __init__(self, name, player_class, id=None):
        self.id = id
        self.name = name
        self.player_class = player_class
        Player.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 15):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string and no more than 15 characters"
            )
        
    @property
    def player_class(self):
        return self._player_class
    
    @player_class.setter
    def player_class(self, player_class):
        if isinstance(player_class, str) and len(player_class):
            self._player_class = player_class
        else:
            raise ValueError(
                "player_class must be a non-empty string"
            )
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS players (
            id  INTEGER PRIMARY KEY,
            name TEXT,
            player_class TEXT
            )"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO players (name, player_class)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.player_class))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, name, player_class):
        player = cls(name, player_class)
        player.save()
        return player
    
    def update(self):
        sql = """
            UPDATE players
            SET name = ?, player_class = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.player_class, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM players
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        player = cls.all.get(row[0])
        if player:
            player.name = row[1]
            player.player_class = row[2]
        else:
            player = cls(row[1, row[2]])
            player.id = row[0]
            cls.all[player.id] = player
        return player
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM players
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM players
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def player_items(self):
        from models.player_items import Player_Items
        sql = """
            SELECT * FROM player_items
            WHERE player_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Player_Items.instance_from_db(row) for row in rows
        ]