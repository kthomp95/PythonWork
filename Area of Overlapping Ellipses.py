#Kevin Thompson
#DSC 430
# Oct 24 2023
#A0701
#I have not given or received any unauthorized assistance on this assignment.”
# Video Link:https://youtu.be/GsdlzUYCHaY



import a0701
import random
import math
from random import shuffle

def main():
    """this function will approximate the area of the overlap of 2 ellipses given"""
    p1 = Point(0, 0)
    p2 = Point(0, 0)
    circle1 = Ellipse(p1, p2, 2)

    p3 = Point(0, 0)
    p4 = Point(0, 0)
    circle2 = Ellipse(p3, p4, 2)
    print(overlap(circle1, circle2))

    p5 = Point(5, 3)
    p6 = Point(0, 0)
    e1 = Ellipse(p5, p6, 10)

    p7 = Point(3, 5)
    p8 = Point(0, 0)
    e2 = Ellipse(p7, p8, 8)

    print(overlap(e1, e2))

    p9 = Point(-1, -1)
    p10 = Point(1, 1)
    e3 = Ellipse(p9, p10, 6)

    p11 = Point(-3, 3)
    p12 = Point(3, -3)
    e4 = Ellipse(p11, p12, 9)

    print(overlap(e3, e4))

class Point:
    """this class is of a point on a 2d grid that is made with an x and y value"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
def distance(p1,p2):
    """This function will find the distance between two points"""
    x = p2.x - p1.x
    y = p2.y - p1.y
    distance = math.sqrt(x**2+y**2)
    return distance

class Ellipse:
    """this class makes an elipse based off of 2 points and its width"""
    def __init__(self, point1, point2, width):
        self.p1 = point1
        self.p2 = point2
        self.width = width

    def x_min(self):  # we want to find the minimum x value'd point for creating a box
        """this will find the lower x value of the two points"""
        if self.p1.x < self.p2.x:
            return self.p1.x
        elif self.p1.x > self.p2.x:
            return self.p2.x
        else:  # this will be if both points have the same x value in which case we can return either as the minimum value
            return self.p1.x

    def y_min(self):  # this will be the same idea as x min
        """this will find the lower y value of the two points"""
        if self.p1.y < self.p2.y:
            return self.p1.y
        elif self.p1.y > self.p2.y:
            return self.p2.y
        else:
            return self.p1.y

    def x_max(self):  # same as the x min/max
        """this will find the higher x value of the two points"""
        if self.p1.x < self.p2.x:
            return self.p2.x
        elif self.p1.x > self.p2.x:
            return self.p1.x
        else:
            return self.p1.x

    def y_max(self):  # same as the x min/max
        """this will find the higher y value of the two points"""
        if self.p1.y < self.p2.y:
            return self.p2.y
        elif self.p1.y > self.p2.y:
            return self.p1.y
        else:
            return self.p1.y


def make_box(e1, e2):
    """this funtion will make a box around 2 elipses"""
    if e1.width > e2.width:  # we want to use the bigger width for making the box just to be sure -- altho idk if this is necessary
        w = e1.width
    elif e1.width < e2.width:
        w = e2.width
    else:
        w = e1.width
    # b value (top of box)
    if e1.y_max() > e2.y_max():
        b = e1.y_max() + w  # create the upper y boundary of our box
    elif e1.y_max() < e2.y_max():
        b = e2.y_max() + w
    else:
        b = e1.y_max() + w
    # t value (bottom of box)
    if e1.y_min() < e2.y_min():  # this will give us the min y value of our box
        t = e1.y_min() - w
    elif e1.y_min() > e2.y_min():
        t = e2.y_min() - w
    else:
        t = e1.y_min() - w
    # r value (right end of box)
    if e1.x_max() > e2.x_max():
        r = e1.x_max() + w
    elif e1.x_max() < e2.x_max():
        r = e2.x_max() + w
    else:
        r = e1.x_max() + w
    # l value (left end of box)
    if e1.x_min() < e2.x_min():
        l = e1.x_min() - w
    elif e1.x_min() > e2.x_min():
        l = e2.x_min() - w
    else:
        l = e1.x_min() - w
    #print("xmin:",l,"xmax",r,"ymin:",t,"ymax:",b)
    return b, t, r, l





def overlap(e1, e2):
    """this function will take two ellipses, make a box around them, plot 10,000 random points in that box and see how
    many of those points will land in the overlap of the two ellipses. It then returns the ratio of points in overlap
    to total points"""
    make_box(e1, e2) #make a box around the ellipses
    randomNumbers = a0701.main_2() #make a list of random numbers
    randomNumbers2 = [] #empty list for random numbers
    counterTotal = 0 #initialize counter for total points
    counterInside = 0 #initialize counter for counting points that fall within overlap
    for i in randomNumbers:
        randomNumbers2.append(i) #fill the empty list with the same random numbers
    random.shuffle(randomNumbers2) #shuffle the new list
    for i in range(0, 10000): #create 10,000 points within the box
        point = Point(randomNumbers[i] + random.randint(make_box(e1, e2)[3], make_box(e1, e2)[2]-1),
                    randomNumbers2[i] + random.randint(make_box(e1, e2)[1], make_box(e1, e2)[0]-1)) #transform random float into random numbers that will be within the boundary of the box
        if distance(point, e1.p1) + distance(point, e1.p2) < e1.width and distance(point, e2.p1) + distance(point, e2.p2) < e2.width: #if the point is within the two ellipses
            counterInside += 1
            counterTotal += 1
        elif distance(point, e1.p1) + distance(point, e1.p2) == e1.width and distance(point, e2.p1) + distance(point, e2.p2) < e2.width: #if the point is on the boundary of one ellipse and within the other
            counterInside += 1
            counterTotal += 1
        elif distance(point, e1.p1) + distance(point, e1.p2) < e1.width and distance(point, e2.p1) + distance(point, e2.p2) == e2.width:#if the point is on the boundary of one ellipse and within the other
            counterInside += 1
            counterTotal += 1
        elif distance(point, e1.p1) + distance(point, e1.p2) == e1.width and distance(point, e2.p1) + distance(point, e2.p2) == e2.width: #if the point is on the boundary of both ellipses
            counterInside += 1
            counterTotal += 1
        else: #if the point is outside of one of the ellipses
            counterTotal += 1
    print(counterInside,'/',counterTotal,'=',counterInside/counterTotal)
    ratio = counterInside/counterTotal
    l = e1.width*2 #length of box
    w = e2.width*2 #width of box
    boxArea = l*w #area of rectangle
    overlapArea = boxArea*ratio #this should find the area by multiplying the area of the total box by the ratio of points that fell within the overlap
    #print(make_box(e1,e2))
    return overlapArea


main()


