from Player import Player
from Deck import Deck

def war_game():
    # Players
    player_one = Player('One')
    player_two = Player('Two')

    # Deck
    new_deck = Deck()
    # Shuffle Created Deck
    new_deck.shuffle()

    # Split Deck in half between the two players
    number_half_deck = len(new_deck.all_cards) / 2
    for i in range(0, int(number_half_deck)):
        card_player_one = new_deck.deal_one()
        player_one.add_cards(card_player_one)
        card_player_two = new_deck.deal_one()
        player_two.add_cards(card_player_two)


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
        at_war = True
        #Players at War
        while at_war:
            # Player 1 has the highest card
            if player_one_cards[-1].value > player_one_cards[-1].value:
                # Player One gets the cards because card is higher value
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                # time for next round
                at_war = False
                break
            # Player Two Has highest Card
            if player_one_cards[-1].value < player_two_cards[-1].value:

                # Player Two gets the cards
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                
                # time for next round
                at_war = False
                break
            # Start
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            if len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            for num in range(5):
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())
