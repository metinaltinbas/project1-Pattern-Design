import random
from Universe import *

class Probe():

    def __init__(self):
        _x = random.randint(2 ** 3, 2 ** 64 - 1)
        _y = random.randint(2 ** 3, 2 ** 64 - 1)
        _z = random.randint(2 ** 3, 2 ** 64 - 1)

        self._x = _x
        self._y = _y
        self._z = _z

        initialCoordinates = [_x,_y,_z]

        self.fuel = 10**22
        self.coordinateList = [initialCoordinates]
        self.idOfPlanets = []
        self.totalDistance = 0
        self.numberOfStarsVisited = 0
        self.numberOfPlanetsExplored = 0

    def printProbeFindingsLife(self,list, i, x):
        print ("Your origin was ", self.coordinateList[0])
        print ("Traveled", self.totalDistance, "miles")
        print ("\t", "You have", self.fuel, " fuel remaining.")
        print ("\t", "Visited", self.numberOfStarsVisited, " Stars.")
        print ("\t", "Explored", self.numberOfPlanetsExplored, " Planets.")
        print ("Found life on planet", list[i].PlanetList[x].identifier, list[i].PlanetList[x].planetNumber)

    def printProbeFindingsFuel(self):
        print("Fuel is not enough")
        print ("Your origin was ", self.coordinateList[0])
        print ("Traveled", self.totalDistance, " miles")
        print ("\t", "You have", self.fuel, " fuel remaining.")
        print ("\t", "Visited", self.numberOfStarsVisited, " Stars.")
        print ("\t", "Explored", self.numberOfPlanetsExplored, " Planets.")


    def nextStar(self,list):
        for i in range(len(list)):
            y = self.fuel - list[i].probeDistant
            if(list[i].isVisited==False):
                    if (y > 0):
                        self._x = list[i]._x
                        self._y = list[i]._y
                        self._z = list[i]._z
                        Coordinates = [self._x, self._y, self._z]
                        self.coordinateList.append(Coordinates)
                        self.idOfPlanets.append(list[i].PlanetList)
                        self.totalDistance += list[i].probeDistant
                        self.numberOfStarsVisited +=1
                        self.fuel -= list[i].probeDistant
                        self.fuel += list[i].reCharge
                        list[i].isVisited = True
                        for x in range(len(list[i].PlanetList)):
                            self.numberOfPlanetsExplored += 1
                            self.fuel -= list[i].PlanetList[x].distance * 2
                            self.totalDistance += list[i].PlanetList[x].distance *2
                            self.fuel += list[i].reCharge
                            if list[i].PlanetList[x].isLife==True:
                                dist = ((self._x - Coordinates[0]) ** 2 + (
                                        self._y - Coordinates[1]) ** 2 + (
                                                self._z - Coordinates[2]) * 2) ** 0.5
                                if (self.fuel>dist):
                                    self.totalDistance += dist
                                    self.fuel -= dist
                                    # print ("Your origin was ", self.coordinateList[0])
                                    # print ("Traveled", self.totalDistance, "miles")
                                    # print ("\t", "You have",self.fuel," fuel remaining.")
                                    # print ("\t", "Visited",self.numberOfStarsVisited, " Stars.")
                                    # print ("\t", "Explored", self.numberOfPlanetsExplored, " Planets.")
                                    # print ("Found life on planet",list[i].PlanetList[x].identifier,list[i].PlanetList[x].planetNumber)
                                    self.printProbeFindingsLife(list,i,x)

                                    return True
                                else:
                                    print("Probe couldn't return the origin after finding life on a planet.")
                        break
                    else:
                        self.printProbeFindingsFuel()
                        # print("Fuel is not enough")
                        # print ("Your origin was ",self.coordinateList[0])
                        # print ("Traveled", self.totalDistance," miles")
                        # print ("\t", "You have", self.fuel, " fuel remaining.")
                        # print ("\t", "Visited", self.numberOfStarsVisited, " Stars.")
                        # print ("\t", "Explored", self.numberOfPlanetsExplored, " Planets.")
                        return True




