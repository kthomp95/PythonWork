# Kevin Thompson
# DSC 430
# Oct 24 2023
# A0701
# I have not given or received any unauthorized assistance on this assignment.”
# Video Link:https://youtu.be/XX3_zGJZCIQ

def intro():
    """Prints the purpose of the program as an introduction"""
    # print("The purpose of this program is to make Pseudo random numbers using war and peace")


def main_2():
    """The purpose of this program is to make 10,000 Pseudo random numbers using war and peace"""
    intro()
    psuedoList = []
    sum = 0
    for i in range(100, 10100):
        prng = WarAndPeacePseudoRandomNumberGenerator(i, 100, 32)
        psuedoList.append(prng.random())
    print(psuedoList)
    print("The max is :", max(psuedoList))
    print("The min is: ", min(psuedoList))
    for i in psuedoList:
        sum += i
    print("The mean is: ", sum / 10000)
    return psuedoList


class WarAndPeacePseudoRandomNumberGenerator:
    """Object for creating random numbers using war and peace"""

    def __init__(self, seed, step, steps):
        self.seed = seed
        self.step = step
        self.steps = steps

    def random(self):
        """this function will return a lists of 0s and 1s based on whether or not 2 characters in a book are greater than one another. It will start at a seed given, and check characters by a step given for a number of times given"""
        stepCounter = 0  # variable initialized to 0 to count steps
        numberList = []  # empty set to store the scores
        infile = open("war-and-peace.txt", "rb")
        infile.seek(self.seed)  # set cursor to the seed
        x = infile.read(1)  # read only the first character
        position = str(x)[2]  # change character from byte to string

        while stepCounter < self.steps:
            stepCounter += 1  # add step
            self.seed += self.step  # get ready to move cursor a step
            ch1 = position  # ch1 is the current position
            infile.seek(self.seed)  # move cursor
            x = infile.read(1)
            position = str(x)[2]
            ch2 = position  # ch2 is current position

            self.seed += self.step  # get ready to move cursor
            infile.seek(self.seed)  # move cursor
            x = infile.read(1)
            position = str(x)[2]

            if ch1 > ch2:
                b = 1  # add 1 to list if ch1 greater than ch2
                numberList.append(b)
            elif ch1 == ch2:
                stepCounter -= 1  # if values are the same we want to basically redo so just bring counter back 1
            else:
                b = 0
                numberList.append(b)
        x = 1  # set x = 1 to create 1/2,1/4,1/8 etc with
        r = 0  # this will be our random number
        for i in range(1, 33):
            for i in numberList:
                y = 2 ** x  # denominator
                x += 1  # increase x by one for the next number
                z = 1 / y  # compute fraction
                r += z * i  # add to r
        return r


main_2()


# the following functions were made independently first because I didn't read that we needed to make an object
# but ill just keep them here for my own notes basically

def main():
    """The purpose of this program is to make 10,000 Pseudo random numbers using war and peace"""
    intro()
    psuedoList = []
    sum = 0
    for i in range(1500000, 20000000):
        psuedoList.append(calculate_r(random_number(i, 100, 32)))
    print(psuedoList)
    print("The max is: ", max(psuedoList))
    print("The min is: ", min(psuedoList))

    for i in psuedoList:
        sum += i
    print("The mean is: ", sum / 10000)


def random_number(seed, step, steps):
    """this function will return a lists of 0s and 1s based on whether or not 2 characters in a book are greater than one another. It will start at a seed given, and check characters by a step given for a number of times given"""
    stepCounter = 0  # variable initialized to 0 to count steps
    numberList = []  # empty set to store the scores
    infile = open("war-and-peace.txt", "rb")
    infile.seek(seed)  # set cursor to the seed
    x = infile.read(1)  # read only the first character
    position = str(x)[2]  # change character from byte to string

    while stepCounter < steps:
        stepCounter += 1  # add step
        seed += step  # get ready to move cursor a step
        ch1 = position  # ch1 is the current position
        infile.seek(seed)  # move cursor
        x = infile.read(1)
        position = str(x)[2]
        ch2 = position  # ch2 is current position

        seed += step  # get ready to move cursor
        infile.seek(seed)  # move cursor
        x = infile.read(1)
        position = str(x)[2]

        if ch1 > ch2:
            b = 1  # add 1 to list if ch1 greater than ch2
            numberList.append(b)
        elif ch1 == ch2:
            stepCounter -= 1  # if values are the same we want to basically redo so just bring counter back 1
        else:
            b = 0
            numberList.append(b)

    x = 1  # set x = 1 to create 1/2,1/4,1/8 etc with
    r = 0  # this will be our random number
    for i in range(1, 33):
        for i in numberList:
            y = 2 ** x  # denominator
            x += 1  # increase x by one for the next number
            z = 1 / y  # compute fraction
            r += z * i  # add to r
    return r


def calculate_r(numberList):
    """Takes a list of numbers and divides them by 1/(2^(n+1)) for n in range 0-32"""
    x = 1  # set x = 1 to create 1/2,1/4,1/8 etc with
    r = 0  # this will be our random number
    for i in range(1, 33):
        for i in numberList:
            y = 2 ** x  # denominator
            x += 1  # increase x by one for the next number
            z = 1 / y  # compute fraction
            r += z * i  # add to r
    return r
