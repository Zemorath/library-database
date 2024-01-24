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
    