"""Zoo."""


class Animal:
    """Animal class."""

    def __init__(self, name: str, species: str, age: int):
        """
        Class constructor.

        Each animal has a name and a specie.
        :param name: animal name
        :param specie: animal specie
        """
        self.name = name
        self.species = species
        self.age = age
        
    def __repr__(self):
        return self.name + ' ' + str(self.age)


class Zoo:
    """Zoo class."""

    def __init__(self, name: str, max_number_of_animals: int):
        """
        Class constructor.

        Each zoo has a name and max number of animals the zoo can have.
        There also should be an overview of all animals present in the zoo.

        :param name: zoo name
        :param max_number_of_animals: how many animals can be in the zoo
        """
        self.name = name
        self.max_number_of_animals = max_number_of_animals
        self.animals = []
        pass

    def can_add_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be added to the zoo.

        Animal can be added to the zoo if:
        1. Adding a new animal does not exceed zoo's max number of animals.
        2. Same Animal object is not present in the zoo.
        3. Animal with same name and specie is not yet present in the zoo.
        :param animal: animal who is checked
        :return: bool describing whether the animal can be added to the zoo or not
        """
        if len(self.animals) + 1 > self.max_number_of_animals:
            return False
        if animal in self.animals:
            return False
        for zoo_animal in self.animals:
            if animal.name == zoo_animal.name and animal.species == zoo_animal.species:
                return False
        else:
            return True
        # for zoo_animal in self.animals:
            # if animal.name == zoo_animal.name and animal.species == zoo_animal.species:
                # return False
        # if animal not in self.animals:
            # if len(self.animals) + 1 > self.max_number_of_animals:
                # return False
            # else:
                # return True
        pass

    def add_animal(self, animal: Animal):
        """
        Add animal to the zoo if possible.

        :param animal: animal who is going to be added to the zoo
        Function does not return anything
        """
        if self.can_add_animal(animal):
            self.animals.append(animal)
        pass

    def can_remove_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be removed from the zoo.

        Animal can be removed from the zoo if animal is present in the zoo.

        :param animal: animal who is checked
        :return: bool describing whether animal can be removed from the zoo or not.
        """
        if animal in self.animals:
            return True
        else:
            return False
        pass

    def remove_animal(self, animal: Animal):
        """
        Remove animal from the zoo if possible.

        :param animal: animal who is going to be removed from the zoo.
        Function does not return anything
        """
        if self.can_remove_animal(animal):
            self.animals.remove(animal)
        pass

    def get_all_animals(self):
        """
        Return a list with all the animals in the zoo.

        :return: list of Animal objects
        """
        return self.animals
        pass

    def get_animals_by_age(self):
        """
        Return a list of animals sorted by age (from younger to older).

        :return: list of Animal objects sorted by age
        """
        return sorted(self.animals, key=lambda animal: animal.age)
        pass

    def get_animals_sorted_alphabetically(self):
        """
        Return a list of animals sorted (by name) alphabetically.

        :return: list of Animal objects sorted by name alphabetically
        """
        return sorted(self.animals, key=lambda animal: animal.name)
        pass

a1 = Animal('a1', 'karu', 15)
a2 = Animal('a2', 'ilves', 15)
a3 = Animal('a3', 'karu', 15)
a4 = Animal('a1', 'karu', 15)
zoo = Zoo('test', 2)
zoo.add_animal(a1)
zoo.add_animal(a2)
zoo.add_animal(a3)
zoo.add_animal(a4)
print(zoo.animals)
