def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    n = HAND_SIZE
    touch = ''
    hand = {}
    while touch != 'n' or touch != 'r' or touch != 'e': 
        touch = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if (touch == 'n'):
            hand = dealHand(n)
            playHand(hand, wordList, n)
        elif (touch == 'r'):
            if hand == {}:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                playHand(hand, wordList, n)
        elif (touch == 'e'):
            break
        else:
            print('Invalid Command.')

