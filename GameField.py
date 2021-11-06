from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


def calculate_point(point):
    return int(point / 2)


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
                if field[i + 1][j] == 3:
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
    # # print(connected_points)
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
    for i in range(16):
        for j in range(16):
            if i % 2 == 1 and j % 2 == 1:
                field[i][j] = 5
    return field


def field_preparation(field):
    center_real = backwards_calculating_point(5)
    field[0][center_real] = 2
    field[-1][center_real] = 1
    return field


class GameField:
    def __init__(self):
        self.field = self.get_start_field()
        self.graph = self.set_graph()

    @staticmethod
    def get_start_field():
        return field_preparation(fill_the_field())

    def set_graph(self):
        grid = Grid(matrix=self.graphPrepare(self.field))
        return grid

    def pathfinder(self, players):  # players - список игроков, field - экземпляр класса GameField
        grid = self.graph
        fpWay = False  # Есть ли путь для первого игрока
        spWay = False  # Есть ли путь для второго игрока

        for win in players[0].forWin:
            grid.cleanup()
            start = grid.node(players[0].current_position.y, players[0].current_position.x)
            end = grid.node(win[1], win[0])

            finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
            path, runs = finder.find_path(start, end, grid)
            # # print('operations:', runs, 'path length:', len(path)) #Тестовый вывод
            # # print(grid.grid_str(path=path, start=start, end=end))
            if len(path) >= 2:
                fpWay = True
                break
        for win in players[1].forWin:
            grid.cleanup()
            start = grid.node(players[1].current_position.y, players[1].current_position.x)
            end = grid.node(win[1], win[0])

            finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
            path, runs = finder.find_path(start, end, grid)
            # # print('operations:', runs, 'path length:', len(path)) #Тестовый вывод
            # # print(grid.grid_str(path=path, start=start, end=end))
            if len(path) >= 2:
                spWay = True
                break
        if fpWay and spWay:
            return True
        else:
            return False

    def graphPrepare(self, field):
        tempField = []
        for i in range(len(field[0])):
            tempField.append([])
            for j in range(len(field[1])):
                if field[i][j] == 0:
                    tempField[i].append(1)  # Пустая клетка
                elif field[i][j] == 3:
                    tempField[i].append(3)  # Пустая стенка
                elif field[i][j] == 4:
                    tempField[i].append(0)  # Стенка
                elif field[i][j] == 5:
                    tempField[i].append(0)  # Стенка
                elif field[i][j] == 1:
                    tempField[i].append(1)  # Игрок
                elif field[i][j] == 2:
                    tempField[i].append(1)  # Игрок

        return tempField

    def set_wall(self, wall):
        self.field[wall.coordinates_start.x][wall.coordinates_start.y] = 4
        self.field[wall.coordinates_end.x][wall.coordinates_end.y] = 4
        self.field[wall.coordinates_middle.x][wall.coordinates_middle.y] = 4

    def move_player(self, player):
        self.field[player.current_position.x][player.current_position.y] = 0
        self.field[player.next_position.x][player.next_position.y] = player.player_number
        player.current_position = player.next_position

# game_field = GameField()
# messages.# print_field(game_field.field)
# for row in game_field.field:
#     # print(row)
# player = Player(True, 1)
# field = GameField()
# for i in field.field:
#     # print(i)
# # print(field.pathfinder([player, player]))
