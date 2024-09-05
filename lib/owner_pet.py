class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self, name,pet_type= 'dog',owner= 'fido') -> None:
        if pet_type not in self.PET_TYPES:
            raise Exception(f'{pet_type} is not a valid pet type')
        self.name = name
        self.owner = owner
        self.pet_type = pet_type
        Pet.all.append(self)

    
    


         
class Owner:
    def __init__(self, name) -> None:
        self.name = name
    def pets(self):
      return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self,pet):
        if pet.owner is not self:
            pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(Pet.all, key=lambda pet: pet.name)
        return sorted_pets           