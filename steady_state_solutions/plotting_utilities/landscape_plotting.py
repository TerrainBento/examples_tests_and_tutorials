# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:02:26 2017

@author: Charlie Shobe

Plotting script for landscapes for EMS steady-state runs

Assumes the existence of a variable "topo" which is just final topography.
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
topo = topo.reshape(100,160)
ts1_plot = t1.imshow(topo[::-1], cmap='terrain', vmin = 0, vmax = 50)

#add colorbar
cb = plt.colorbar(ts1_plot, label = 'Elevation [m]')

#axis labels
t1.tick_params(labelbottom='off', labelleft='off') 
t1.set_ylabel('1 km side length', labelpad = 15)
t1.set_xlabel('1.6 km side length', labelpad = 15)

#save figure
topo_fig.savefig('basic_streampower_topo.eps',bbox_inches='tight', dpi=300)