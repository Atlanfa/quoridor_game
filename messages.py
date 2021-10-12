def choose_action_message(player):
    print(f"{player.player_number} player turn, choose action.\n1 - Move hero.\n2 - Place the wall.")


def move_player_message():
    print("Choose action:\nChoose coordinates from list below or type 'back' for returning to choosing between moving "
          "hero or placing wall")


def print_places_to_move(places_to_move):
    counter = 1
    for place in places_to_move:
        print(f"{counter} - {place.x} {place.y}")
        counter += 1
    print("Type 'back' for return")


def wrong_action_message(e = None):
    print("You entered wrong action")
    print(e)


def place_the_wall_message():
    print("Enter wall start coordinates and end coordinates(like '0 1 2 1') or type 'back' for returning to choosing "
          "between moving hero or placing wall")


def win_message(player):
    print(f"{player.player_number} player won. Do you want to play again(type yes for playing again).")

    # print(f"{win_status['player'].capitalize()} won. Do you want to play again(type yes for playing again).")

def print_field(field):
    num_horizontal = "     "
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