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


class Village(PlaceBase):
    pass


if __name__ == '__main__':
    arena = Arena().create()
    player = characters.Player().create()
    player.report()

    arena.enter(player)