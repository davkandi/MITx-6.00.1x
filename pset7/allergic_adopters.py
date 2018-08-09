class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        self.name = name
        self.desired_species = desired_species
        self.allergic_species = allergic_species
        
    def get_score(self, adoption_center):
        for animal in self.allergic_species:
            if adoption_center.get_number_of_species(animal) != 0:
                return 0.0
        return Adopter.get_score(self, adoption_center)
class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
        self.medicine_effectiveness = medicine_effectiveness
        
    def get_score(self, adoption_center):
        Listvalue = []
        for animal in self.medicine_effectiveness.keys():
            if adoption_center.get_number_of_species(animal) != 0:
                Listvalue.append(self.medicine_effectiveness[animal])
                
        if Listvalue != []:
            return Adopter.get_score(self, adoption_center) * min(Listvalue)
        else:
            return Adopter.get_score(self, adoption_center)
