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
        # check hand value
            # if hand value < 16 draw new card
            # elif hand value >= 21 pass

        while self._in_game:
            hand_value = self.count_hand()
            if hand_value > 16:
                self._in_game = False
                print(f"{self._name} passes...")
            else:
                new_card = deck.give_card()
                self._hand.append(new_card)

    def count_hand(self):
        return sum([card.value for card in self._hand])

    def show_hand(self):
        print(self._hand)

    def __repr__(self):
        return self._name


class HumanPlayer(PlayerBase):
    def create(self):
        # todo replace this with an input()
        self._name = "Robert Vari"
        self._credits = random.randint(100, 1000)

    def draw_card(self, deck):
        print("This is your turn.")

        while self._in_game:
            hand_value = self.count_hand()
            print(f"Your hand value: {hand_value}")
            print(f"Your cards: {self._hand}")

            if hand_value > 21:
                self._in_game = False
                print(f"Your hand value is to much: {hand_value}")
                break

            result = input("Do you want to draw a new card? (y/n)")
            if result == "y":
                new_card = deck.give_card()
                print(f"The new card is: {new_card}")
                self._hand.append(new_card)
            else:
                print("You passed.")
                self.in_game = False


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

    player1 = HumanPlayer()
    player1.create()

    player1.draw_card(deck)

    player1.show_hand()