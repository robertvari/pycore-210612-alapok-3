import random, time

from game_assets import characters


class PlaceBase:
    def __init__(self):
        self._player = None

    def create(self):
        print("A Place is born")
        return self

    def enter(self, player):
        print(f"{player} enters PlaceBase")
        self._player = player


class Tavern(PlaceBase):
    pass


class Arena(PlaceBase):
    def __init__(self):
        self._enemies = []

    def create(self):
        print("The Arena is born")

        for _ in range(10):
            enemy = characters.Enemy().create()
            self._enemies.append(enemy)

        return self

    def enter(self, player):
        self._player = player
        current_enemy = random.choice(self._enemies)

        print(f"{self._player} enters the Arena!")

        while True:
            # enemy attacks first
            current_enemy.attack(self._player)

            if not self._player.is_alive():
                print(f"{self._player} is dead...")
                break

            time.sleep(2)

            self._player.attack(current_enemy)

            if not current_enemy.is_alive():
                print(f"{current_enemy} is dead...")
                break

            time.sleep(2)


class Village(PlaceBase):
    def enter(self, player):
        self._player = player
        print(f"Welcome {player} in out friendly village.")


if __name__ == '__main__':
    arena = Arena().create()
    village = Village().create()

    player = characters.Player().create()
    arena.enter(player)