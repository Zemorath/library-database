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
    