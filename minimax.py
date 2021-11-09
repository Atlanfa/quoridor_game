from infinity import inf
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.finder.a_star import AStarFinder


def minimax(game_field, depth, alpha, beta, maximizing_player, player_one, player_two):
    if depth == 0 or game_field.game_over():
        return static_evaluation_of_game_field(game_field, player_one, player_two) if maximizing_player else static_evaluation_of_game_field(game_field, player_two, player_one)

    if maximizing_player:
        max_evaluation = -inf
        for position in get_all_moves(game_field):               # TODO
            evaluation = minimax(position, depth - 1, alpha, beta, False, player_two, player_one)
            max_evaluation = max(max_evaluation, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return max_evaluation
    else:
        min_evaluation = +inf
        for position in get_all_moves(game_field):               # TODO
            evaluation = minimax(position, depth - 1, alpha, beta, True, player_one, player_two)
            min_evaluation = min(min_evaluation, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return min_evaluation


def static_evaluation_of_game_field(game_field, player_one, player_two):
    grid = game_field.graph
    evaluations_for_first = []
    evaluations_for_second = []
    for win_position in player_one.for_win:
        grid.cleanup()
        start = grid.node(player_one.current_position.y, player_one.current_position.x)
        end = grid.node(win_position[1], win_position[0])

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        if len(path) >= 2:
            evaluations_for_first.append(len(path))
    for win_position in player_two.for_win:
        grid.cleanup()
        start = grid.node(player_two.current_position.y, player_two.current_position.x)
        end = grid.node(win_position[1], win_position[0])

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        if len(path) >= 2:
            evaluations_for_second.append(len(path))
    min_first = min(evaluations_for_first)
    min_second = min(evaluations_for_second)
    evaluation = min_first - min_second

    return evaluation
