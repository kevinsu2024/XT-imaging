import sys
sys.path.insert(0, '../pretrained_models/pyradon/src')
from frt import FRT
from simulator import Simulator
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

# Location of image to be read 
directory = 'images/image1.png'
# Image to be analyzed
img = cv.imread(directory, cv.IMREAD_GRAYSCALE)
img = cv.resize(img, (512, 512), interpolation=cv.INTER_AREA)
print(img.shape)
transformed_img = np.zeros((1,512,512))
transformed_img[0,:,:] = img


"""This is the start of example streaks"""

s = Simulator()
s.debug_bit = 2
s.x1 = 0.375; s.x2 = 0.5; s.y1 = 0; s.y2 = 0.5;
s.run()

""" End of example"""

# print(len(f.finder.streaks))

# 


s.finder.pars.use_exclude = False
s.finder.pars.use_subtract_mean = True
s.finder.pars.use_short = True
s.finder.reset()
for i in range(transformed_img.shape[0]): 
    s.finder.input(transformed_img[i,:,:], psf=2, variance=2.5**2) # note the psf is given as width sigma, and variance of the noise we used. 
    print(f'Frame= {i} | Best S/N= {s.finder.data.best_snr}')

if len(s.finder.streaks_all):
    s.finder.streaks_all[0].print()

streak = s.finder.streaks[0]
offset = 15
plt.figure()
plt.imshow(img)
plt.plot([streak.x1-offset, streak.x2-offset], [streak.y1,streak.y2], lw=1, ls='--', color='red')
plt.plot([streak.x1+offset, streak.x2+offset], [streak.y1,streak.y2], lw=1, ls='--', color='red')
plt.colorbar()
plt.show()
