def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    lenght = 0
    for x in hand.keys():
        lenght += hand[x]
    return lenght
