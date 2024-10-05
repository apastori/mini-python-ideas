from suits import suits
from ranks import ranks
from Card import Card
import random

class Deck:
    def __init__(self):
        self.all_cards = []
        self.deck = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.all_cards.append(new_card)
                self.deck.append(new_card)
    def __str__(self):
        deck_str = ''
        for card in self.all_cards:
            deck_str += '\n '+ card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_str
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()