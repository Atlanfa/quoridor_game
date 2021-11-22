import copy

from infinity import inf
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder

from Coordinate import Coordinate
from Wall import Wall, if_there_path_to_win

import time


def timeit(func):
    """
    Декоратор для измерения времени работы функции.
    """
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("Processing time of %s(): %.4f seconds."
              % (func.__qualname__, time.time() - start_time))
        return result

    return measure_time

counter = 0

class Minimax:
    def __init__(self, game_field, player_one, player_two, action=None, depth=+inf, parrent=None):
        self.game_field = game_field
        self.player_one = player_one
        self.player_two = player_two
        self.action = action
        self.depth = depth
        self.minimax_eval = None
        self.child = []
        self.parrent = None
        self.player_one_path = None
        self.player_two_path = None



def minimax(obj_minimax, depth, alpha, beta, maximizingPlayer, player_one, player_two):
    global counter
    counter += 1
    if depth == 0:  # TODO GameOver
        path_first, path_second = get_paths_to_win(obj_minimax.game_field, player_one, player_two)  # Список путей
        path_first = min(path_first, key=len)  # Кратчайший для первого
        path_second = min(path_second, key=len)  # Кратчайший для второго
        obj_minimax.player_one_path = path_first
        obj_minimax.player_two_path = path_second
        return evaluation(obj_minimax)

    if type(obj_minimax) != Minimax:
        obj_minimax = Minimax(copy.deepcopy(obj_minimax), player_one, player_two, action=None, depth=depth)
    path_first, path_second = get_paths_to_win(obj_minimax.game_field, player_one, player_two)  # Список путей
    path_first = min(path_first, key=len)  # Кратчайший для первого
    path_second = min(path_second, key=len)  # Кратчайший для второго
    obj_minimax.player_one_path = path_first
    obj_minimax.player_two_path = path_second
    walls = get_all_walls(obj_minimax.game_field, player_one, player_two, path_second)
    for wall in walls:
        obj_minimax.child.append(Minimax(wall[0], wall[1], wall[2], wall[3], depth, obj_minimax))
    next_move_one_player = get_all_moves(obj_minimax.game_field, player_one, player_two, path_first)
    obj_minimax.child.append(
        Minimax(next_move_one_player[0][0], next_move_one_player[0][1], next_move_one_player[0][2], next_move_one_player[0][3]))

    if maximizingPlayer:
        max_eval = -inf
        for child_local in obj_minimax.child:
            eval, act = minimax(child_local, depth - 1, alpha, beta, False, player_two, player_one)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            obj_minimax.minimax_eval = alpha
            if beta <= alpha:
                break
        return max_eval, obj_minimax

    else:
        min_eval = +inf
        for child_local in obj_minimax.child:
            eval, act = minimax(child_local, depth - 1, alpha, beta, True, player_one, player_two)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            obj_minimax.minimax_eval = beta
            if beta <= alpha:
                break
        return min_eval, obj_minimax



def call_minimax(game_field, depth, alpha, beta, maximizingPlayer, player_one, player_two):
    evl, act = minimax(game_field, depth, alpha, beta, maximizingPlayer, player_one, player_two)
    global counter
    print(counter)
    counter = 0
    for kid in act.child:
        if kid.minimax_eval == evl:
            return kid.action




def evaluation(minim):
    minim.minimax_eval = len(minim.player_one_path) - len(minim.player_two_path)
    return minim.minimax_eval, minim



def get_paths_to_win(game_field, player_one, player_two):  # Путь для игрока
    grid = game_field.graph
    paths_for_first = []
    paths_for_second = []
    for win_position in player_one.for_win:
        grid.cleanup()
        start = grid.node(player_one.current_position.y, player_one.current_position.x)
        end = grid.node(win_position[1], win_position[0])

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        if len(path) >= 2:
            paths_for_first.append(path)
    for win_position in player_two.for_win:
        grid.cleanup()
        start = grid.node(player_two.current_position.y, player_two.current_position.x)
        end = grid.node(win_position[1], win_position[0])

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        if len(path) >= 2:
            paths_for_second.append(path)

    return paths_for_first, paths_for_second


def get_all_walls(game_field, player_one, player_two, path_to_win):
    game_fields = []
    if player_one.walls_amount > 0:
        walls = []
        del path_to_win[0::2]
        for wall in path_to_win:
            if wall[0] % 2 == 0:
                if wall[0] - 2 >= 0:
                    walls.append(Wall(Coordinate(wall[1], wall[0]), Coordinate(wall[1], wall[0] - 2), game_field))
                if wall[0] + 2 <= 16:
                    walls.append(Wall(Coordinate(wall[1], wall[0]), Coordinate(wall[1], wall[0] + 2), game_field))
            else:
                if wall[1] - 2 >= 0:
                    walls.append(Wall(Coordinate(wall[1], wall[0]), Coordinate(wall[1] - 2, wall[0]), game_field))
                if wall[1] + 2 <= 16:
                    walls.append(Wall(Coordinate(wall[1], wall[0]), Coordinate(wall[1] + 2, wall[0]), game_field))

        for wall in walls:
            first = if_there_path_to_win(game_field, player_one, player_two, wall) # TODO Самая времязатратная функция ~80-90% времени
            second = wall.between_two_pares
            third = wall.is_there_another_wall
            four = wall.is_length_correct
            if first and second and not third and four:
                temp_field = copy.deepcopy(game_field)
                temp_field.set_wall(wall)
                temp_player = copy.deepcopy(player_one)
                temp_player.decrease_wall_amount()
                game_fields.append((temp_field, temp_player, player_two, wall))

    return game_fields



def get_all_moves(game_field, player_one, player_two, path):
    game_fields = []
    tem_field = copy.deepcopy(game_field)
    tem_player = copy.deepcopy(player_one)
    tem_two_player = copy.deepcopy(player_two)
    player_one_moves = tem_player.set_places_to_move(game_field, [tem_player, tem_two_player])
    ind = -1
    for index, step in enumerate(tem_player.places_to_move):
        if step.x == path[2][1] and step.y == path[2][0]:
            ind = index
            break
    tem_player.set_next_position(tem_player.places_to_move[ind])
    if tem_player.can_move_here:
        tem_field.move_player(tem_player)
        game_fields.append((tem_field, tem_player, tem_two_player, tem_player.next_position))
    return game_fields
