# Kevin Thompson
# DSC 430
# Nov 13 2023
# I have not given or received any unauthorized assistance on this assignment.”
# Video Link: https://youtu.be/tGFKZKJwI58


import matplotlib.pyplot as plt
import random
import numpy as np



def salt_n_pepper(img, p):
    """This function takes an image and degrades it with random black and white dots"""
    #img = plt.imread("Depaul.jpg")
    png = plt.imread(img)
    img_copy = png.copy()
    red = img_copy[:, :, 0]
    width = img_copy.shape[0]
    height = img_copy.shape[1]
    for x in range(width):
        for y in range(height):
            chance = random.random()
            if chance < p/2: #create white pixels
                img_copy[x,y,0]= 255
                img_copy[x, y, 1:] = 255
                img_copy[x, y, 2:] = 255
            elif p /2 < chance <= p: #create black pixels
                img_copy[x, y, 0] = 0
                img_copy[x, y, 1:] = 0
                img_copy[x, y, 2:] = 0
    plt.imshow(img_copy)
    plt.show()

##################################################################################################################

"""Final functions used for assignment: """


def salt_n_pepper_test(img, p):
    """This function will take an image and degrade it with salt and pepper based on the percent chance thats input"""
    #img = plt.imread("Depaul.jpg")
    png = plt.imread(img) #read the file
    img_copy = png.copy() #turn the file into a copy
    red = img_copy[:, :, 0] #set only to red channel
    width = red.shape[0] #create a variable for the x axis
    height = red.shape[1] #create a variable for the y axis
    for x in range(width): #iterate throughh the matrix of the image
        for y in range(height):
            chance = random.random()
            if chance <= p: #create white pixels # if our random number is less than or equal to the % input
                red[x,y]= 0 #make this pixel black

    plt.imshow(red, cmap='gray') #plot with grayscale
    plt.show()

    return red


def median_filter(img, w):
    """This function will median filter an image by w x w pixels"""
    width = img.shape[0]  # create a variable for the x axis
    height = img.shape[1]  # create a variable for the y axis
    for x in range(0 , width , w): #iterate throw x axis
        for y in range(0 , height, w): #iterate through y axis
            img[x:x+w,y:y+w] = np.median(img[x:x+w,y:y+w])  #build a square of l, w = w
    plt.imshow(img, cmap = 'gray')
    plt.show()


def main():
    """This function will do the homework examples"""

    median_filter(salt_n_pepper_test("Depaul.jpg", .7), 2)
    median_filter(salt_n_pepper_test("Depaul.jpg", .7), 4)
    median_filter(salt_n_pepper_test("Depaul.jpg", .7), 9)
    median_filter(salt_n_pepper_test("Depaul.jpg", .25), 2)
    median_filter(salt_n_pepper_test("Depaul.jpg", .25), 6)
    median_filter(salt_n_pepper_test("Depaul.jpg", .25), 5)

main()
