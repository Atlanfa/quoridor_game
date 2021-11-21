from infinity import inf
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder


def minimax(game_field, depth, alpha, beta, maximizing_player, player_one, player_two):
    if depth == 0 or game_field.game_over():
        if maximizing_player:
            paths_for_first, paths_for_second = get_paths_to_win(game_field, player_one, player_two)
        else:
            paths_for_first, paths_for_second = get_paths_to_win(game_field, player_two, player_one)
        return static_evaluation_of_game_field(paths_for_first, paths_for_second)
    paths_for_first, paths_for_second = get_paths_to_win(game_field, player_one, player_two)
    if maximizing_player:
        max_evaluation = -inf
        walls = get_all_walls(game_field, player_one, paths_for_first)
        all_moves = get_all_moves(game_field)
        possible_moves = walls + all_moves
        for position in possible_moves:               # TODO
            evaluation = minimax(position, depth - 1, alpha, beta, False, player_two, player_one)
            max_evaluation = max(max_evaluation, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return max_evaluation
    else:
        min_evaluation = +inf
        walls = get_all_walls(game_field, player_two, paths_for_second)
        all_moves = get_all_moves(game_field)
        possible_moves = walls + all_moves
        for position in possible_moves:               # TODO
            evaluation = minimax(position, depth - 1, alpha, beta, True, player_one, player_two)
            min_evaluation = min(min_evaluation, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return min_evaluation


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


def get_all_walls(game_field, player, path_to_win):
    walls = [wall if wall[0] % 2 == 0 and wall[1] % 2 == 0 else path_to_win.pop(wall) for wall in path_to_win]
