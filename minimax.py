import copy

from infinity import inf
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder

from Coordinate import Coordinate
from Wall import Wall, if_there_path_to_win


class Minimax:
    def __init__(self, game_field, player_one, player_two, action):
        self.game_field = game_field
        self.player_one = player_one
        self.player_two = player_two
        self.action = action
        self.depth = -1
        self.minimax_eval = -inf

def call_minimax(game_field, depth, alpha, beta, maximizing_player, player_one, player_two):
    moves = []
    eval, moves = minimax(game_field, depth, alpha, beta, maximizing_player, player_one, player_two, moves)
    # TODO

def minimax(game_field, depth, alpha, beta, maximizing_player, player_one, player_two, moves):
    if depth == 0 or game_field.game_over():
        if maximizing_player:
            paths_for_first, paths_for_second = get_paths_to_win(game_field, player_one, player_two)
        else:
            paths_for_first, paths_for_second = get_paths_to_win(game_field, player_two, player_one)
        return static_evaluation_of_game_field(paths_for_first, paths_for_second)
    paths_for_first, paths_for_second = get_paths_to_win(game_field, player_one, player_two)
    if maximizing_player:
        max_evaluation = -inf
        walls = get_all_walls(game_field, player_one, paths_for_first, paths_for_first)
        all_moves = get_all_moves(game_field, player_one, player_two)
        possible_moves = walls + all_moves
        for move in possible_moves:
            moves.append(Minimax(move[0], move[1], move[2], move[3]))
        for position in possible_moves:
            position.depth = depth - 1
            evaluation = minimax(position.game_field, depth - 1, alpha, beta, False, position.player_two, position.player_one, moves)
            max_evaluation = max(max_evaluation, evaluation)
            alpha = max(alpha, evaluation)
            position.minimax_eval = min_evaluation
            if beta <= alpha:
                break
        return max_evaluation, moves
    else:
        min_evaluation = +inf
        walls = get_all_walls(game_field, player_two, paths_for_second, paths_for_second)
        all_moves = get_all_moves(game_field, player_two, player_one)
        possible_moves = walls + all_moves
        for move in possible_moves:
            moves.append(Minimax(move[0], move[1], move[2], move[3]))
        for position in moves:
            position.depth = depth - 1
            evaluation = minimax(position.game_field, depth - 1, alpha, beta, True, position.player_one, position.player_two, moves)
            min_evaluation = min(min_evaluation, evaluation)
            beta = min(beta, evaluation)
            position.minimax_eval = min_evaluation
            if beta <= alpha:
                break
        return min_evaluation, moves


def get_paths_to_win(game_field, player_one, player_two):
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

def static_evaluation_of_game_field(paths_for_first, paths_for_second):
    evaluations_for_first = [len(path) for path in paths_for_first]
    evaluations_for_second = [len(path) for path in paths_for_second]
    min_first = min(evaluations_for_first)
    min_second = min(evaluations_for_second)
    evaluation = min_first - min_second

    return evaluation


def get_all_walls(game_field, player_one, player_two, path_to_win):
    game_fields = []
    if player_one.walls_amount > 0:
        walls = []
        del path_to_win[0::2]
        for wall in path_to_win:
            if wall[0] % 2 == 0:
                walls.append(Wall(Coordinate(wall[1], wall[0]), Coordinate(wall[1], wall[0] - 2), game_field))
                walls.append(Wall(Coordinate(wall[1], wall[0]), Coordinate(wall[1], wall[0] + 2), game_field))
            else:
                walls.append(Wall(Coordinate(wall[1], wall[0]), Coordinate(wall[1] - 2, wall[0]), game_field))
                walls.append(Wall(Coordinate(wall[1], wall[0]), Coordinate(wall[1] + 2, wall[0]), game_field))
        for wall in walls:
            first = if_there_path_to_win(game_field, player_one, player_two, wall)
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


def get_all_moves(game_field, player_one, player_two):
    game_fields = []
    player_one_moves = player_one.set_places_to_move(game_field, [player_one, player_two])
    for move in player_one_moves:
        tem_field = copy.deepcopy(game_field)
        tem_player = copy.deepcopy(player_one)
        tem_player.set_next_position(move)
        if tem_player.can_move_here:
            tem_field.move_player(tem_player)
            game_fields.append((tem_field, tem_player, player_two, tem_player.next_position))
    return game_fields

