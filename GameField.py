from Graph import update_connections_from_field, create_graph
from Node import create_nodes_from_field


def calculate_point(point):
    return int(point/2)


def backwards_calculating_point(point):
    return point + (point - 2)


def get_connected_points(field):
    connected_points = []
    for i in range(0, len(field), 2):
        for j in range(0, len(field[i]), 2):
            if i != len(field) - 1 and j != len(field) - 1:
                if field[i][j + 1] == 3:
                    connected_points.append(
                        ((calculate_point(i), calculate_point(j)), (calculate_point(i), calculate_point(j + 2))))
                if field[i+1][j] == 3:
                    connected_points.append(
                        ((calculate_point(i), calculate_point(j)), (calculate_point(i + 2), calculate_point(j))))
            else:
                if i == len(field) - 1 and j != len(field) - 1:
                    if field[i][j + 1] == 3:
                        connected_points.append(
                            ((calculate_point(i), calculate_point(j)), (calculate_point(i), calculate_point(j + 2))))
                if j == len(field) - 1 and i != len(field) - 1:
                    if field[i + 1][j] == 3:
                        connected_points.append(
                            ((calculate_point(i), calculate_point(j)), (calculate_point(i + 2), calculate_point(j))))
    #print(connected_points)
    return connected_points


def fill_the_field():
    field = []

    for row_index in range(9):
        if row_index != 8:
            row_items = []
            for row_item_index in range(9):
                if row_item_index != 8:
                    row_items.append(0)
                    row_items.append(3)
                else:
                    row_items.append(0)
            field.append(row_items)
            field.append([3 for i in range(17)])
        else:
            row_items = []
            for row_item_index in range(9):
                if row_item_index != 8:
                    row_items.append(0)
                    row_items.append(3)
                else:
                    row_items.append(0)
            field.append(row_items)
    return field


def field_preparation(field):
    center_real = backwards_calculating_point(5)
    field[0][center_real] = 2
    field[-1][center_real] = 1
    return field


class GameField:
    def __init__(self):
        self.field = self.get_start_field()
        self.nodes = create_nodes_from_field(self.field)
        self.graph = update_connections_from_field(get_connected_points(self.field), create_graph(self.nodes), self.nodes)

    @staticmethod
    def get_start_field():
        return field_preparation(fill_the_field())

    def set_wall(self, wall):
        self.field[wall.coordinates_start.x][wall.coordinates_start.y] = 4
        self.field[wall.coordinates_end.x][wall.coordinates_end.y] = 4
        self.field[wall.coordinates_middle.x][wall.coordinates_middle.y] = 4
        self.graph = update_connections_from_field(get_connected_points(self.field), create_graph(self.nodes), self.nodes)

    def move_player(self, player):
        self.field[player.current_position.x][player.current_position.y] = 0
        self.field[player.next_position.x][player.next_position.y] = player.player_number
        player.current_position = player.next_position


# game_field = GameField()
# for row in game_field.field:
#     print(row)