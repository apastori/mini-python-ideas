from initial_list import initial_list
from display_game import display_game
from position_choice import position_choice
from replacement_choice import replacement_choice
from gameon_choice import gameon_choice

def main():
    print("Word Replacement Game")
    game_on = True
    game_list = initial_list
    while game_on:
        display_game(game_list)
        position = position_choice()
        game_list = replacement_choice(game_list, position)
        display_game(game_list)
        game_on = gameon_choice()


if __name__ == "__main__":
    main()