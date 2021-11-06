from datetime import datetime

import GameField, Player, Wall, Coordinate, messages
from users_input import enter, who, play
from utils import clear_console


def startGame():
    game_field = GameField.GameField()
    playerOne = Player.Player(True, 1)
    playerTwo = Player.Player(False, 2)
    messages.with_who_you_want_to_play()
    whoIs = who()
    if whoIs == "1":
        playerOne = Player.Player(True, 1)
        playerTwo = Player.Player(True, 2)
    elif whoIs == "2":
        playerOne = Player.Player(True, 1)
        playerTwo = Player.Player(False, 2)
    elif whoIs == "3":
        playerOne = Player.Player(False, 1)
        playerTwo = Player.Player(True, 2)
    elif whoIs == "4":
        playerOne = Player.Player(False, 1)
        playerTwo = Player.Player(False, 2)
    else:
        messages.wrong_action_message("21")
        startGame()
    list_of_players = [playerOne, playerTwo]
    counter = 0
    moves = 0  # Счётчик ходов
    start = datetime.now()
    while not playerOne.isWin() and not playerTwo.isWin():
        messages.print_field(game_field.field)
        game(list_of_players[counter], game_field, list_of_players)
        game_field.graph = game_field.set_graph()
        moves += 1
        counter = 1 if counter == 0 else 0
        clear_console()
    end = datetime.now()
    # print(end - start)
    # print(moves)
    # print(playerOne.current_position.x, playerOne.current_position.y)
    # print(playerTwo.current_position.x, playerTwo.current_position.y)
    messages.win_message(playerOne if playerOne.isWin() else playerTwo, game_field.field)
    if play() == "yes" or play() == "1":
        startGame()


def setWall(player, game_field, list_of_players):
    clear_console()
    messages.print_field(game_field.field)
    if player.walls_amount > 0:
        messages.place_the_wall_message()
        wallinput = enter(player, "wall")
        if wallinput == "back":
            game(player, game_field, list_of_players)
        else:
            coordinatesSplit = wallinput.split(" ")
            if len(coordinatesSplit) == 4:
                try:
                    coordinates = [int(coordinate) for coordinate in coordinatesSplit]
                    wall = Wall.Wall(Coordinate.Coordinate(coordinates[0], coordinates[1]),
                                     Coordinate.Coordinate(coordinates[2], coordinates[3]), game_field)
                    first = wall.if_there_path_to_win(game_field, list_of_players[0], list_of_players[1], wall)
                    second = wall.between_two_pares
                    third = wall.is_there_another_wall
                    if first and second and not third:
                        game_field.set_wall(wall)
                        player.decrease_wall_amount()
                    else:
                        messages.wrong_action_message("51")
                        setWall(player, game_field, list_of_players)

                except Exception as e:
                    # print("54")
                    messages.wrong_action_message(e)
                    setWall(player, game_field, list_of_players)
            else:
                messages.wrong_action_message("56")
                setWall(player, game_field, list_of_players)
    else:
        game(player, game_field, list_of_players)


def playerMove(player, game_field, list_of_players):
    clear_console()
    messages.print_field(game_field.field)
    player.set_places_to_move(game_field, list_of_players)
    messages.print_places_to_move(player.places_to_move)
    try:
        movePlayerInput = enter(player, "move")  #
        if movePlayerInput == "back":
            game(player, game_field, list_of_players)
        elif int(movePlayerInput) in range(1, len(player.places_to_move) + 1):
            player.set_next_position(player.places_to_move[int(movePlayerInput) - 1])
            if player.can_move_here:  # Проверки на передвижение
                game_field.move_player(player)
            else:
                messages.wrong_action_message("74")
                playerMove(player, game_field, list_of_players)
    except Exception:
        messages.wrong_action_message("77")
        playerMove(player, game_field, list_of_players)


def game(player, game_field, list_of_players):
    clear_console()
    messages.print_field(game_field.field)
    messages.choose_action_message(player)
    gameinput = enter(player, "choose")
    if gameinput == "1":
        playerMove(player, game_field, list_of_players)
    elif gameinput == "2":
        setWall(player, game_field, list_of_players)
    else:
        messages.wrong_action_message("91")
        game(player, game_field, list_of_players)


if __name__ == '__main__':
    startGame()
