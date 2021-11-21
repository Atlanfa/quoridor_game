from random import randint
from infinity import inf
from datetime import datetime
from Wall import Wall

import minimax


class Bot:
    def __init__(self, act, coord):
        self.action = act
        self.coordinate = coord


bot_action = Bot(None, None)

def choose(player, game_field, list_of_players):
    # return str(randint(1, 2))
    start = datetime.now()
    print("CHOOSE")
    player_two = list_of_players[1] if list_of_players[0].player_number == player.player_number else list_of_players[0]
    bot_doing = minimax.call_minimax(game_field, depth=1, alpha=-inf, beta=+inf, maximizing_player=True, player_one=player,
                         player_two=player_two)
    if type(bot_doing) == Wall:
        bot_action.action = "2"
        bot_action.coordinate = bot_doing
    else:
        bot_action.action = "1"
        bot_action.coordinate = bot_doing
    print(datetime.now() - start)
    return bot_action.action


def move(player):
    # return randint(1, len(player.places_to_move))
    for index, step in enumerate(player.places_to_move):
        if step.x == bot_action.coordinate.x and step.y == bot_action.coordinate.y:
            return index

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
    return f"{bot_action.coordinate.coordinates_start.x} {bot_action.coordinate.coordinates_start.y} {bot_action.coordinate.coordinates_end.x} {bot_action.coordinate.coordinates_end.y}"
