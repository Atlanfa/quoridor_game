from Coordinate import Coordinate
from GameField import backwards_calculating_point
from Player import Player
from Wall import Wall
from bot import *


def enter(player, types, game_field = None, list_of_players = None):
    if types == "wall":
        if player.player_type:
            return player.action[1]
        elif not player.player_type:
            return place_wall()
            pass
    elif types == "move":
        if player.player_type:
            return player.action[1]
        elif not player.player_type:
            return move(player)
            pass
    elif types == "choose":
        if player.player_type:
            player.action = get_action_from_opponent()
            return player.action[0]
        elif not player.player_type:
            return choose(player, game_field, list_of_players)
            pass
    elif types == "playAgain":
        if player.player_type:
            return "1"
            # return input()


def get_action_from_opponent():
    temp = input().split(" ")
    return to_our_coordinates(temp)


def to_our_coordinates(temp):
    if temp[0] == "move" or temp[0] == "jump":
        temp[0] = "1"
        temp[1] = Coordinate(backwards_calculating_point(int(temp[1][1])), backwards_calculating_point(ord(temp[1][0].lower()) - 96))
    elif temp[0] == "wall":
        temp[0] = '2'
        if temp[1][2] == 'h':
            x = ((ord(temp[1][0].lower()) - 96 - 18) * 2) - 1
            y = ((int(temp[1][1])) * 2) - 1
            temp[1] = f"{y} {x - 1} {y} {x + 1}"
        else:
            x = ((ord(temp[1][0].lower()) - 96 - 18) * 2) - 1
            y = ((int(temp[1][1])) * 2) - 1
            temp[1] = f"{y - 1} {x} {y + 1} {x}"
    return temp


def who(text = None):
    state = input()
    if text is None:
        return "2" if state == "Black" or state == "black" else "3"
    else:
        return text


def play():
    return "1"
    # return input()


# player = Player(True, 1)

# print(enter(player, "choose"))
# print(enter(player, "wall"))
