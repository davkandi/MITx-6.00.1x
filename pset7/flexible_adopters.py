class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        self.name = name
        self.desired_species = desired_species
        self.considered_species = considered_species
        
    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)
        num_other = 0
        for elt in self.considered_species:
            num_other += adoption_center.get_number_of_species(elt)
            
        return adopter_score + 0.3 * num_other
            
class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        self.name = name
        self.desired_species = desired_species
        self.feared_species = feared_species
        
    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)

        num_feared = adoption_center.get_number_of_species(self.feared_species)
            
        if adopter_score - 0.3 * num_feared >= 0:
            return adopter_score - 0.3 * num_feared
        else:
            return 0.0
