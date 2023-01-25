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

# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(38, 10))

wls = np.linspace(3.11, 3.6, 800) * 1e-6

main = os.path.expanduser('~/local/convergence/arf_fiber/kolyadin/')
path = os.path.relpath(main + 'wavelength/air/ref0_outputs')

raw = np.load(path + '/all_e.npy').imag
base = np.zeros_like(wls)

for j in range(len(wls)):

    b = raw[j, :]
    L = b[np.where((b > 1e-7) * (b < 1e0/8))]
    try:
        base[j] = np.min(L)
    except ValueError:
        base[j] = np.nan


CL = 20 * base / np.log(10)

ax1.plot(wls[~np.isnan(CL)], CL[~np.isnan(CL)], '^-', color='blue',
         label='ref0',
         linewidth=1.5, markersize=0)

path = os.path.relpath(main + 'wavelength/air/outputs')

raw = np.load(path + '/all_e.npy').imag

base = np.zeros_like(wls)

for j in range(len(wls)):

    b = raw[j, :]
    L = b[np.where((b > 1e-7) * (b < 1e0/8))]
    try:
        base[j] = np.min(L)
    except ValueError:
        base[j] = np.nan


CL = 20 * base / np.log(10)

# Plot the data
ax1.plot(wls[~np.isnan(CL)], CL[~np.isnan(CL)], '^-', color='orange',
         label='ref1',
         linewidth=1.5, markersize=0)
# Set Figure and Axes parameters ################################

# Set titles
# fig.suptitle("Wavelength Study: Air outside glass cladding",  fontsize=22)

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
plt.subplots_adjust(top=0.985,
                    bottom=0.141,
                    left=0.048,
                    right=0.996,
                    hspace=0.2,
                    wspace=0.2)

# ax1.set_ylim(1e-6, 1e2)
ax1.set_xlim(3.1e-6, 3.61e-6)
plt.legend(fontsize=18)
# Show figure (needed for running from command line)
plt.show()

# %%

# Save cleaned data to numpy arrays for comparison plot

np.save(os.path.relpath(main + 'wavelength/data/air_CL'), CL)
np.save(os.path.relpath(main + 'wavelength/data/air_wls'), wls)


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
