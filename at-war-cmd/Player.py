from Card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_card(self, new_cards):
        # new_cards can be a single card
        # or a list of cards
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        elif isinstance(new_cards, Card):
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards left.'