from random import randint
from infinity import inf
from datetime import datetime

import minimax


class Bot:
    action = None
    coordinate = None


def choose(player, game_field, list_of_players):
    # return str(randint(1, 2))
    start = datetime.now()
    print("CHOOSE")
    list_of_players.remove(player)
    bot_action = minimax.call_minimax(game_field, depth=1, alpha=-inf, beta=+inf, maximizing_player=True, player_one=player,
                         player_two=list_of_players[0])
    if type(bot_action) == Wall:
        Bot.action == 2
        Bot.coordinate = bot_action
    else:
        Bot.action = 1
        Bot.coordinate = bot_action
    print(datetime.now() - start)
    return Bot.action


def move(player):
    # return randint(1, len(player.places_to_move))
    return player.places_to_move.index(Bot.coordinate)

def place_wall():
    # x = randint(0, 16)
    # y = 0
    # x2 = 0
    # y2 = 0
    # if x % 2 == 1:
    #     y = randint(0, 16)
    #     while y % 2 == 1:
    #         y = randint(0, 16)
    #     x2 = x
    #     if y - 2 >= 2 and y + 2 <= 14:
    #         if randint(0, 1) == 0:
    #             y2 = y - 2
    #         else:
    #             y2 = y + 2
    #     else:
    #         return place_wall()
    # else:
    #     y = randint(1, 15)
    #     while y % 2 == 0:
    #         y = randint(1, 15)
    #     y2 = y
    #     if x - 2 >= 2 and x + 2 <= 14:
    #         if randint(0, 1) == 0:
    #             x2 = x - 2
    #         else:
    #             x2 = x + 2
    #     else:
    #         return place_wall()
    # return f"{x} {y} {x2} {y2}"
    return f"{Bot.coordinate.coordinates_start.x} {Bot.coordinate.coordinates_start.y} {Bot.coordinate.coordinates_end.x} {Bot.coordinate.coordinates_end.y}"
