import random

from game_assets.utilities import get_fantasy_name


class ItemBase:
    def __init__(self):
        self._name = None
        self._price = 0
        self._weight = 0

    def create(self):
        self._name = get_fantasy_name()
        self._price = random.randint(1, 100)
        self._weight = random.randint(1, 100)
        return self

    def report(self):
        print(f"Name: {self._name}")
        print(f"Price: {self._price}")
        print(f"Weight: {self._weight}")


class Common(ItemBase):
    def create(self):
        super().create()
        self._price = random.randint(1, 10)
        return self


class Weapon(ItemBase):
    def create(self):
        super().create()
        self._price = random.randint(100, 10000)
        return self


class Magic(ItemBase):
    def create(self):
        super().create()
        self._price = random.randint(500, 10000)
        return self


class Food(ItemBase):
    def create(self):
        super().create()
        self._weight = random.randint(1, 10)
        self._price = random.randint(1, 10)

        return self


if __name__ == '__main__':
    common_item = Common().create()
    common_item.report()

    weapon_item = Weapon().create()
    weapon_item.report()

    magic_item = Magic().create()
    magic_item.report()