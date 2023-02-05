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
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(28, 14))

styles = [
    # {'lw': .5, 'msz': 0, 'ls': '-', 'm': '^',
    #   'c': 'grey', 'label': '$N_1$ configuration'},

    {'lw': 3, 'msz': 0, 'ls': '-', 'm': '^',
     'c': 'g', 'label': '$N_0$'},

    {'lw': 2.5, 'msz': 0, 'ls': (0, (8, 8)), 'm': '^',
     'c': 'orange', 'label': 'polymer with $n_{im}=0.1$, air outside'},

    {'lw': 2.4, 'msz': 0, 'ls': '-', 'm': '^',
     'c': 'firebrick', 'label': '$k = 0.01$'},

    {'lw': 1.2, 'msz': 0, 'ls': '-', 'm': '^',
     'c': 'darkblue', 'label': '$k = 0.001$'},

    {'lw': .5, 'msz': 0, 'ls': '-', 'm': '^',
     'c': 'grey', 'label': '$k = 0.0001$'}

]

materials = [
    # 'air',
    'glass',
    'poly',
    'poly2',
    'poly3',
    'poly4'
]

ks = [np.infty, 0.1, 0.01, 0.001, .0001]

# Plot the data
for s, d in zip(materials, styles):
    wls = np.load(relpath(main + s + '_wls.npy'))
    CL = np.load(relpath(main + s + '_CL.npy'))
    ax1.plot(wls[~np.isnan(CL)], CL[~np.isnan(CL)], ls=d['ls'],
             label=d['label'], linewidth=d['lw'], markersize=d['msz'],
             marker=d['m'], color=d['c'])

# Set Figure and Axes parameters ################################

# Set titles
# fig.suptitle("Kolyadin Fiber: Fundamental Mode Losses \n\
# for Lossy Polymer Coatings",
#              fontsize=30)


# Set axis labels
ax1.set_xlabel("\nWavelength", fontsize=28)
ax1.set_ylabel("CL\n", fontsize=28)

# Set up ticks and grids

plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)

ax1.xaxis.set_major_locator(MultipleLocator(1e-7))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.yaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(AutoMinorLocator(1))
ax1.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax1.grid(which='minor', color='#CCCCCC', linestyle=':')

# # Set log scale on y axes
ax1.set_yscale('log')

# Turn on subplot tool when graphing to allow finer control of spacing
# plt.subplot_tool(fig)

# After fine tuning, these are the values we want (use export from tool)
plt.subplots_adjust(top=0.905,
                    bottom=0.11,
                    left=0.065,
                    right=0.95,
                    hspace=0.2,
                    wspace=0.2)

# ax1.set_ylim(1e-7, 1e3)
ax1.legend(fontsize=25)
# Show figure (needed for running from command line)
plt.show()

# %%
# Save to .dat file for pgfplots

paper_path = relpath(expanduser('~/papers/outer_materials/\
figures/data/arf/8tube'))


# Plot the data
for s, k in zip(materials, ks):
    wls = np.load(relpath(main + s + '_wls.npy'))
    CL = np.load(relpath(main + s + '_CL.npy'))
    msk = ~np.isnan(CL)

    both = np.column_stack((wls[msk]*1e6, CL[msk]))
    np.savetxt(paper_path + '/k_'+str(k) + '.dat', both, fmt='%.8f')
