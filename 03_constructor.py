class Cup:
    color = None
    empty = True

    def __init__(self, color, empty):
        self.color = color
        self.empty = empty


black_cup = Cup("Black", True)
red_cup = Cup("Red", False)
blue_cup = Cup("Blue", False)

print(black_cup.color)
print(red_cup.color)
print(blue_cup.color)