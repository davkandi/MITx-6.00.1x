def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    def getKey(item):
        return item[1]
    
    List1 = []
    for ac in list_of_adoption_centers:
        List1.append([ac, adopter.get_score(ac)])  
    List1.sort(key = getKey, reverse = True)
    
    Listscore = []
    for elt in List1:
        Listscore.append(elt[0])
    return Listscore
         
def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    def getKey(item):
        return item[1]
    def getKey2(item):
        return item[0]
        
    List1 = []
    for e in list_of_adopters:
        List1.append([e, e.get_score(adoption_center)])
    List1.sort(key = getKey2)
    List1.sort(key= getKey, reverse = True)
    Listscore = []
    for elt in List1:
        Listscore.append(elt[0])
        
    FinalL = []
    for elt in Listscore: 
        if n == 0:
            break
        else:
            FinalL.append(elt)
            n -= 1
    return FinalL
