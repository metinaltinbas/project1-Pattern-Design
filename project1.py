from Universe import *
from Star import *
from Probe import Probe


def main():
    starLength= 1024
    universe = Universe(starLength)
    universe.generateStars()
    universe.printUniverse()

    print("==========")

    probe = Probe()

    # calculating probe distant to stars
    for i in range(len(universe.StarList)):
        dist = ((probe._x - universe.StarList[i]._x) ** 2 + (
                probe._y - universe.StarList[i]._y) ** 2 + (
                        probe._z - universe.StarList[i]._z) * 2) ** 0.5
        universe.StarList[i].probeDistant = dist

    universe.StarList.sort(key = lambda c: c.probeDistant) # to see which star is close to probe


    counter =1
    x = probe.nextStar(universe.StarList)

    while(counter!=starLength+1 and x!=True):
        universe.StarList.sort(key=lambda c: c.probeDistant)
        counter+=1
        x = probe.nextStar(universe.StarList)


    if(counter==1024 or x==None):
        print ("Could not find a life or there is no life at the universe.")
    pass

if(__name__ == "__main__"):
    main()