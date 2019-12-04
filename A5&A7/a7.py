import cv2 as cv
import numpy as np
import math
import A5 as fv

#euclidean distance function
def euclideanDistance(v1, v2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(v1, v2)]))

#open image and vector file
v1 = fv.featureVector('0.png')
vecFile = open('FeatureVectors.txt', 'r')

#read lines in feature vector file and compare
distance = []
for line in vecFile:
    line = line.strip()
    v2 = line.split(',')
    for i in range(len(v2)):
        v2[i] = float(v2[i])
    distance.append(euclideanDistance(v1, v2))

vecFile.close()
print(distance)
print(distance.index(min(distance)))