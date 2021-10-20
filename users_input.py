from bot import *


def enter(player, types):
    if types == "wall":
        if player.player_type:
            return input()
        elif not player.player_type:
            return placeWall()
            pass
    elif types == "move":
        if player.player_type:
            return input()
        elif not player.player_type:
            return move(player)
            pass
    elif types == "choose":
        if player.player_type:
            return input()
        elif not player.player_type:
            return choose()
            pass
    elif types == "playAgain":
        if player.player_type:
            return input()


def who():
    return input()


def play():
    return input()
