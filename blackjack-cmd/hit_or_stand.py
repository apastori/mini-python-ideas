from hit import hit

def hit_or_stand(deck,hand):
    hit_stand = ''
    hit_stand_tuple = ('h', 's')
    while hit_stand != hit_stand_tuple[1]:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function imported above
            hit_stand = hit_stand_tuple[0]
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            hit_stand = hit_stand_tuple[1]
        else:
            print("Sorry, unknown option entered. Please try again.")
            continue
        break
    return hit_stand