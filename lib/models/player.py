

class Player:

    all = []

    def __init__(self, name):
        self._name = name
        Player.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 15):
            self._name = name

    