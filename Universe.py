import random
from Star import *
from Planet import *

class Universe():

    def __init__(self,numberOfStars):

        self.totalStar = numberOfStars
        self.StarList = []

        self.dwarfStartRockyPlanetCount = 0
        self.dwarfStartGaseousPlanetCount = 0
        self.dwarfStartHabitablePlanetCount = 0
        self.dwarfIntelligentLifeCount = 0


        self.giantStartRockyPlanetCount = 0
        self.giantStartGaseousPlanetCount = 0
        self.giantStartHabitablePlanetCount = 0
        self.giantIntelligentLifeCount = 0


        self.mediumStartRockyPlanetCount = 0
        self.mediumStartGaseousPlanetCount = 0
        self.mediumStartHabitablePlanetCount = 0
        self.mediumIntelligentLifeCount = 0

    def generateStars(self):
        self.giantStar=0
        self.dwarfStar=0
        self.mediumStar=0
        for i in range(self.totalStar):
            x = random.randint(0, 2)
            if x == 0:
                a = GiantStar()
                a.coordinateControl(self.StarList)
                self.StarList.append(a)
                y = random.randint(0, 2)
                for i in range (a.numberPlanets):
                    if y == 0:
                        r = RockyPlanet()
                        a.PlanetList.append(r)
                        self.giantStartRockyPlanetCount+=1

                    elif y == 1:
                        g = GaseousPlanet()
                        a.PlanetList.append(g)
                        self.giantStartGaseousPlanetCount+=1

                    elif y == 2:
                        h = HabitablePlanet()
                        if random.randint(0, 10000) < a.lifeChance*10000:
                            if (h.distance<a.goldilockZoneMax and h.distance>a.goldilockZoneMin):
                                h.isLife=True
                                self.giantIntelligentLifeCount+=1
                        a.PlanetList.append(h)
                        self.giantStartHabitablePlanetCount+=1

                self.giantStar+=1

            elif x ==1:
                b =DwarfStar()
                b.coordinateControl(self.StarList)
                self.StarList.append(b)
                y = random.randint(0, 2)
                for i in range(b.numberPlanets):
                    if y == 0:
                        r = RockyPlanet()
                        b.PlanetList.append(r)
                        self.dwarfStartRockyPlanetCount+=1

                    elif y == 1:
                        g = GaseousPlanet()
                        b.PlanetList.append(g)
                        self.dwarfStartGaseousPlanetCount+=1

                    elif y == 2:
                        h = HabitablePlanet()
                        if random.randint(0, 10000) < b.lifeChance*10000:
                            if (h.distance<b.goldilockZoneMax and h.distance>b.goldilockZoneMin):
                                h.isLife=True
                                self.dwarfIntelligentLifeCount+=1
                        b.PlanetList.append(h)
                        self.dwarfStartHabitablePlanetCount+=1

                self.dwarfStar+=1

            elif x ==2:
                c = MediumStar()
                c.coordinateControl(self.StarList)
                self.StarList.append(c)
                y = random.randint(0, 2)
                for i in range(c.numberPlanets):
                    if y == 0:
                        r = RockyPlanet()
                        c.PlanetList.append(r)
                        self.mediumStartRockyPlanetCount+=1

                    elif y == 1:
                        g = GaseousPlanet()
                        c.PlanetList.append(g)
                        self.mediumStartGaseousPlanetCount+=1

                    elif y == 2:
                        h = HabitablePlanet()
                        if random.randint(0, 10000) < c.lifeChance*10000:
                            if (h.distance<c.goldilockZoneMax and h.distance>c.goldilockZoneMin):
                                h.isLife = True
                                self.mediumIntelligentLifeCount+=1

                        c.PlanetList.append(h)
                        self.mediumStartHabitablePlanetCount+=1

                self.mediumStar+=1


    def printUniverse(self):
        print ("Total number of stars in my universe",self.totalStar)
        print ("There are",self.giantStar ,"Giant Stars with:")
        print ("\t",self.giantStartGaseousPlanetCount," Gaseous Planets")
        print ("\t",self.giantStartRockyPlanetCount," Rocky Planets")
        print ("\t",self.giantStartHabitablePlanetCount," Habitable Planets")
        print ("\t",self.giantIntelligentLifeCount," Planets with Intelligent Life")

        print ("There are",self.dwarfStar ,"Dwarf Stars with:")
        print ("\t", self.dwarfStartGaseousPlanetCount, " Gaseous Planets")
        print ("\t", self.dwarfStartRockyPlanetCount, " Rocky Planets")
        print ("\t", self.dwarfStartHabitablePlanetCount, " Habitable Planets")
        print ("\t",self.dwarfIntelligentLifeCount," Planets with Intelligent Life")


        print  ("There are",self.mediumStar ,"Medium Stars with:")
        print ("\t", self.mediumStartGaseousPlanetCount, " Gaseous Planets")
        print ("\t", self.mediumStartRockyPlanetCount, " Rocky Planets")
        print ("\t", self.mediumStartHabitablePlanetCount, " Habitable Planets")
        print ("\t",self.mediumIntelligentLifeCount," Planets with Intelligent Life")




