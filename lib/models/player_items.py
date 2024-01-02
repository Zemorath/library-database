
from models.__init__ import CURSOR, CONN
from models.player import Player
from models.item import Item

class Player_Items:

    all = {}

    def __init__(self, player_id, item_id, id=None):
        self.id = id
        self.player_id = player_id
        self.item_id = item_id
        Player_Items.all.append(self)

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, player_id):
        if type(player_id) is int and Player.find_by_id(player_id):
            self._player_id = player_id
        else:
            raise ValueError(
                "player_id must reference a player in the database"
            )
    
    @property
    def item_id(self):
        return self._item_id
    
    @item_id.setter
    def item_id(self, item_id):
        if type(item_id) is int and Item.find_by_id(item_id):
            self._item_id = item_id
        else:
            raise ValueError(
                "item_id must reference an item in the database"
            )
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS player_items (
            id INTEGER PRIMARY KEY,
            player_id INTEGER,
            item_id INTEGER,
            FOREIGN KEY (player_id) REFERENCES players(id)
            )"""
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS player_items
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO player_items (player_id, item_id)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.player_id, self.item_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        sql = """
            UPDATE player_items
            SET player_id = ?, item_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.player_id, self.item_id, self.id))

        CONN.commit()
    
    def delete(self):
        sql = """
            DELTE FROM player_item
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id))
        CONN.commit()