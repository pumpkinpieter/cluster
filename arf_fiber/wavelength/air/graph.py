#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

plt.close('all')

main = os.path.expanduser('~/local/convergence/arf_fiber/wavelength/')
path = os.path.relpath(main + 'air/outputs')

raw = np.load(path + '/all_e.npy').imag
wls = np.linspace(1, 2, 200) * 1e-6

base = np.zeros_like(wls)

for j in range(len(wls)):

    b = raw[j, :]
    L = b[np.where(b > 0)]
    try:
        base[j] = np.min(L)
    except ValueError:
        base[j] = np.nan


CL = 20 * base / np.log(10)

# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(15, 7))

# Plot the data
ax1.plot(wls, CL, '^-', color='blue',
         label='shifting_capillaries',
         linewidth=1.5, markersize=1.4)
# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("Wavelength Study: Air outside glass cladding",  fontsize=16)

# Set axis labels
ax1.set_xlabel("\nWavelength", fontsize=11)
ax1.set_ylabel("CL", fontsize=11)

# Set up ticks and grids

plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)

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

# Show figure (needed for running from command line)
plt.show()

# %%

# Save cleaned data to numpy arrays for comparison plot

np.save(os.path.relpath(main + 'fixed_cap_clean_CL'), CL)


# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/papers/arf_embedding/\
figures'))

mask = ~np.isnan(CL)
mask[14] = False

# both = np.concatenate((es[mask][np.newaxis], CL[mask][np.newaxis]), axis=1)
both = np.column_stack((wls[mask], CL[mask]))
# both = np.column_stack((x,y))
np.savetxt(paper_path + '/fixed_capillaries.dat', both, fmt='%.8f')
