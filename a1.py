import numpy as np
from PIL import Image

#photo = input("Enter file name:")
img = Image.open("pepe.png")

imgArray = np.array(img)
print(imgArray.shape)

def addBorder(imgArr):
    temp = np.array([[0 for x in range(height + 2)] for y in range(width + 2)]).astype('int8')
    width, height = imgArr.shape
    for i in range(0, width):
        for j in range(0,height):
            temp = imgArr[i][j]
            tmpArr[i+1][j+1] = temp

def convolution(kernel, imgArr):

    width, height = imgArray.shape
    temp = np.array([[0 for x in range(height + 2)] for y in range(width + 2)]).astype('int8')
    outArr = imgArr
    for i in range(0, width):
        for j in range(0, height):
            #convolution math
            print()


    return outArr



width, height = imgArray.shape


kernel = [[-1,-1,-1],[-1,5,-1], [-1,-1,-1]] #KERNEL, IM DUMMY THICC



temp = addBorder(imgArr)


outArr = convolution(kernel, imgArray)

