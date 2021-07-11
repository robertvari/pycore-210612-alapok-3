import random


class PlayerBase:
    def __init__(self):
        self._name = None
        self._credits = 0
        self._hand = []
        self._in_game = True

    def create(self):
        self._credits = random.randint(100, 1000)


class HumanPlayer(PlayerBase):
    pass


class AiPlayer(PlayerBase):
    pass


class Deck:
    def __init__(self):
        self._cards = []

    def create(self):
        self._cards.clear()

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        names = ["Heart", "Club", "Diamond", "Spade"]

        for name in names:
            for card in cards:
                card_name = f"{name} {card[0]}"
                value = card[1]

                new_card = Card(card_name, value)

                self._cards.append(new_card)

        random.shuffle(self._cards)

    def give_card(self):
        pass

    def show(self):
        print(self._cards)


class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}"


if __name__ == '__main__':
    deck = Deck()
    deck.create()

    player = AiPlayer()
    player.create()