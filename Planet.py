import random


class Planet():
    counter = 0

    def __init__(self):
        distance = random.uniform(1, 300) #it will be calculated in millions later
        self.distance = distance
        self.isLife = False # set to false by default, we will change it later if it has intelligent life
        self.planetNumber = self.__class__.counter + 1
        self.__class__.counter += 1




class RockyPlanet(Planet):
    def __init__(self):
        Planet.__init__(self)
        self.identifier = "r"

class GaseousPlanet(Planet):
    def __init__(self):
        Planet.__init__(self)
        self.identifier = "g"



class HabitablePlanet(Planet):
    def __init__(self):
        Planet.__init__(self)
        self.identifier = "h"



