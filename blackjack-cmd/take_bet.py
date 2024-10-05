def take_bet(player_chips):
    while True:
        player_bet = input('How many chips would you like to bet? ')
        try:
            player_bet_num = int(player_bet)
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if player_bet_num > player_chips.total:
                print("Sorry, your bet can't exceed",player_chips.total)
            else:
                return player_bet_num