def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabet = list(string.ascii_lowercase)
    
    for char in lettersGuessed:
        alphabet.remove(char)
    
    string = ''
    for letter in alphabet:
        string += letter
    
    return string
