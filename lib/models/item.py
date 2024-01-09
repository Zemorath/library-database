from models.__init__ import CURSOR, CONN

class Item:

    all = []

    def __init__(self, name, health, defense, attack, crit_dmg, crit_chance, speed, id = None):
        self.id = id
        self._name = name
        self._health = health
        self._defense = defense
        self._attack = attack
        self._crit_dmg = crit_dmg
        self._crit_chance = crit_chance
        self._speed = speed
        Item.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if(type(name) == str) and (len(name) >= 3):
            if self._name == name:
                self.name = name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, health):
        if (type(health) == int) and (0 < health <= 200):
            if self._health == health:
                self.health = health
    
    @property
    def defense(self):
        return self._defense
    
    @defense.setter
    def defense(self, defense):
        if (type(defense) == int) and (0 < defense <= 200):
            if self._defense == defense:
                self.defense = defense

    @property
    def attack(self):
        return self._attack
    
    @attack.setter
    def attack(self, attack):
        if (type(attack) == int) and (0 < attack <= 300):
            if self._attack == attack:
                self.attack = attack

    @property
    def crit_dmg(self):
        return self._crit_dmg
    
    @crit_dmg.setter
    def crit_dmg(self, crit_dmg):
        if (type(crit_dmg) == int) and (0 < crit_dmg <= 30):
            if self._crit_dmg == crit_dmg:
                self.crit_dmg = crit_dmg
    
    @property
    def crit_chance(self):
        return self._crit_chance
    
    @crit_chance.setter
    def crit_chance(self, crit_chance):
        if (type(crit_chance) == int) and (0 < crit_chance <= 20):
            if self._crit_chance == crit_chance:
                self.crit_chance = crit_chance
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, speed):
        if (type(speed) == int) and (0 < speed <= 150):
            if self._speed == speed:
                self.speed = speed

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT,
            health INTEGER,
            defense INTEGER,
            attack INTEGER,
            crit_dmg INTEGER,
            crit_chance INTEGER,
            speed INTEGER
            )"""
        
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS items;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO items (name, health, defense, attack, crit_dmg, crit_chance, speed)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.health, self.defense, self.attack, self.crit_dmg, self.crit_chance, self.speed))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, health, defense, attack, crit_dmg, crit_chance, speed):
        item = cls(name, health, defense, attack, crit_dmg, crit_chance, speed)
        item.save()
        return item
    
    def update(self):
        sql = """
            UPDATE items
            SET name = ?, health = ?, defense = ?, attack = ?, crit_dmg = ?, crit_chance = ?, speed = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.health, self.defense, self.attack, self.crit_dmg, self.crit_chance, self.speed, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM items
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        item = cls.all.get(row[0])
        if item:
            item.name = row[1]
            item.health = row[2]
            item.defense = row[3]
            item.attack = row[4]
            item.crit_dmg = row[5]
            item.crit_chance = row[6]
            item.speed = row[7]
        else:
            item = cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            item.id = row[0]
            cls.all[item.id] = item
        return item
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM items
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM items
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM items
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    def player_items(self):
        from models.player_items import Player_Items
        sql = """
            SELECT * FROM player_items
            WHERE item_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()

        return [
            Player_Items.instance_from_db(row) for row in rows
        ]