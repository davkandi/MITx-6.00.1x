def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    handcopy = hand.copy()
    for x in word:
        if handcopy.get(x, 0) != 0:
            handcopy[x] -= 1
        else:
            return False
            
    if word in wordList:
        return True
    else:
        return False

