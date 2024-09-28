from marker import marker

def player_input():
    marker_i = ''
    while not (marker_i == marker[0] or marker_i == marker[1]):
        marker_i = input("Player 1 choose X(x) or O(o)").upper()
    if marker_i == 'X':
        return ('X', 'O')
    return ('O', 'X')
    
    