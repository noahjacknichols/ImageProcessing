import numpy as np
from PIL import Image


def connectedComponent(imgarr):
    equivList = [].append(0)

    width, height = imgarr.shape()
    for i in range(height):
        for j in range(width):
            if(imgarr[i][j] == 0):
                x = 0
                y = 0
                if(i != 0):
                    #check up
                    if(imgarr[i-1][j] != 255):
                        x = imgarr[i-1][j]
                if(j != 0):
                    #check left
                    if(imgarr[i][j-1] != 255):
                        y = imgarr[i][j-1]
                    
                if(x == 0 and y == 0):
                    #neither of the above conditions were met 
                    equivList.append(len(equivList))
                    imgarr[i][j] = equivList[len(equivList)-1]
                else:
                    #we know one of the up or left pixels wasn't white, conditions met
                    lowest = x if y > x else y
                    equivList[x] = lowest
                    equivList[y] = lowest
                    imgarr[i][j] = lowest

    for i in range(height):
        for j in range(width):
            if(imgarr[i][j] != 255):
                x = imgarr[i][j]
                imgarr[i][j] = imgarr[i][j] if equivList[x] >= imgarr[i][j] else equivList[x]

    equivCount = [0]
    temp = []

    for p in range(1,len(equivList)):
        equivCount.append(0)
    for i in range(height):
        for j in range(width):
            if(imgarr[i][j] != 255 and imgarr[i][j] != 0):
                equivCount[imgarr[i][j]] +=1

    for i in range(1,len(equivCount) +1):
        sum = 0
        for j in range(1,len(equivCount) + 1):
            if(i == equivList[j]):
                sum += equivCount[i]
        if(sum > 0):
            temp.append(sum)

    return temp

