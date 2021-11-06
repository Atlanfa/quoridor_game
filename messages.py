from Coordinate import Coordinate
from GameField import GameField
from Player import Player
from Wall import Wall

def send_wall(wall):
    if wall.coordinates_start.x == wall.coordinates_end.x:
        print(f"wall {chr(int(wall.coordinates_middle.y / 2 + 96 + 19)).capitalize()}{int((wall.coordinates_middle.x + 1) / 2)}h")
    else:
        print(f"wall {chr(int(wall.coordinates_middle.y / 2 + 96 + 19)).capitalize()}{int((wall.coordinates_middle.x + 1) / 2)}v")

def send_move(player):
    print(f"move {chr(int(player.current_position.y / 2 + 96) + 1).capitalize()}{int(player.current_position.x / 2) + 1}")

def send_jump(player):
    print(f"jump {chr(int(player.current_position.y / 2 + 96) + 1).capitalize()}{int(player.current_position.x / 2) + 1}")

def choose_action_message(player):
    print(f"{player.player_number} player turn, choose action.\n1 - Move hero.\n2 - Place the walll.")
    pass


def move_player_message():
    print("Choose action:\nChoose coordinates from list below or type 'back' for returning to choosing between moving "
          "hero or placing wall")
    pass


def print_places_to_move(places_to_move):
    counter = 1
    for place in places_to_move:
        print(f"{counter} - {place.x} {place.y}")
        counter += 1
    print("Type 'back' for return")
    pass


def wrong_action_message(e=None):
    print("You entered wrong action")
    print(e)
    pass


def place_the_wall_message():
    print("Enter wall start coordinates and end coordinates(like '0 1 2 1') or type 'back' for returning to choosing "
          "between moving hero or placing wall")
    pass


def win_message(player, field):
    print_field(field)
    print(f"{player.player_number} player won. Do you want to play again(type yes for playing again).")


def print_field(field):
    a = 1
    if a == 0:
        num_horizontal = "    "
        counter = 0
        for item in field[0]:
            if counter < 10:
                num_horizontal += f"{counter}  "
                counter += 1
            else:
                num_horizontal += f"{counter} "
                counter += 1
        print(num_horizontal)

        num_horizontal = "     "
        counter = 0
        for item in field[0]:
            if item == 0 or item == 1 or item == 2:
                num_horizontal += f"{counter}"
                counter += 1
            else:
                num_horizontal += "     "
        print(num_horizontal)

        counter_1 = 0
        counter_2 = 0
        for row in field:
            if row[0] == 0 or row[0] == 1 or row[0] == 2:
                if counter_2 < 10:
                    print(f"{counter_2}  {counter_1}{row}")
                    counter_1 += 1
                    counter_2 += 1
                else:
                    print(f"{counter_2} {counter_1}{row}")
                    counter_1 += 1
                    counter_2 += 1

            else:
                if counter_2 < 10:
                    print(f"{counter_2}   {row}")
                    counter_2 += 1
                else:
                    print(f"{counter_2}  {row}")
                    counter_2 += 1
    else:
        for index, i in enumerate(field):
            for index2, j in enumerate(i):
                if j == 5:
                    print("\033[33m {}".format("+"), end="")
                elif j == 3:
                    print("\033[37m {}".format(" "), end="")
                elif j == 0:
                    print("\033[32m {}".format("0"), end="")
                elif j == 1:
                    print("\033[31m {}".format("X"), end="")
                elif j == 2:
                    print("\033[31m {}".format("M"), end="")
                elif j == 4:
                    print("\033[33m {}".format("#"), end="")
            print()




def with_who_you_want_to_play():
    print("Choose how to play:\n1)Play with human\n2)Play with bot\n3)Bot vs bot")

# gamef = GameField()
# walls = Wall(Coordinate(1, 0), Coordinate(1, 2), gamef)
# walls = Wall(Coordinate(14, 15), Coordinate(16, 15), gamef)
# walls = Wall(Coordinate(2, 1), Coordinate(4, 1), gamef)
# walls = Wall(Coordinate(2, 3), Coordinate(0, 3), gamef)
# walls = Wall(Coordinate(1, 2), Coordinate(1, 4), gamef)
# walls = Wall(Coordinate(15, 14), Coordinate(15, 16), gamef)
# send_wall(walls)

# pla = Player(True, 1)
# pla.current_position.x = 16
# pla.current_position.y = 0
# send_move(pla)