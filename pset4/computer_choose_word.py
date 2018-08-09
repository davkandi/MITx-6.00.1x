def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    def isThere(word, hand):
        '''
        my function to test is a word is in a hand
        '''
        handcopy = hand.copy()
        counter = 0
        for x in word:
            if handcopy.get(x, 0) != 0:
                handcopy[x] -= 1
                counter += 1
            else:
                return False
        if counter == len(word):
            return True
        else:
            return False
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestscore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestword = 'None'
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isThere(word, hand) == True:                   
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > bestscore:
                # Update your best score, and best word accordingly
                bestscore = score
                bestword = word

    # return the best word you found.
    return bestword

