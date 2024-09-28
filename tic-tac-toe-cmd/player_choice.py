from space_check import space_check

def player_choice(board):
    position = 0
    while (position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or 
    not space_check(board, position)):
        new_position = input('Choose your next position: (1-9)')
        if not new_position.isdigit():
            continue
        position = int(new_position)
        if position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Choose valid position: (1-9)")
            continue
        if not space_check(board, position):
            print("Position inserted is already in use")
            continue
    return position