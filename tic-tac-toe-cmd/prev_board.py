from place_marker import place_marker

def prev_board(board, position):
    board[position] = '$'
    return board