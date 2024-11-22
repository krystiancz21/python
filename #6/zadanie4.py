from abc import ABC, abstractmethod
import random
import types

class Animal(ABC):
    """
    Abstract base class for animals.

    Attributes
    ----------
    name : str
        Animal name
    occurance : list
        List of habitats where the animal occurs
    is_protected : bool
        Whether the species is protected

    Methods
    -------
    info()
        Displays information about the animal
    """
    def __init__(self,name,occurance,is_protected):
        self.name = name
        self.occurance = occurance
        self.is_protected = is_protected
    
    @abstractmethod
    def info(self):
        print(f"Name: {self.name}, Occurence: {self.occurance}, Protected: {self.is_protected}")

class Predator(Animal):
    """
    Class representing a predator animal.

    Attributes
    ----------
    hunting_time : str
        Time of hunting ('day' or 'night')

    Methods
    -------
    info()
        Displays information about the predator
    hunt()
        Simulates hunting behavior
    """
    def __init__(self,name,occurance,is_protected,hunting_time):
        Animal.__init__(self,name,occurance,is_protected)
        self.hunting_time = hunting_time
    
    def info(self):
        print(f"Name: {self.name}, Occurence: {self.occurance}, Protected: {self.is_protected}, Hunting time: {self.hunting_time}")

    def hunt(self):
        print(f"{self.name} starts hunting")

class Herbivore(Animal):
    """
    Class representing a herbivorous animal.

    Attributes
    ----------
    favourite_plants : list
        List of preferred plants for feeding

    Methods
    -------
    info()
        Displays information about the herbivore
    search()
        Simulates searching for food
    """
    def __init__(self,name,occurance,is_protected,favourite_plants):
        Animal.__init__(self,name,occurance,is_protected)
        self.favourite_plants = favourite_plants
    
    def info(self):
        print(f"Name: {self.name}, Occurence: {self.occurance}, Protected: {self.is_protected}, Favourite plants: {self.favourite_plants}")

    def search(self):
        chosen_favourite_plant = random.choice(self.favourite_plants)
        print(f"{self.name} starts searching for {chosen_favourite_plant}")

class Omnivore(Predator, Herbivore):
    """
    Class representing an omnivorous animal.
    Inherits from both Predator and Herbivore classes.

    Methods
    -------
    info()
        Displays information about the omnivore
    """
    def __init__(self,name,occurance,is_protected,hunting_time,favourite_plants):
        Predator.__init__(self,name,occurance,is_protected,hunting_time)
        Herbivore.__init__(self,name,occurance,is_protected,favourite_plants)
    
    def info(self):
        print(f"Name: {self.name}, Occurence: {self.occurance}, Protected: {self.is_protected}, Hunting time: {self.hunting_time}, Favourite plants: {self.favourite_plants}")

def feeding_routine(self, hunt_time):
    """
    Determines feeding routine based on time of day.

    Parameters
        hunt_time(str): Time of feeding ('day' or 'night')

    During day the animal searches for plants, during night it hunts.
    """
    if hunt_time.lower() in ["day"]:
        self.search()
    elif hunt_time.lower() in ["night"]:
        self.hunt()
    else:
        print("Incorrect hunt_time value.")


if __name__ == "__main__":
    lion = Predator("Lion", ["Africa", "Asia"], True, "night")
    lion.info()
    lion.hunt()
    print('-'*10)

    rabbit = Herbivore("Rabbit", ["Europe", "Asia"], False, ["grass", "carrots", "clover"])
    rabbit.info()
    rabbit.search()
    print('-'*10)

    bear = Omnivore("Bear", ["Europe", "North America"], True, "day", ["berries", "honey", "nuts"])
    bear.info()
    bear.feeding_routine = types.MethodType(feeding_routine, bear)

    bear.feeding_routine("day")
    bear.feeding_routine("night")
    bear.feeding_routine("day")
    print("-- Try to add incorect value: --")
    bear.feeding_routine("evening")