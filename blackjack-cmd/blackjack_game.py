from Deck import Deck
from Hand import Hand
from Chips import Chips
from take_bet import take_bet
from show_some import show_some
from show_all import show_all
from hit_or_stand import hit_or_stand
from hit import hit
from player_bust import player_busts
from player_wins import player_wins
from dealer_busts import dealer_busts
from dealer_wins import dealer_wins
from push import push
from dealer_stand import dealer_stand

def blackjack_game():
    playing = True
    while True:
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
            Dealer hits until she reaches 17. Aces count as 1 or 11.')
        # Create Deck
        deck_game = Deck()
        # Shuffle Deck
        deck_game.shuffle()

        # Create Player Hand And Give him two cards
        player_hand = Hand()
        player_hand.add_card(deck_game.deal_one())
        player_hand.add_card(deck_game.deal_one())
        
        # Create Dealer Hand And Give him two cards
        dealer_hand = Hand()
        dealer_hand.add_card(deck_game.deal_one())
        dealer_hand.add_card(deck_game.deal_one())

        # Set up the Player's chips
        player_chips = Chips()  # remember the default value is 100    
        
        # Prompt the Player for their bet
        player_chips.bet = take_bet(player_chips)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        while playing:  # recall this variable from our hit_or_stand function
            # Prompt for Player to Hit or Stand
            hit_stand_option = hit_or_stand(deck_game,player_hand) 
            # Show cards (but keep one dealer card hidden)
            show_some(player_hand,dealer_hand)  
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)
                break
            if hit_stand_option == 's':
                playing = False        
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
        if player_hand.value <= 21:
            while dealer_hand.value < dealer_stand:
                hit(deck_game,dealer_hand)    
            # Show all cards
            show_all(player_hand,dealer_hand)
            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)
        # Inform Player of their chips total 
        print("\nPlayer's winnings stand at",player_chips.total)
        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        if new_game[0].lower()=='y':
            playing=True
            continue
        else:
            print("Thanks for playing!")
            break          
