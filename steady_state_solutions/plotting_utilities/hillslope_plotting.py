# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:22:30 2017

@author: Charlie Shobe

Plotting script for hillslope topography analytical comparisons for EMS models
*assumes there is a variable called "domain" that is a 1-D array describing
distance along teh base of the topographic profile.

*assumes there is a variable called "topo" that is a 1-D array describing an
east-west topographic profile taken across the middle of the domain.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

##instantiate figure and plot
fig = plt.figure(figsize=(6, 3.75))
hillslope = plt.subplot()

#plotting param
matplotlib.rcParams.update({'font.size': 20})

#parameters
uplift_rate = 0.0005
hillslope_diffusivity = 1.0

#plot the actual profile
hillslope.plot(domain * dx / 1000, topo, marker='o', c='k', linewidth = 0, markerfacecolor='None', label = 'Numerical Solution')

#plot the theoretical profile
x = np.arange(-max(domain) / 2., max(domain) / 2. + dx, dx)
theory_profile = (uplift_rate / hillslope_diffusivity) * \
    ((max(x+max(x))/2.)**2 / 2.0) + ((-uplift_rate / hillslope_diffusivity) *\
    (x**2 / 2.0))
plt.plot((x + max(x)) * dx / 1000, theory_profile , linestyle='-', c='grey', linewidth = 2, label = 'Analytical Solution')

#axis labels
hillslope.set_xlabel('Distance [km]')
hillslope.set_ylabel('Elevation [m]')

#legend
hillslope.legend(scatterpoints = 1, prop={'size':12})

#save figure
fig.savefig('basic_lin_diff_topo.eps',bbox_inches='tight', dpi=300)