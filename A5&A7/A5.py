import numpy as np
import cv2
import imutils

#read image and convert image to gray
image = cv2.imread("0.png")
print("IMAGE",image.shape)
copy = cv2.imread("0.png")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

# print(ret)
# print(thresh)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(image, contours, 3, (0,255,0),3)

cv2.drawContours(copy, contours, -1, (0, 0, 255), 3)
cv2.imwrite("test.png", copy)
cv2.waitKey(0)
cv2.waitKey(10)

for c in contours:
    print("area is:", cv2.contourArea(c))
#initialize region variables to store ratios
reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8, reg9 = 0,0,0,0,0,0,0,0,0

#break up the image
height = len(grayImage)
width = len(grayImage[0])
print(height,width)

regionHeight = height//3 -10
regionWidth = width//3 -10
print(regionHeight, regionWidth)
startX = 0
startY = 0
endX = regionHeight
endY = regionWidth
print(grayImage)
regions = []
flag = False
while(flag == False):

    for i in range(0,3):
        # startX = 0
        # endX = regionHeight
        for j in range(0,3):
            black = 0
            white = 0
            print(startX,startY)
            
            for k in range(startX,endX):
                for x in range(startY, endY):
                    # print(x,k)
                    
                    if(grayImage[k][x] == 255):
                        white+=1
                    else:
                        black+=1
            try:
                ratio = black/white
            except:
                ratio = 255
            regions.append(ratio)
            startY+=regionWidth
            endY+=regionWidth
            # print(startX,startY)
        startX+=regionHeight
        endX+=regionHeight
        startY= 0
        endY=regionWidth
    flag = True
print(regions)


# #calculate x parameters
# incx = width//3
# b1x = width//3
# if (width%3) == 0:
#     b1x -=1
# b2x = b1x+incx
# b3x = b2x+incx

# #calculate y parameters
# incy = height//3
# b1y = height//3
# if (height%3) == 0:
#     b1y -=1
# b2y = b1y+incy
# b3y = b2y+incy

#initialize min and max variables
# minimum = int(grayImage[0,0])
# maximum = int(grayImage[0,0])

# #loop through height and width of image and update min and max variables
# for i in range(height):
#     for j in range(width):
#         if int(grayImage[i,j]) > maximum:
#             maximum = grayImage[i,j]
#         if int(grayImage[i,j]) < minimum:
#             minimum = grayImage[i,j]

# #calculate the median level
# median = (maximum + minimum) / 2

# for i in range(height):
#     for j in range(width):
#         if int(grayImage[i,j]) > median:
#             grayImage[i,j] = 255
#         else:
#             grayImage[i,j] =0
#-----------------------------------------------------------------------------------
#loop through image and checking pixel values, update the black and white counters
#update the region ratio based on black and white counters after the loop iterations
#repeat for all regions
#-----------------------------------------------------------------------------------

# #REGION 1
# black = 0
# white = 0
# for i in range(0, b1y+1):
#     for j in range(0,b1x+1):

#         if grayImage[i,j] == 0:
#             black+=1
#         else:
#             white+=1
# try:
#     reg = black/(white)
# except:
#     reg = 255
# #REGION 2
# black = 0
# white = 0
# for i in range(0, b1y+1):
#     for j in range(b1x+1,b2x+1):

#         if grayImage[i,j] == 0:
#             black+=1
#         else:
#             white+=1
# try:
#     reg2 = black/(white)
# except:
#     reg2 = 255

# #REGION 3
# black = 0
# white = 0
# for i in range(0, b1y+1):
#     for j in range(b2x+1,b3x+1):

#         if grayImage[i,j] == 0:
#             black+=1
#         else:
#             white+=1
# try:
#     reg3 = black/(white)
# except:
#     reg3 = 255
# #REGION 4
# black = 0
# white = 0
# for i in range(b1y+1, b2y+1):
#     for j in range(0,b1x+1):

#         if grayImage[i,j] == 0:
#             black+=1
#         else:
#             white+=1
# try:
#     reg4 = black/(white)
# except:
#     reg4 = 255
# #REGION 5
# for i in range(b1y+1, b2y+1):
#     for j in range(b1x+1,b2x+1):

#         if grayImage[i,j] == 0:
#             black+=1
#         else:
#             white+=1
# try:
#     reg5 = black/(white)
# except:
#     reg5 = 255
# #REGION 6
# black = 0
# white = 0
# for i in range(b1y+1,b2y+1):
#     for j in range(b2x+1,b3x+1):

#         if grayImage[i,j] == 0:
#             black+=1
#         else:
#             white+=1
# try:
#     reg6 = black/(white)
# except:
#     reg6 = 255

# #REGION 7
# black = 0
# white = 0
# for i in range(b2y+1, b3y+1):
#     for j in range(0,b1x+1):

#         if grayImage[i,j] == 0:
#             black+=1
#         else:
#             white+=1
# try:
#     reg7 = black/(white)
# except:
#     reg7 = 255
# #REGION 8
# white = 0
# black = 0
# for i in range(b2y+1, b3y+1):
#     for j in range(b1x+1,b2x+1):

#         if grayImage[i,j] == 0:
#             black+=1
#         else:
#             white+=1
# try:
#     reg8 = black/(white)
# except:
#     reg8 = 255
# #REGION 9
# black = 0
# white = 0
# for i in range(b2y+1, b3y+1):
#     for j in range(b2x+1, b3x+1):

#         if grayImage[i,j] == 0:
#             black+=1
#         else:
#             white+=1
# try:
#     reg9 = black/(white)
# except:
#     reg9 = 255
# #construct the feature vector and clean output by rounding to 3 decimal places
# featureVector = [round(reg1,3),round(reg2,3),round(reg3,3),round(reg4,3),round(reg5,3),round(reg6,3),round(reg7,3),round(reg8,3),round(reg9,3)]
# print(featureVector)
# cv2.imshow("brown",grayImage)
# cv2.imwrite("output.png", grayImage)
# cv2.waitKey(0)

#-----UPDATES-----
#changed the region ratios from region = black/white to region = (white+black)
#updated feature vector to round all region values