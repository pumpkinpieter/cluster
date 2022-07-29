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

# Close old graphs

plt.close('all')

main = os.path.expanduser('~/local/convergence/arf_fiber/poletti/embedding/')

# Get paths to data

path1 = os.path.relpath(main + 'shifting_tubes/outputs')

# Load data and range of embeddings (es)

raw1 = np.load(path1 + '/all_e.npy').imag
es = np.linspace(0.002, .9999, 240)

# Process the data
base1 = np.zeros_like(es)

for j in range(len(es)):
    b = raw1[j, :]
    c = np.where((b != 0) * (np.abs(b) < 2) * (b > 0), 1, 0)
    base1[j] = np.mean(b, where=list(c))

CL1 = 20 * base1 / np.log(10)
mask = ~np.isnan(CL1)
CL2 = np.load(main + 'fixed_cap_clean_CL.npy')

# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False, figsize=(30, 30))

# Plot the data
ax1.plot(es[mask], CL1[mask], '^-', color='blue',
         label='shifting_capillaries',
         linewidth=2.5, markersize=3.4)

ax2.plot(es, CL2, 'o-', color='green',
         label='fixed_capillaries',
         linewidth=2.5, markersize=3.4)

# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("Comparison of Embedding Sensitivity", fontsize=42)

ax1.set_title('Shifting Capillaries, Fixed Cladding Position:\n',
              fontsize=30)
ax2.set_title('Fixed Capillaries, Shifting Cladding Position:\n',
              fontsize=30)

# Set axis labels
ax2.set_xlabel("\nFraction of Capillary Tube Embedded", fontsize=20)
ax1.set_ylabel("CL", fontsize=20)
ax2.set_ylabel("CL", fontsize=20)

# Set up ticks and grids

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)

ax1.xaxis.set_major_locator(MultipleLocator(.05))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.yaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(AutoMinorLocator(1))
ax1.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax1.grid(which='minor', color='#CCCCCC', linestyle=':')


ax2.xaxis.set_major_locator(MultipleLocator(.05))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
ax2.yaxis.set_major_locator(MultipleLocator(1))
ax2.yaxis.set_minor_locator(AutoMinorLocator(1))
ax2.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax2.grid(which='minor', color='#CCCCCC', linestyle=':')

# # Set log scale on y axes
ax1.set_yscale('log')
ax2.set_yscale('log')

# Turn on subplot tool when graphing to allow finer control of spacing
# plt.subplot_tool(fig)

# After fine tuning, these are the values we want (use export from tool)
plt.subplots_adjust(top=0.88,
                    bottom=0.11,
                    left=0.085,
                    right=0.935,
                    hspace=0.3,
                    wspace=0.2)

# Show figure (needed for running from command line)
plt.show()
