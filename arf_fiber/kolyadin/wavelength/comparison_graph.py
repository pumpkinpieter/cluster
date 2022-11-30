#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
from os.path import expanduser, relpath
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

plt.close('all')

main = expanduser('~/local/convergence/arf_fiber/kolyadin/wavelength/\
data/')


# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(36, 15))

styles = [
    {'lw': 1.5, 'msz': 0, 'ls': '-', 'm': '^',
     'c': 'blue', 'label': 'no polymer, air outside'},

    {'lw': 2, 'msz': 0, 'ls': '-', 'm': '^',
     'c': 'g', 'label': 'no polymer, glass outside'},

    # {'lw': 2, 'msz': 0, 'ls': (0, (6, 6)), 'm': '^',
    #  'c': 'orange', 'label': 'polymer with $n_{im}=.1$, air outside'},

    {'lw': 2, 'msz': 0, 'ls': '-', 'm': '^',
     'c': 'firebrick', 'label': 'polymer with $n_{im}=0.01$, air outside'}

]

materials = [
    'air',
    'glass',
    # 'poly',
    'poly2'
]

# Plot the data
for s, d in zip(materials, styles):
    wls = np.load(relpath(main + s + '_wls.npy'))
    CL = np.load(relpath(main + s + '_CL.npy'))
    ax1.plot(wls[~np.isnan(CL)], CL[~np.isnan(CL)], ls=d['ls'],
             label=d['label'], linewidth=d['lw'], markersize=d['msz'],
             marker=d['m'], color=d['c'])

# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("Kolyadin Fiber: Fundamental Mode Losses \n\
for Lossy Polymer Coatings",
             fontsize=30)

# Set axis labels
ax1.set_xlabel("\nWavelength", fontsize=24)
ax1.set_ylabel("CL\n", fontsize=24)

# Set up ticks and grids

plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)

ax1.xaxis.set_major_locator(MultipleLocator(1e-7))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.yaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(AutoMinorLocator(1))
ax1.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax1.grid(which='minor', color='#CCCCCC', linestyle=':')


# # Set log scale on y axes
ax1.set_yscale('log')
ax1.set_ylim(1e-7, 1e3)
# Turn on subplot tool when graphing to allow finer control of spacing
# plt.subplot_tool(fig)

# After fine tuning, these are the values we want (use export from tool)
plt.subplots_adjust(top=0.905,
                    bottom=0.11,
                    left=0.065,
                    right=0.95,
                    hspace=0.2,
                    wspace=0.2)

ax1.legend(fontsize=20)
# Show figure (needed for running from command line)
plt.show()
