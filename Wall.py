from Coordinate import Coordinate
from GameField import calculate_point, get_connected_points
from Graph import update_connections_from_field, create_graph


class Wall:
    def __init__(self, coordinates_start, coordinates_end):
        self.coordinates_start = coordinates_start
        self.coordinates_end = coordinates_end
        self.coordinates_middle = self.set_coordinates_middle()
        self.is_length_correct = self.if_length_correct()
        self.between_two_pares = None
        self.is_there_another_wall = None
        self.is_there_path_to_win = None

    def set_coordinates_middle(self):
        if self.coordinates_start.y == self.coordinates_end.y:
            if self.coordinates_start.x > self.coordinates_end.x:
                return Coordinate(self.coordinates_end.x + 1, self.coordinates_start.y)
            else:
                return Coordinate(self.coordinates_start.x + 1, self.coordinates_start.y)
        else:
            if self.coordinates_start.y > self.coordinates_end.y:
                return Coordinate(self.coordinates_start.x, self.coordinates_end.y + 1)
            else:
                return Coordinate(self.coordinates_start.x, self.coordinates_start.y + 1)

    def if_length_correct(self):
        if self.coordinates_start.x == self.coordinates_end.x:
            if self.coordinates_start.y > self.coordinates_end.y:
                return True if len([num for num in range(self.coordinates_end.y + 1, self.coordinates_start.y)]) == 1 else False
            else:
                return True if len([num for num in range(self.coordinates_start.y + 1, self.coordinates_end.y)]) == 1 else False
        elif self.coordinates_start.y == self.coordinates_end.y:
            if self.coordinates_start.x > self.coordinates_end.x:
                return True if len([num for num in range(self.coordinates_end.x + 1, self.coordinates_start.x)]) == 1 else False
            else:
                return True if len([num for num in range(self.coordinates_start.x + 1, self.coordinates_end.x)]) == 1 else False
        else:
            return False

    def if_between_two_pares(self, game_field):
        if self.coordinates_start.y == self.coordinates_end.y:
            self.between_two_pares = True if game_field.field[self.coordinates_start.x][self.coordinates_start.y - 1] in [0, 1, 2] and game_field.field[self.coordinates_start.x][self.coordinates_start.y + 1] in [0, 1, 2] and game_field.field[self.coordinates_start.x][self.coordinates_end.y - 1] in [0, 1, 2] and game_field.field[self.coordinates_start.x][self.coordinates_end.y + 1] in [0, 1, 2] else False
        elif self.coordinates_start.x == self.coordinates_end.x:
            self.between_two_pares = True if game_field.field[self.coordinates_start.x - 1][self.coordinates_start.y] in [0, 1, 2] and game_field.field[self.coordinates_start.x + 1][self.coordinates_start.y] in [0, 1, 2] and game_field.field[self.coordinates_end.x - 1][self.coordinates_start.y] in [0, 1, 2] and game_field.field[self.coordinates_end.x + 1][self.coordinates_start.y] in [0, 1, 2] else False

    def if_there_another_wall(self, game_field):
        self.is_there_another_wall = False if game_field[self.coordinates_start.x][self.coordinates_start.y] == 3 and game_field[self.coordinates_end.x][self.coordinates_end.y] == 3 and game_field[self.coordinates_middle.x][self.coordinates_middle.y] == 3 else True

    def if_there_path_to_win(self, game_field, player1, player2):
        first = Coordinate(calculate_point(player1.current_position.x), calculate_point(player1.current_position.y))
        second = Coordinate(calculate_point(player2.current_position.x), calculate_point(player2.current_position.y))
        win_for_first = [node.data for node in game_field.nodes[0]]
        win_for_second = [node.data for node in game_field.nodes[-1]]
        graph = update_connections_from_field(get_connected_points(game_field.field), create_graph(game_field.nodes),
                                              game_field.nodes)
        endpoints_for_first = graph.get_all_endpoint(game_field.nodes[first.x][first.y])
        endpoints_for_second = graph.get_all_endpoint(game_field.nodes[second.x][second.y])
        first_win_result = [i for i in endpoints_for_first if i in win_for_first]
        second_win_result = [i for i in endpoints_for_second if i in win_for_second]
        if len(first_win_result) != 0 and len(second_win_result) != 0:
            self.is_there_path_to_win = True
        else:
            self.is_there_path_to_win = False
