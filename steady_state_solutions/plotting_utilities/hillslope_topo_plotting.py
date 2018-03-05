# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:24:55 2017

@author: Charlie

Script to plot topography for 10 row x 100 column grid, for EMS hillslope tests

*assumes there is a variable called "topo" that is topographic__elevation
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import ticker
#plotting param
matplotlib.rcParams.update({'font.size': 20})

# #instantiate figure and plot
topo_fig = plt.figure(figsize=(6, 3.75))
t1 = plt.subplot()
topo = topo.reshape(10,100)
ts1_plot = t1.imshow(topo[::-1], cmap='terrain', vmin = 0, vmax = 50)

#add colorbar
cb = plt.colorbar(ts1_plot, label = 'Elevation [m]')

#axis labels
t1.tick_params(labelbottom='off', labelleft='off') 
t1.set_ylabel('100 m side length', labelpad = 15)
t1.set_xlabel('1 km side length', labelpad = 15)

#save figure
topo_fig.savefig('linear_diffusion_topo.eps',bbox_inches='tight', dpi=300)

