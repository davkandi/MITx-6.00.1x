def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = len(secretWord)
    for char in secretWord:
        if char in lettersGuessed:
            count -= 1
        else:
            return False
        
        if count == 0:
            return True
