import random

class CharacterBase:
    races = {
        "human": {"strength": 50, "max_HP": 100},
        "ork": {"strength": 130, "max_HP": 200},
        "elf": {"strength": 60, "max_HP": 100},
        "dwarf": {"strength": 120, "max_HP": 230},
    }

    def __init__(self):
        self._name = None
        self._race = None
        self._inventory = []
        self._golds = random.randint(0, 100)

        # combat attributes
        self._strength = 0
        self._max_HP = 0
        self._current_HP = 0


class Player(CharacterBase):
    pass


class Enemy(CharacterBase):
    pass


class NPC(CharacterBase):
    pass


if __name__ == '__main__':
    print(CharacterBase.races["name"])