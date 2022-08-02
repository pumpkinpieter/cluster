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

main = os.path.expanduser('~/local/convergence/arf_fiber/embedding/\
extra_glass/')
path = os.path.relpath(main + 'twenty/fixed_tubes/outputs')

raw = np.load(path + '/all_e.npy').imag
es = np.linspace(0.002, .9999, 240)

base = np.zeros_like(es)

for j in range(len(es)):

    b = raw[j, :]

    if j == 41:
        c = np.where((b > 0.03), 1, 0)
        base[j] = np.mean(b, where=list(c))
    elif j == 43:
        c = np.where((b > 0.02), 1, 0)
        base[j] = np.mean(b, where=list(c))
    elif j == 51:
        c = np.where((b > 0.02), 1, 0)
        base[j] = np.mean(b, where=list(c))
    elif j == 108:
        c = np.where((b > 0) * (b < 3), 1, 0)
        base[j] = np.mean(b, where=list(c))
    elif j == 132:
        c = np.where((b > 0.007), 1, 0)
        base[j] = np.mean(b, where=list(c))
    elif j == 168 or j == 169:
        c = np.where((b > 0) * (b < 1), 1, 0)
        base[j] = np.mean(b, where=list(c))
    else:
        c = np.where((b > 1e-3), 1, 0)
        base[j] = np.mean(b, where=list(c))


CL = 20 * base / np.log(10)

# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(30, 15))

# Plot the data
ax1.plot(es, CL, '^-', color='blue',
         label='shifting_capillaries',
         linewidth=2.5, markersize=3.4)
# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("Embedding Sensitivity: Fixed Capillaries \
\n Extra Glass cladding with air.",  fontsize=30)

# Set axis labels
ax1.set_xlabel("\nFraction of Capillary Tube Embedded", fontsize=20)
ax1.set_ylabel("CL", fontsize=25)

# Set up ticks and grids

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)

ax1.xaxis.set_major_locator(MultipleLocator(.05))
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

np.save(os.path.relpath(main + 'data/twenty_fixedcap.npy'), CL)


# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/papers/arf_embedding/\
figures'))

mask = ~np.isnan(CL)
mask[14] = False

# both = np.concatenate((es[mask][np.newaxis], CL[mask][np.newaxis]), axis=1)
both = np.column_stack((es[mask], CL[mask]))
# both = np.column_stack((x,y))
np.savetxt(paper_path + '/fixed_capillaries.dat', both, fmt='%.8f')
