from game_assets.assets import Deck, AiPlayer, HumanPlayer


class Blackjack:
    def __init__(self):
        self._intro()
        self._deck = Deck()
        self._deck.create()

        self._players = []

        # create AI players
        self._create_AI_players()

        # create Human player
        human_player = HumanPlayer()
        human_player.create()
        self._players.append(human_player)

        self._start()

    def _create_AI_players(self):
        for _ in range(3):
            new_AI_player = AiPlayer()
            new_AI_player.create()
            self._players.append(new_AI_player)

    def _intro(self):
        print("="*50, "BLACKJACK", "="*50)

    def _start(self):
        for player in self._players:
            player.draw_card(self._deck)


if __name__ == '__main__':
    Blackjack()