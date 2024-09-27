def replacement_choice(game_list, position):
    user_string = input('Type a string to place at the position')
    game_list[position] = user_string
    return game_list