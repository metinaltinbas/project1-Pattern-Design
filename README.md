# CS342 Design Patterns
## Fall 2018
### PROJECT 1 README FILE


# Project 1 - Searching the Stars
### Due Date: 11:59 p.m., September 28th, 2018

*All programs will be tested on the machines in the Q22 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files
* project1.py

### Grading Rubric
**Total: 47 points**
* Universe Class Requirements:
   * (2 pts) The __init__ method takes the number of stars to create
   * (2 pts) Contain a print universe method that prints required data
* Star Class Requirements:
   * (2 pts) Star Base Class with unique x, y, z coordinates in the range 2**8..2**64
   * (3 pts) Star SubClasses: DwarfStar, GiantStar, MediumStar
   * (3 pts) Each Star subtype has attributes: chances of life, number of planets (as a range), goldilocks zone, recharge amount
   * (2 pts) Stars generate and save a list of planets using the above attributes
   * (2 pts) Star Coordinates are verifiably unique
   * (2 pts) Instance variables follow python conventions for private data
* Planet Class Requirements:
   * (2 pts) Planet base class that contains distance from star
   * (4 pts) Planet SubClasses: RockyPlanet, GaseousPlanet, HabitablePlanet
   * (4 pts) Each Planet is marked with having or not having intelligent life based on star attributes and distance from star
   * (2 pts) Each planet has a unique identifier as described.
* Probe Class Requirements:
   * (3 pts) Keeps track of the requested information
   * (5 pts) Unique algorithm to determine which Star should be visited next
   * (2 pts) Has a fuel attribute that depletes during the search algorithm, and recharges using the recharge amount for each star
   * (3 pts) A print method that prints the probe’s findings.
* Submission:
   * (2 pts) Follows requested project structure and submission format
   * (2 pts) README sections complete
   * Meets the commit requirement of having 3 significant commits 24 hours apart


***


## Description


For our first assignment we are going to simulate the universe, and then search it for intelligent life. There will be two parts to this project. In Part A you will build a universe of stars and planets. Each star will have a type, an x, y, and z coordinate, and a random range of planets orbiting the star.

