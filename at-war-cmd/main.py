from Player import Player
from Deck import Deck

# Players
player_one = Player('One')
player_two = Player('Two')

# Deck
new_deck = Deck()
# Shuffle Created Deck
new_deck.shuffle()

# Split Deck in half between the two players
number_half_deck = len(new_deck.all_cards) / 2
for i in range(0, number_half_deck):
    card_player_one = new_deck.deal_one()
    player_one.add_card(card_player_one)
    card_player_two = new_deck.deal_one()
    player_two.add_card(card_player_two)


# Prepare start the game
game_on = True
round_num = 0

# Start War Game
while game_on:
    round_num += 1
    print('Round {}'.format(round_num))
    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
    #No Players out of Cards, Game On
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

