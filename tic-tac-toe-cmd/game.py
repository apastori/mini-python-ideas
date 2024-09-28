from player_input import player_input
from choose_first import choose_first
from display_board import display_board
from player_choice import player_choice
from place_marker import place_marker
from prev_board import prev_board
from show_prev_board import show_prev_board
from win_check import win_check
from full_board_check import full_board_check
from players import players
from replay import replay
import copy

def game():
    print("Welcome to Tic-Tac-Toe")
    while True:
        the_board = [' '] * 10
        game_on = None
        prev_the_board = copy.deepcopy(the_board)
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')
        play_game = input('Are you ready to play? Enter Yes or No.')
        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False
        while game_on:
            if turn[-1] == '1':
                # Player1's turn.
                print("Player1 Turn")
                display_board(the_board)
                position = player_choice(the_board)
                # prev display message
                prev_the_board = prev_board(prev_the_board, position)
                show_prev_board(prev_the_board)
                keep_choice = input("Want to insert mark in position with $? Enter Yes (y) or No (n)")
                if not keep_choice.lower().startswith('y'):
                    prev_the_board = copy.deepcopy(the_board)
                    continue
                the_board = place_marker(the_board, player1_marker, position)
                prev_the_board = copy.deepcopy(the_board)
                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = players[1]
            elif (turn[-1] == '2'):
                # Player2's turn
                print("Player2 Turn")
                display_board(the_board)
                position = player_choice(the_board)
                # prev display message
                prev_the_board = prev_board(prev_the_board, position)
                show_prev_board(prev_the_board)
                keep_choice = input("Want to insert mark in position with $? Enter Yes (y) or No (n)")
                if not keep_choice.lower().startswith('y'):
                    prev_the_board = copy.deepcopy(the_board)
                    continue
                the_board = place_marker(the_board, player2_marker, position)
                prev_the_board = copy.deepcopy(the_board)
                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = turn = players[0]
            else:
                raise ValueError("Turn Value is not correct")
        if not replay():
            print('Shutting Down the Game')
            break