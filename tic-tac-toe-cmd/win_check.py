def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # Top Horizonal Line
    (board[4] == mark and board[5] == mark and board[6] == mark) or # Middle Horizonal Line
    (board[7] == mark and board[8] == mark and board[9] == mark) or # Bottom Horizontal Line
    (board[1] == mark and board[4] == mark and board[7] == mark) or # Vertical Left Line
    (board[2] == mark and board[5] == mark and board[8] == mark) or # Vertical Middle Line
    (board[3] == mark and board[6] == mark and board[9] == mark) or # Vertical Rigth Line
    (board[1] == mark and board[5] == mark and board[9] == mark) or # Diagonal LXY
    (board[3] == mark and board[5] == mark and board[7] == mark)) # Diagonal RXY