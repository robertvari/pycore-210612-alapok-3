class PlayerBase:
    def __init__(self):
        self.name = None
        self.credits = 0
        self.hand = []
        self.in_game = True


class Player(PlayerBase):
    pass


class VirtualPlayer(PlayerBase):
    pass


class Deck:
    pass


class Card:
    pass