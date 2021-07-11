from game_assets.assets import Deck, AiPlayer, HumanPlayer


class Blackjack:
    def __init__(self):
        self._intro()
        self._deck = Deck()
        self._deck.create()

        self._bet = 0

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
        # players draw cards
        for player in self._players:
            print(f"{player} draws cards.")

            self._bet += player.give_bet(10)
            player.draw_card(self._deck)

        self._get_winner()

    def _get_winner(self):
        player_list = [p for p in self._players if p.count_hand() <= 21]

        if player_list:
            winner_list = sorted(player_list, key=lambda p: p.count_hand())

            winner = winner_list[-1]
            print(f"The winner: {winner} who wins {self._bet} credits.")
            winner.set_credits(self._bet)
        else:
            print("Nobody wins this time. :(")


if __name__ == '__main__':
    Blackjack()