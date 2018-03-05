# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:35:13 2017

@author: Charlie Shobe

Plotting script for slope-area relationships for EMS steady-state runs

*assumes there is a variable area_array that is drainage area in m^2.
*and also that there's one called slope_array that contains slope in m/m.
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

##instantiate figure and plot
fig = plt.figure(figsize=(6, 3.75))
slope_area = plt.subplot()

#plotting param
matplotlib.rcParams.update({'font.size': 20})

#create an array for the detachment-limited analytical solution
u = 0.0005 #m/yr, uplift or baselevel lowering rate
k = 0.01 #fluvial erodibility
m = 0.5 #discharge exponent
n = 1.0 #slope exponent

#calculate analytical slope from area field
analytical_slope_array = np.power((u / k), 1 / n) * np.power(area_array, -m/n)

#plot the analytical solution
slope_area.plot(area_array, analytical_slope_array, linestyle='-',
                color='grey', linewidth = 1, label = 'Analytical solution')

#plot the data
slope_area.scatter(area_array, slope_array, marker='o', c='k', 
                   label = 'Numerical Solution') #plot HA data
                   
#make axes log and set limits
slope_area.set_xscale('log')
slope_area.set_yscale('log')

slope_area.set_xlim(9*10**1, 5*10**3)
slope_area.set_ylim(1e-4, 1e-2)

#set x and y labels
slope_area.set_xlabel(r'Drainage area [m$^2$]')
slope_area.set_ylabel('Channel slope [-]')
slope_area.legend(scatterpoints=1,prop={'size':12})
slope_area.tick_params(axis='x', which='major', pad=7)

fig.savefig('basic_streampower.eps',bbox_inches='tight', dpi=1000) #save figure