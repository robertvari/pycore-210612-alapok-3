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

    def create(self):
        FIRST = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
                 'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
                 'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
                 'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam', 'She', 'Sheel',
                 'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

        SECOND = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
                  'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
                  'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
                  'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
                  'wain', 'wan', 'win', 'wise', 'ya']

        self._name = f"{random.choice(FIRST)}{random.choice(SECOND)}"

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

    def __repr__(self):
        return self._name


class Player(CharacterBase):
    pass


class Enemy(CharacterBase):
    pass


class NPC(CharacterBase):
    pass


if __name__ == '__main__':
    enemy = Enemy().create()
    enemy.report()

    npc = NPC().create()
    npc.report()