class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = (float(location[0]), float(location[1]))
        
    def get_linear_distance(self, to_location):
        d = to_location
        return ((d[0] - self.location[0]) ** 2 + (d[1] - self.location[1]) ** 2) ** 0.5 #sqrt((to_location[0] - self.location[0]) ** 2 + (to_location[1] - self.location[1]) ** 2) 
        
    def get_score(self, adoption_center):
        import random
        location = adoption_center.get_location()
        distance = self.get_linear_distance(location)
        
        if distance < 1.0 and distance > 0.0:
            return adoption_center.get_number_of_species(self.desired_species)
        elif distance < 3 and distance >= 1:
            return random.uniform(0.7, 0.9) * adoption_center.get_number_of_species(self.desired_species)
        elif distance < 5 and distance > 3:
            return random.uniform(0.5, 0.7) * adoption_center.get_number_of_species(self.desired_species)
        else:
            return random.uniform(0.1, 0.5) * adoption_center.get_number_of_species(self.desired_species)
