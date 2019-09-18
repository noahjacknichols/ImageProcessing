import numpy as np
from PIL import Image

#photo = input("Enter file name:")
img = Image.open("pepe.png")

imgArray = np.array(img)
print(imgArray.shape)

# print(width)
# print(height)

