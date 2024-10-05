from Hand import Hand
from Deck import Deck

def hit(deck,hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()