def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(' ' + dealer.cards[1].__str__())  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')