from random import randint


def choose():
    return str(randint(1, 2))


def move(player):
    return randint(1, len(player.places_to_move))


def place_wall():
    x = randint(0, 16)
    y = 0
    x2 = 0
    y2 = 0
    if x % 2 == 1:
        y = randint(0, 16)
        while y % 2 == 1:
            y = randint(0, 16)
        x2 = x
        if y - 2 >= 2 and y + 2 <= 14:
            if randint(0, 1) == 0:
                y2 = y - 2
            else:
                y2 = y + 2
        else:
            return place_wall()
    else:
        y = randint(1, 15)
        while y % 2 == 0:
            y = randint(1, 15)
        y2 = y
        if x - 2 >= 2 and x + 2 <= 14:
            if randint(0, 1) == 0:
                x2 = x - 2
            else:
                x2 = x + 2
        else:
            return place_wall()
    return f"{x} {y} {x2} {y2}"
