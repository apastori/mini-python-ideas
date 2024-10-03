from ranks_values import ranks_values

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = ranks_values[rank]
    def __str__(self):
        return self.rank + 'Of ' + self.suit