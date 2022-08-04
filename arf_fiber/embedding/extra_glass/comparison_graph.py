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

main = os.path.expanduser('~/local/convergence/arf_fiber/embedding/\
extra_glass/')

# Load range of embeddings (es)
es = np.linspace(0.002, .9999, 240)

CL5 = np.load(main + 'data/five_fixedcap.npy')
CL10 = np.load(main + 'data/ten_fixedcap.npy')
CL15 = np.load(main + 'data/fifteen_fixedcap.npy')
CL20 = np.load(main + 'data/twenty_fixedcap.npy')

CL0 = np.load(main + '../data/air_fixedcap.npy')

# Set up the figure and subplots
fig, axes = plt.subplots(2, 2, sharex=False, figsize=(50, 30))

# Plot the data
axes[0, 0].plot(es, CL0, '^-', color='blue',
                label='shifting_capillaries',
                linewidth=2, markersize=5,
                markerfacecolor='None')

axes[0, 0].set_title('Cladding width 10:\n',
                     fontsize=25)

axes[0, 1].plot(es, CL5, 'o-', color='blue',
                label='fixed_capillaries',
                linewidth=2, markersize=5,
                markerfacecolor='None')

axes[0, 1].set_title('Cladding width 15:\n',
                     fontsize=25)

axes[1, 0].plot(es, CL10, 'o-', color='blue',
                label='fixed_capillaries',
                linewidth=2, markersize=5,
                markerfacecolor='None')

axes[1, 0].set_title('Cladding width 20:\n',
                     fontsize=25)

axes[1, 1].plot(es, CL15, 'o-', color='blue',
                label='fixed_capillaries',
                linewidth=2, markersize=5,
                markerfacecolor='None')

axes[1, 1].set_title('Cladding width 25:\n',
                     fontsize=25)

# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("Embedding Loss Profiles for Varying Cladding Widths\n\
(PML in air)", fontsize=40)

# # Set up ticks and grids

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)


# # Set log scale on y axes
for a in axes.flat:
    a.set_xlabel("\nFraction of Capillary Tube Embedded", fontsize=15)
    a.set_ylabel("CL", fontsize=15)
    # a.set_xlim(0, 1)
    a.set_ylim(1e-2, 2e1)
    a.set_yscale('log')
    a.set_yscale('log')
    a.xaxis.set_major_locator(MultipleLocator(.1))
    a.xaxis.set_minor_locator(AutoMinorLocator(5))
    # a.yaxis.set_major_locator(MultipleLocator(1))
    # a.yaxis.set_minor_locator(AutoMinorLocator(1))
    a.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
    a.grid(which='minor', color='#CCCCCC', linestyle=':')

# Turn on subplot tool when graphing to allow finer control of spacing
# plt.subplot_tool(fig)

# After fine tuning, these are the values we want (use export from tool)
plt.subplots_adjust(top=0.89,
                    bottom=0.08,
                    left=0.045,
                    right=0.98,
                    hspace=0.3,
                    wspace=0.15)

# Show figure (needed for running from command line)
plt.show()
