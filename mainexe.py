import sys
from datetime import datetime

from Coordinate import Coordinate
from GameField import GameField
from Player import Player
from Wall import Wall, if_there_path_to_win
from messages import with_who_you_want_to_play, wrong_action_message, print_field, place_the_wall_message, send_wall, \
    print_places_to_move, send_jump, send_move, choose_action_message
from users_input import enter, who, play
from utils import clear_console


def start_game():
    game_field = GameField()
    player_one = Player(True, 1)
    player_two = Player(False, 2)
    # with_who_you_want_to_play()
    who_is = who()
    if who_is == "1":
        player_one = Player(True, 2)
        player_two = Player(True, 1)
    elif who_is == "2":
        player_one = Player(True, 1)
        player_two = Player(False, 2)
    elif who_is == "3":
        player_one = Player(False, 1)
        player_two = Player(True, 2)
    elif who_is == "4":
        player_one = Player(False, 1)
        player_two = Player(False, 2)
    else:
        # wrong_action_message("21")
        start_game()
    list_of_players = [player_one, player_two]
    counter = 0
    moves = 0  # Счётчик ходов
    while not player_one.is_win() or not player_two.is_win():
        # print_field(game_field.field)
        # start = datetime.now()
        game(list_of_players[counter], game_field, list_of_players)
        if player_one.is_win() or player_two.is_win():
            break
        # end = datetime.now()
        # print(end - start)
        game_field.graph = game_field.set_graph()
        moves += 1
        counter = 1 if counter == 0 else 0
        # clear_console()
    sys.exit()
    # print(moves)
    # print(player_one.current_position.x, player_one.current_position.y)
    # print(player_two.current_position.x, player_two.current_position.y)
    # win_message(player_one if player_one.isWin() else player_two, game_field.field)
    # startGame()


def set_wall(player, game_field, list_of_players, counter=0):
    # clear_console()
    # print_field(game_field.field)
    if counter < 5:
        if player.walls_amount > 0:
            # place_the_wall_message()
            wall_input = enter(player, "wall")
            if wall_input == "back":
                game(player, game_field, list_of_players)
            else:
                coordinates_split = wall_input.split(" ")
                if len(coordinates_split) == 4:
                    try:
                        coordinates = [int(coordinate) for coordinate in coordinates_split]
                        wall = Wall(Coordinate(coordinates[0], coordinates[1]),
                                    Coordinate(coordinates[2], coordinates[3]), game_field)
                        first = if_there_path_to_win(game_field, list_of_players[0], list_of_players[1], wall)
                        second = wall.between_two_pares
                        third = wall.is_there_another_wall
                        if first and second and not third:
                            game_field.set_wall(wall)
                            player.decrease_wall_amount()
                            if player.player_type is False:
                                send_wall(wall)
                        else:
                            # messages.wrong_action_message("51")
                            set_wall(player, game_field, list_of_players, counter + 1)
                    except Exception as e:
                        # print("54")
                        # messages.wrong_action_message(e)
                        set_wall(player, game_field, list_of_players, counter + 1)
                else:
                    # messages.wrong_action_message("56")
                    set_wall(player, game_field, list_of_players, counter + 1)
        else:
            game(player, game_field, list_of_players)
    else:
        print(counter)
        sys.exit()


def player_move(player, game_field, list_of_players):
    # clear_console()
    # print_field(game_field.field)
    player.set_places_to_move(game_field, list_of_players)
    # print_places_to_move(player.places_to_move)
    try:
        move_player_input = enter(player, "move")  #
        if player.action is not None:
            move_player_input = move_player_input.is_in(player.places_to_move)
        if move_player_input == "back":
            game(player, game_field, list_of_players)
        # elif int(move_player_input) in range(1, len(player.places_to_move) + 1):
        player.set_next_position(player.places_to_move[int(move_player_input) - 1])
        if player.can_move_here:  # Проверки на передвижение
            game_field.move_player(player)
            if player.is_jump and player.player_type is False and player.current_position.is_in(
                    player.jump_list) is not None:
                send_jump(player)
            elif player.player_type is False:
                send_move(player)
            player.is_jump = False
            player.jump_list = None
            player.action = None
        else:
            # wrong_action_message("74")
            player_move(player, game_field, list_of_players)
    except Exception as e:
        # wrong_action_message(e)
        # playerMove(player, game_field, list_of_players)
        pass


def game(player, game_field, list_of_players):
    # clear_console()
    # print_field(game_field.field)
    # choose_action_message(player)
    game_input = enter(player, "choose", game_field, list_of_players)
    if game_input == "1":
        player_move(player, game_field, list_of_players)
    elif game_input == "2":
        set_wall(player, game_field, list_of_players)
    else:
        # wrong_action_message("91")
        game(player, game_field, list_of_players)


if __name__ == '__main__':
    start_game()
