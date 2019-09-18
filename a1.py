import numpy as np
from PIL import Image

#photo = input("Enter file name:")
img = Image.open("pepe.png")

imgArray = np.array(img)
print(imgArray.shape)

# print(width)
# print(height)


def convolution(kernel, temp, arr):

    width, height = imgArray.shape
    temp = np.array([[0 for x in range(height + 2)] for y in range(width + 2)]).astype('int8')


    return outArr






kernel = [[-1,-1,-1],[-1,5,-1], [-1,-1,-1]] #KERNEL, IM DUMMY THICC



outArr = convolution(kernel, imgArray)

