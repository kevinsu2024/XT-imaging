# Canny edge detection for images
#
# Author: Kevin Su

# Library imports
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Location of image to be read 
directory = 'images/image1.png'
# Image to be analyzed
img = cv.imread(directory, cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# Analyzed edges
edges = cv.Canny(img,100,200)

# Plot edges against original image
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()