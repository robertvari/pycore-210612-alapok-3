import random
from game_assets.utilities import get_fantasy_name


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

    def create(self):
        self._name = get_fantasy_name()

        self._race = random.choice(list(self.races))
        self._strength = self.races[self._race]["strength"]
        self._max_HP = self.races[self._race]["max_HP"]
        self._current_HP = self._max_HP

        return self

    def report(self):
        print(f"Name: {self._name}")
        print(f"Race: {self._race}")
        print(f"Strength: {self._strength}")
        print(f"Current HP: {self._current_HP}")

    def set_current_HP(self, value):
        self._current_HP -= value

    def attack(self, other):
        print(f"{self._name} attacks {other}")
        attack_strength = random.randint(0, self._strength)

        if attack_strength == 0:
            print(f"{self._name} misses...")
        else:
            print(f"{self._name} hits {other} with {attack_strength}")
            other.set_current_HP(attack_strength)

    def is_alive(self):
        return self._current_HP > 0

    def __repr__(self):
        return self._name


class Player(CharacterBase):
    def create(self):
        super(Player, self).create()
        self._name = "Robert"
        return self


class Enemy(CharacterBase):
    pass


class NPC(CharacterBase):
    pass


if __name__ == '__main__':
    enemy = Enemy().create()
    enemy.report()

    npc = NPC().create()
    npc.report()