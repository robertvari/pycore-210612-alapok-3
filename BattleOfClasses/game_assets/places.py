class PlaceBase:
    def __init__(self):
        self._player = None

    def create(self):
        return self

    def enter(self, player):
        self._player = player


class Tavern(PlaceBase):
    pass


class Arena(PlaceBase):
    pass


class Village(PlaceBase):
    pass