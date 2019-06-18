import random

class Star():

    def __init__(self):
        _x = random.randint(2**3, 2**64-1)
        _y = random.randint(2**3, 2**64-1)
        _z = random.randint(2**3, 2**64-1)
        self._x = _x
        self._y = _y
        self._z = _z
        self.isVisited = False  # set to False by default
        self.probeDistant = 0 # set 0 by default



    def coordinateControl(self,list):

        for i in range(len(list)):
            if(self._x==list[i]._x and self._y==list[i]._y and self._z==list[i]._z):
                while(self._x==list[i]._x and self._y==list[i]._y and self._z==list[i]._z):
                    _x = random.randint(2 ** 3, 2 ** 64 - 1)
                    _y = random.randint(2 ** 3, 2 ** 64 - 1)
                    _z = random.randint(2 ** 3, 2 ** 64 - 1)
                    self._x = _x
                    self._y = _y
                    self._z = _z



class DwarfStar(Star):

    def __init__(self):
        Star.__init__(self)
        rangeOfPlanet = random.randint(8, 15)
        goldilockZoneMin = 30
        goldilockZoneMax = 90
        self.lifeChance = 0.0006
        self.numberPlanets = rangeOfPlanet
        self.goldilockZoneMin = goldilockZoneMin
        self.goldilockZoneMax = goldilockZoneMax
        self.reCharge = 2**20
        self.PlanetList = []



class MediumStar(Star):

    def __init__(self):
        Star.__init__(self)
        rangeOfPlanet = random.randint(2, 9)
        goldilockZoneMin = 60
        goldilockZoneMax = 140
        self.lifeChance = 0.0005
        self.numberPlanets = rangeOfPlanet
        self.goldilockZoneMin = goldilockZoneMin
        self.goldilockZoneMax = goldilockZoneMax
        self.reCharge = 2**30
        self.PlanetList = []


class GiantStar(Star):

    def __init__(self):
        Star.__init__(self)
        rangeOfPlanet = random.randint(5, 10)
        goldilockZoneMin = 100
        goldilockZoneMax = 250
        self.lifeChance = 0.0009
        self.numberPlanets = rangeOfPlanet
        self.goldilockZoneMin = goldilockZoneMin
        self.goldilockZoneMax = goldilockZoneMax
        self.reCharge = 2**25
        self.PlanetList = []




