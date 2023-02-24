#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
from os.path import relpath, expanduser
import matplotlib.pyplot as plt
# from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

plt.close('all')

T = [10]
P = [4, 5]
ref = 0
alphas = [5, 7.5, 10]

main = relpath(expanduser('~/local/convergence/arf_fiber/wavelength/glass/\
pml_study/data'))

wls = np.linspace(1, 2, 200) * 1e-6
wls[12] = np.nan
wls = wls[~np.isnan(wls)]

figsize = (15*len(T), 8*len(P))
# Set up the figure and subplots
fig, ax = plt.subplots(len(P), len(T), sharex=False, figsize=figsize)
if len(T) == 1:
    ax = ax[:, np.newaxis]

# Plot the data
for i, p in enumerate(P):
    for j, t in enumerate(T):
        for alpha in alphas:
            try:
                name = '/ref%i_p%i_alpha%.2f_T%.2f' % (ref, p, alpha, t)
                CL = np.load(main + name + '.npy')

                ax[i, j].plot(wls, CL,
                              label='alpha=%.2f' % alpha,
                              linewidth=1.5)
            except FileNotFoundError:
                pass

            ax[i, j].legend(fontsize=18)
            ax[i, j].set_title('ref = %i, p = %i, T = %.2f' % (ref, p, t),
                               fontsize=22)

# Set Figure and Axes parameters ################################

# Set titles
# fig.suptitle("Wavelength Study: glass cladding to infinity",  fontsize=26)

# Set up ticks and grids

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)


# Turn on subplot tool when graphing to allow finer control of spacing
# plt.subplot_tool(fig)

# After fine tuning, these are the values we want (use export from tool)
plt.subplots_adjust(top=0.905,
                    bottom=0.11,
                    left=0.065,
                    right=0.95,
                    hspace=0.25,
                    wspace=0.2)

# Show figure (needed for running from command line)
plt.show()
