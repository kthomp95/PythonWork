# Kevin Thompson
# DSC 430
# Nov 13 2023
# I have not given or received any unauthorized assistance on this assignment.”
# Video Link: https://youtu.be/WfJEXUTJ_Gk

import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

def main():
    """This function will use the other functions to organize this program for the assignment"""
    print("This program is designed to compare the distance between planet objects in our solar system at different days in"
          "the planets' year cycle.")

    print("The distance between earth and mars on day 732 is: ",distance(earth, mars, 732))


    print("We will simulate 1000 years of data: and check to see if the final matrix is symmetric:  ")
    if (symmetryCheck(simulationYears())) == True:
        print("The matrix is symmetric")
    else:
        print("The matrix is not symmetric")

    print("Next we plot clean data of 1000 days: ")
    simulationClean()

    print("Next is the same data made with noise: ")
    simulationNoisy()

    print("Next the same simulation with different noise amounts: ")
    simulationNewNoise()



class Planet:
    """Class planet takes distance from sun and length of year"""

    def __init__(self, r, length):
        self.r = r
        self.length = length

    def position(self, day):
        """This function will take a day and calculate the position of the planet through its orbit in x,y coordinates"""
        percComplete = day / self.length  # calculate percent of year complete
        angle = 360 * percComplete  # calculate angle
        xCord = round(self.r * (math.cos(math.radians(angle))), 2)  # calculate x coord
        yCord = round(self.r * (math.sin(math.radians(angle))), 2)  # calculate y coord
        coordList = []  # use list for x,y format
        coordList.append(xCord)
        coordList.append(yCord)
        return coordList  # return coordinate position as list


# create object for each planet

mercury = Planet(3.5, 88)
venus = Planet(6.7, 225)
earth = Planet(9.3, 365)
mars = Planet(14.2, 687)
jupiter = Planet(48.4, 4333)
saturn = Planet(88.9, 10759)
uranus = Planet(179, 30687)
neptune = Planet(288, 60190)


# mercury.position(33)

def distance(p1, p2, day):
    """this function will find the distance between two planet objects with position based on the day"""
    d = math.sqrt((p2.position(day)[0] - p1.position(day)[0]) ** 2 + (p2.position(day)[1] - p1.position(day)[1]) ** 2)
    return d





def simulationClean():
    """simulates 1000 days and computes distances between objects and then plots the data as a time series"""
    exact = {} #Empty dictionary to make DF

    for i in range(1000): #simulate 1000 days
        d1 = distance(earth, mercury, i) #compute distance
        d2 = distance(earth, venus, i)
        d3 = distance(earth, mars, i)
        exact[i] = d1, d2, d3 #put each days distance in dictionary ordered by day


    exactdf = pd.DataFrame.from_dict(exact, orient='index', columns=["Mercury", "Venus", "Mars"]) #create DF
    #clean averages
    mercMean = exactdf["Mercury"].mean() #compute mean for horizontal line
    venusMean = exactdf["Venus"].mean()
    marsMean = exactdf["Mars"].mean()
    #clean plot:
    plt.plot(exactdf.index, exactdf["Mercury"], label="Mercury", c='green', alpha=.3)
    plt.plot(exactdf.index, exactdf["Venus"], label="Venus", c='blue', alpha=.3)
    plt.plot(exactdf.index, exactdf["Mars"], label="Mars", c='orange', alpha=.3)
    plt.title("Distance of Planets from Earth Throughout 1,000 Days")
    plt.xlabel('Day', fontsize=15)
    plt.ylabel('Distance(CM)', fontsize=15)
    plt.legend(loc="upper right")
    plt.axhline(mercMean, linestyle='--', c='green', lw=2.5)
    plt.axhline(venusMean, linestyle='--', c='blue', lw=2.5)
    plt.axhline(marsMean, linestyle='--', c='orange', lw=2.5)
    plt.show()


def simulationNoisy():
    """Simulates 1000 years of noisy planet position data and plots it"""
    noise = {} #empty dictionary to make DF from
    stdPrep = [] #empty list to compute moving STD
    # noisy data:
    for i in range(1000): #simulate 1000 days
        d1n = distance(earth, mercury, i) #compute distance on a given day
        d2n = distance(earth, venus, i)
        d3n = distance(earth, mars, i)
        stdPrep.append(d1n) #put distances in list to get STD
        stdPrep.append(d2n)
        stdPrep.append(d3n)

        # create dynamic std
        noiseFactor = np.std(stdPrep) #compute STD of distances
        noise[i] = noiseFactor * random.random() * d1n, noiseFactor * random.random() * d2n, noiseFactor * random.random() * d3n #make data noisy based on STD

    # create dataframe
    noisedf = pd.DataFrame.from_dict(noise, orient='index', columns=["Mercury", "Venus", "Mars"]) #create dataframe

    # noisy averages
    mercMean = noisedf["Mercury"].mean() #compute averages for horizontal line
    venusMean = noisedf["Venus"].mean()
    marsMean = noisedf["Mars"].mean()

    # noisy plot:
    plt.plot(noisedf.index, noisedf["Mercury"], label="Mercury", c='green', alpha=.3)
    plt.plot(noisedf.index, noisedf["Venus"], label="Venus", c='blue', alpha=.3)
    plt.plot(noisedf.index, noisedf["Mars"], label="Mars", c='orange', alpha=.3)
    plt.title("Distance of Planets from Earth Throughout 1,000 Days -- noisy")
    plt.xlabel('Day', fontsize=15)
    plt.ylabel('Distance(CM)', fontsize=15)
    plt.legend(loc="upper right")
    plt.axhline(mercMean, linestyle='--', c='green', lw=2.5)
    plt.axhline(venusMean, linestyle='--', c='blue', lw=2.5)
    plt.axhline(marsMean, linestyle='--', c='orange', lw=2.5)
    plt.show()

def simulationNewNoise():
    """This is the same as the previous function but it tries different types of noise"""
    noise = {}  # empty dictionary to make DF from
    stdPrep = []  # empty list to compute moving STD
    # noisy data:
    for i in range(1000):  # simulate 1000 days
        d1n = distance(earth, mercury, i)  # compute distance on a given day
        d2n = distance(earth, venus, i)
        d3n = distance(earth, mars, i)
        stdPrep.append(d1n)  # put distances in list to get STD
        stdPrep.append(d2n)
        stdPrep.append(d3n)

        # create dynamic std
        s = .51
        noise[i] = s * random.random() * d1n, s * random.random() * d2n, s * random.random() * d3n  # make data noisy based on STD

    # create dataframe
    noisedf = pd.DataFrame.from_dict(noise, orient='index', columns=["Mercury", "Venus", "Mars"])  # create dataframe

    # noisy averages
    mercMean = noisedf["Mercury"].mean()  # compute averages for horizontal line
    venusMean = noisedf["Venus"].mean()
    marsMean = noisedf["Mars"].mean()

    # noisy plot:
    plt.plot(noisedf.index, noisedf["Mercury"], label="Mercury", c='green', alpha=.3)
    plt.plot(noisedf.index, noisedf["Venus"], label="Venus", c='blue', alpha=.3)
    plt.plot(noisedf.index, noisedf["Mars"], label="Mars", c='orange', alpha=.3)
    plt.title("Distance of Planets from Earth Throughout 1,000 Days -- noisy (s = .51)")
    plt.xlabel('Day', fontsize=15)
    plt.ylabel('Distance(CM)', fontsize=15)
    plt.legend(loc="upper right")
    plt.axhline(mercMean, linestyle='--', c='green', lw=2.5)
    plt.axhline(venusMean, linestyle='--', c='blue', lw=2.5)
    plt.axhline(marsMean, linestyle='--', c='orange', lw=2.5)
    plt.show()


    #do the same simulation with a new 's'

    noise = {}  # empty dictionary to make DF from
    stdPrep = []  # empty list to compute moving STD
    # noisy data:
    for i in range(1000):  # simulate 1000 days
        d1n = distance(earth, mercury, i)  # compute distance on a given day
        d2n = distance(earth, venus, i)
        d3n = distance(earth, mars, i)
        stdPrep.append(d1n)  # put distances in list to get STD
        stdPrep.append(d2n)
        stdPrep.append(d3n)

        # create dynamic std
        s = 10
        noise[
            i] = s * random.random() * d1n, s * random.random() * d2n, s * random.random() * d3n  # make data noisy based on STD

    # create dataframe
    noisedf = pd.DataFrame.from_dict(noise, orient='index', columns=["Mercury", "Venus", "Mars"])  # create dataframe

    # noisy averages
    mercMean = noisedf["Mercury"].mean()  # compute averages for horizontal line
    venusMean = noisedf["Venus"].mean()
    marsMean = noisedf["Mars"].mean()

    # noisy plot:
    plt.plot(noisedf.index, noisedf["Mercury"], label="Mercury", c='green', alpha=.3)
    plt.plot(noisedf.index, noisedf["Venus"], label="Venus", c='blue', alpha=.3)
    plt.plot(noisedf.index, noisedf["Mars"], label="Mars", c='orange', alpha=.3)
    plt.title("Distance of Planets from Earth Throughout 1,000 Days -- noisy (s=10)")
    plt.xlabel('Day', fontsize=15)
    plt.ylabel('Distance(CM)', fontsize=15)
    plt.legend(loc="upper right")
    plt.axhline(mercMean, linestyle='--', c='green', lw=2.5)
    plt.axhline(venusMean, linestyle='--', c='blue', lw=2.5)
    plt.axhline(marsMean, linestyle='--', c='orange', lw=2.5)
    plt.show()

def simulationYears():
    """simulates 1000 years of planet movement and creates a matrix of average distance between planets"""
    exact = {} #empty dictionary to create DF
    planets = ["Mercury", "Venus", "Earth", "Mars", "jupiter", "Saturn", "Uranus", "Neptune"] #list of planet names
    counter = 0 #counter used to index the planet list
    distanceList = [] #empty list used to house all distances of the 1k year simulation to take the average of
    avgDistance = [] #empty list to store averages
    planetList = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, 0] #list of planet data
    for planet in planetList: #iterate through planets
        if len(avgDistance) != 0: #checks to see if this list has data, if so that means we've already done a planet
            exact[planets[counter - 1]] = avgDistance #creates a key of the planet, then values are all the average distances
            avgDistance = [] #resets the list of average distances for the next planet simulations
        if planet == 0: #because of how the loop is structured, we need another 9th 'planet', but we don't actually want to use it
            break
        planetCounter = 0 #initializes variable
        counter += 1 #used to move through the planet list

        while planetCounter <= 8: # run simulation for all 8 planets
            planetCounter += 1
            if len(distanceList) != 0: #checks to see if list is empty
                x = sum(distanceList) / len(distanceList) #find average of distances
                avgDistance.append(x) #put average distance into list
                distanceList = [] #reset distance list for next simulation
            for i in range(365000): #simulates 1000 years
                if planetCounter == 9: #this means we have completed the simulations
                    break
                d = distance(planet, planetList[planetCounter - 1], i) #take the distance -- but we don't want the last planet 0
                distanceList.append(d)  #add distance to distance list to be averaged later
    matrix = pd.DataFrame.from_dict(exact, orient='index', columns=planets[0:8]) #create dataframe
    print(matrix) #show matrix

    return matrix #returns matrix


def symmetryCheck(matrix):
    """checks to see if a matrix is symmetrical"""
    matrix = matrix.to_numpy()
    for i in range(len(matrix)): #will iterate through the length of the matrix
        for j in range(len(matrix)):
            if (matrix[i][j] != matrix[j][i]): #comparing opposite elements of the matrix to one another, if theyre different it is not symmetrical
                return False
    return True



main()
