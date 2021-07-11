import random


class PlayerBase:
    name_list = ["Brittney Moriah", "Curtis Tristin", "Lucas Troy", "Chip Gale", "Simon Lynn"]

    def __init__(self):
        self._name = None
        self._credits = 0
        self._hand = []
        self._in_game = True

    def create(self):
        self._credits = random.randint(100, 1000)
        self._name = random.choice(self.name_list)

    def draw_card(self, deck):
        new_card = deck.give_card()
        self._hand.append(new_card)

    def show_hand(self):
        print(self._hand)

    def __str__(self):
        return self._name


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
        new_card = self._cards[-1]
        self._cards.remove(new_card)

        return new_card

    @property
    def cards(self):
        return self._cards

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

    player1 = AiPlayer()
    player1.create()

    for _ in range(10):
        player1.draw_card(deck)

    print(player1._hand)