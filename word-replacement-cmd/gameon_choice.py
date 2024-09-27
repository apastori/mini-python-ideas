def gameon_choice():
    choice = ''
    while choice.upper() not in ['Y', 'N']:
        choice = input('Would you like to keep playing? Y or N')
        if choice.upper() not in ['Y', 'N']:
            print('Sorry, please select Yy or Nn')
    if choice.upper() == 'Y':
        return True
    return False