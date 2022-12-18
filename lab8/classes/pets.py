

class Pets:
    pets_list =[] #список тварин

    @classmethod
    def add_pet(cls, pet): #додавання тваринки в лист
        cls.pets_list.append(pet)
