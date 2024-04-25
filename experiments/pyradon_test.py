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
img = cv.resize(img, (512,512), interpolation=cv.INTER_AREA)
transformed_img = np.zeros((1,512,512))
for i in range(len(transformed_img)):
    transformed_img[i,:,:] = img


"""This is the start of example streaks"""

s = Simulator()
# s.debug_bit = 2
""" End of example"""


s.finder.pars.use_exclude = False
s.finder.pars.use_subtract_mean = True
s.finder.pars.use_short = True
s.finder.pars.min_length = 1
s.finder.pars.num_iterations = 1
s.finder.pars.verbosity = 100
s.finder.pars.use_show = False #flip to true if you want to see how the streaks are generated

for i in range(transformed_img.shape[0]): 
    s.finder.input(transformed_img[i,:,:], psf=0, variance=0) # note the psf is given as width sigma, and variance of the noise we used. 
    print(f'Frame= {i} | Best S/N= {s.finder.data.best_snr}')

plt.figure()
plt.imshow(img)

for i in range(len(s.finder.streaks_all)):
    s.finder.streaks_all[i].print()
    streak = s.finder.streaks_all[i]
    offset = 1
    plt.plot([streak.x1-offset, streak.x2-offset], [streak.y1,streak.y2], lw=1, ls='--', color='red')
    plt.plot([streak.x1+offset, streak.x2+offset], [streak.y1,streak.y2], lw=1, ls='--', color='red')
plt.style.use('grayscale')
plt.colorbar()
plt.show()
