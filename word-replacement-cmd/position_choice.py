def position_choice():
    choice = ''
    while choice not in ['0', '1', '2']:
        choice = input('Pick a Position to replace in list (0,1,2): ')
        if choice not in ['0', '1', '2']:
            print('Sorry you did not choose a valid position (0, 1, 2)')
    return int(choice)