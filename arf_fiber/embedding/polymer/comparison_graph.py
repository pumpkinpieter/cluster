#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
import matplotlib.pyplot as plt
from cmasher import get_sub_cmap
from os.path import expanduser, relpath
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

plt.close('all')

main = expanduser('~/local/convergence/arf_fiber/embedding/polymer/data/')
path = relpath(main + 'k_')

# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(28, 14))

materials = [
    # 'inf',
    # 0.01,
    # 0.005,
    1e-3,
    5e-4,
    1e-4,
    1e-5,
    0,
]

cmap = get_sub_cmap('cmr.ocean', 0.4, .85, N=len(materials))
colors = cmap.colors

# styles = [

#     {'lw': 1.5, 'msz': 0, 'ls': '-', 'm': '^',
#      'c': cmap.colors[7], 'label': '$N_0$'},

#     {'lw': 1.5, 'msz': 0, 'ls': '-', 'm': '^',
#      'c': cmap.colors[6], 'label': '$k = 0.01$'},

#     {'lw': 1.5, 'msz': 0, 'ls': '-', 'm': '^',
#      'c': cmap.colors[5], 'label': '$k = 0.005$'},

#     {'lw': 1.5, 'msz': 0, 'ls': '-', 'm': '^',
#      'c': cmap.colors[4], 'label': '$k = 0.001$'},

#     {'lw': 1.5, 'msz': 0, 'ls': '-', 'm': '^',
#      'c': cmap.colors[3], 'label': '$k = 0.0005$'},

#     {'lw': 1.5, 'msz': 0, 'ls': '-', 'm': '^',
#      'c': cmap.colors[2], 'label': '$k = 0.0001$'},

#     {'lw': 1.5, 'msz': 0, 'ls': '-', 'm': '^',
#      'c': cmap.colors[1], 'label': '$k = 0.00001$'},

#     {'lw': 1.5, 'msz': 0, 'ls': '-', 'm': '^',
#      'c': cmap.colors[0], 'label': '$k = 0.0$'},

#     # {'lw': 2.5, 'msz': 0, 'ls': (0, (8, 8)), 'm': '^',
#     #  'c': 'orange', 'label': 'polymer with $n_{im}=0.1$, air outside'},

#     # {'lw': 2.4, 'msz': 0, 'ls': '-', 'm': '^',
#     #  'c': 'firebrick', 'label': '$k = 0.01$'},

#     # {'lw': .5, 'msz': 0, 'ls': '-', 'm': '^',
#     #  'c': 'grey', 'label': '$k = 0.0001$'}

# ]


# Plot the data
for i, k in enumerate(materials):
    CL = np.load(relpath(path + str(float(k)) + '.npy'))
    es = np.linspace(0.002, .9999, len(CL))

    ax1.plot(es[~np.isnan(CL)], CL[~np.isnan(CL)], ls='-',
             label='k = ' + f'{k:.0e}' if k != 0 else 'k = 0',
             linewidth=2.5, color=colors[-i-1])

# Set Figure and Axes parameters ################################

# Set titles
# fig.suptitle("Kolyadin Fiber: Fundamental Mode Losses \n\
# for Lossy Polymer Coatings",
#              fontsize=30)


# Set axis labels
ax1.set_xlabel("\nEmbedding Fraction", fontsize=28)
ax1.set_ylabel("CL\n", fontsize=28)

# Set up ticks and grids

plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)

ax1.xaxis.set_major_locator(MultipleLocator(.1))
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
plt.subplots_adjust(top=0.969,
                    bottom=0.111,
                    left=0.075,
                    right=0.98,
                    hspace=0.2,
                    wspace=0.2)

# ax1.set_ylim(1e-7, 1e3)
ax1.legend(title='Exctinction Coefficients', title_fontsize=20, fontsize=20)
# Show figure (needed for running from command line)
plt.show()
