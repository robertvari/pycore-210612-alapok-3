class PlayerBase:
    def __init__(self):
        self.name = None
        self.credits = 0
        self.hand = []
        self.in_game = True


class HumanPlayer(PlayerBase):
    pass


class AiPlayer(PlayerBase):
    pass


class Deck:
    pass


class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Name: {self.name} Value: {self.value}"


if __name__ == '__main__':
    card1 = Card("Heart 2", 2)
    card2 = Card("Heart 3", 3)
    card3 = Card("Heart 4", 4)
    hand = [card1, card2, card1]
    print(hand)