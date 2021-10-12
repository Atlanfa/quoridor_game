from Coordinate import Coordinate


class Player:
    def __init__(self, player_type, player_number):
        self.player_type = player_type  # True - Player, False - computer
        self.player_number = player_number  # int
        self.walls_amount = 10
        self.current_position = self._set_start_position()
        self.next_position = None
        self.can_move_here = None
        self.places_to_move = None

    def isWin(self):
        if self.player_number == 1:
            if self.current_position.x == 0:
                return True
        if self.player_number == 2:
            if self.current_position.x == 16:
                return True
        return False

    def _set_start_position(self):
        return Coordinate(16, 8) if self.player_number == 1 else Coordinate(0, 8)

    def decrease_wall_amount(self):
        if self.walls_amount != 0:
            self.walls_amount -= 1

    def set_places_to_move(self, game_field):
        places_to_move_list = []
        if self.current_position.x == 0 and 0 < self.current_position.y < 16:
            if self.check_right(game_field.field):
                places_to_move_list.append(self.right())
            if self.check_left(game_field.field):
                places_to_move_list.append(self.left())
            if self.check_down(game_field.field):
                places_to_move_list.append(self.down())
        elif self.current_position.x == 16 and 0 < self.current_position.y < 16:
            if self.check_right(game_field.field):
                places_to_move_list.append(self.right())
            if self.check_left(game_field.field):
                places_to_move_list.append(self.left())
            if self.check_up(game_field.field):
                places_to_move_list.append(self.up())
        elif self.current_position.x == 0 and self.current_position.y == 0:
            if self.check_down(game_field.field):
                places_to_move_list.append(self.down())
            if self.check_right(game_field.field):
                places_to_move_list.append(self.right())
        elif self.current_position.x == 0 and self.current_position.y == 16:
            if self.check_down(game_field.field):
                places_to_move_list.append(self.down())
            if self.check_left(game_field.field):
                places_to_move_list.append(self.left())
        elif self.current_position.x == 16 and self.current_position.y == 0:
            if self.check_up(game_field.field):
                places_to_move_list.append(self.up())
            if self.check_right(game_field.field):
                places_to_move_list.append(self.right())
        elif self.current_position.x == 16 and self.current_position.y == 16:
            if self.check_up(game_field.field):
                places_to_move_list.append(self.up())
            if self.check_left(game_field.field):
                places_to_move_list.append(self.left())
        elif 0 < self.current_position.x < 16 and self.current_position.y == 16:
            if self.check_down(game_field.field):
                places_to_move_list.append(self.down())
            if self.check_up(game_field.field):
                places_to_move_list.append(self.up())
            if self.check_left(game_field.field):
                places_to_move_list.append(self.left())
        elif 16 > self.current_position.x > 0 == self.current_position.y:
            if self.check_down(game_field.field):
                places_to_move_list.append(self.down())
            if self.check_up(game_field.field):
                places_to_move_list.append(self.up())
            if self.check_right(game_field.field):
                places_to_move_list.append(self.right())
        elif 0 < self.current_position.x < 16 and 0 < self.current_position.y < 16:
            if self.check_down(game_field.field):
                places_to_move_list.append(self.down())
            if self.check_up(game_field.field):
                places_to_move_list.append(self.up())
            if self.check_right(game_field.field):
                places_to_move_list.append(self.right())
            if self.check_left(game_field.field):
                places_to_move_list.append(self.left())
        self.places_to_move = places_to_move_list

    def set_next_position(self, coordinate):
        if coordinate.is_correct and coordinate in self.places_to_move:
            self.next_position = coordinate
            self.can_move_here = True
        else:
            self.next_position = None
            self.can_move_here = False

    def up(self):
        return Coordinate(self.current_position.x - 2, self.current_position.y)

    def down(self):
        return Coordinate(self.current_position.x + 2, self.current_position.y)

    def left(self):
        return Coordinate(self.current_position.x, self.current_position.y - 2)

    def right(self):
        return Coordinate(self.current_position.x, self.current_position.y + 2)

    def check_up(self, field):
        return True if field[self.current_position.x - 1][self.current_position.y] == 3 else False

    def check_down(self, field):
        return True if field[self.current_position.x + 1][self.current_position.y] == 3 else False

    def check_right(self, field):
        return True if field[self.current_position.x][self.current_position.y + 1] == 3 else False

    def check_left(self, field):
        return True if field[self.current_position.x][self.current_position.y - 1] == 3 else False

# player = Player(True, 1)
# print(f"x-{player.current_position.x} y-{player.current_position.y}")
# print(player.next_position)
