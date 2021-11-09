from infinity import inf


def minimax(game_field, depth, alpha, beta, maximizing_player):
    if depth == 0 or game_field.game_over():
        return static_evaluation_of_game_field(game_field)      # TODO

    if maximizing_player:
        max_evaluation = -inf
        for position in get_all_moves(game_field):               # TODO
            evaluation = minimax(position, depth - 1, alpha, beta, False)
            max_evaluation = max(max_evaluation, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return max_evaluation
    else:
        min_evaluation = +inf
        for position in get_all_moves(game_field):               # TODO
            evaluation = minimax(position, depth - 1, alpha, beta, True)
            min_evaluation = min(min_evaluation, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return min_evaluation
