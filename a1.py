import numpy as np
from PIL import Image

#photo = input("Enter file name:")


def addBorder(imgArr):
    width, height = imgArr.shape
    temp = np.array([[0 for x in range(height + 2)] for y in range(width + 2)]).astype('int8')
    
    for i in range(1, width-1):
        for j in range(1,height-1):
            t = imgArr[i][j]
            temp[i+1][j+1] = t
    return temp

def convolution(kernel, imgArr):
    tmpArr = imgArr
    width, height = imgArray.shape
    outArr = imgArr
    for i in range(0, width):
        for j in range(0, height):
            outArr[i][j] = (kernel[0][0] * tmpArr[i][j]) + (kernel[0][1] * tmpArr[i][j + 1]) + (kernel[0][2] * tmpArr[i][j + 2]) + \
                       (kernel[1][0] * tmpArr[i + 1][j]) + (kernel[1][1] * tmpArr[i + 1][j + 1]) + (kernel[1][2] * tmpArr[i + 1][j + 2]) + \
                       (kernel[2][0] * tmpArr[i + 2][j]) + (kernel[2][1] * tmpArr[i + 2][j + 1]) + (kernel[2][2] * tmpArr[i + 2][j + 2])


    return outArr

def black_white(imgArr):
    width, height = imgArray.shape
    outArr = imgArr
    for i in range(0, width):
        for j in range(0, height):
            if(outArr[i][j] > 127):
                outArr[i][j] = 255
            else:
                outArr[i][j] = 0
    return outArr



 ######  MAIN  ######   
img = Image.open("pepe.png")

imgArray = np.array(img)
print(imgArray.shape)
width, height = imgArray.shape


kernel = [[-1,-1,-1],[-1,8,-1], [-1,-1,-1]] #KERNEL, IM DUMMY THICC
outArr = black_white(imgArray)

# temp = addBorder(imgArray)
# outArr = convolution(kernel, temp)

output = Image.fromarray(outArr, 'L')
output.save("output.png")



#outArr = convolution(kernel, imgArray)

