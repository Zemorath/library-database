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

    