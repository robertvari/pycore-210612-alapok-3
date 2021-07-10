class Cup:
    # static attributes
    color = "Black"
    empty = True


black_cup = Cup()

red_cup = Cup()
red_cup.color = "Red"

blue_cup = Cup()
blue_cup.color = "Blue"
blue_cup.empty = False


print(black_cup.color)
print(black_cup.empty)

print(red_cup.color)
print(red_cup.empty)

print(blue_cup.color)
print(blue_cup.empty)