import random
from players import players

def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return players[0]
    return players[1]