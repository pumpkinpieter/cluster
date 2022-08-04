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
path = os.path.relpath(main + 'one/fixed_tubes/outputs')
p3path = os.path.relpath(main + 'one/fixed_tubes/p3_outputs')
p4path = os.path.relpath(main + 'one/fixed_tubes/p4_outputs')

raw = np.load(path + '/all_e.npy').imag
rawp3 = np.load(p3path + '/all_e.npy').imag
rawp4 = np.load(p4path + '/all_e.npy').imag

es = np.linspace(0.002, .9999, 240)

base = np.zeros_like(es)

for j in range(len(es)):

    b = raw[j, :]
    c = np.where((b > 1e-4) * (b < 2), 1, 0)
    base[j] = np.mean(b, where=list(c))

CL = 20 * base / np.log(10)
base = np.zeros_like(es)

for j in range(len(es)):

    b = rawp4[j, :]
    c = np.where((b > 1e-4) * (b < 2), 1, 0)
    base[j] = np.mean(b, where=list(c))

CLp4 = 20 * base / np.log(10)

base = np.zeros_like(es)

for j in range(len(es)):

    b = rawp3[j, :]
    c = np.where((b > 1e-4) * (b < 2), 1, 0)
    base[j] = np.mean(b, where=list(c))

CLp3 = 20 * base / np.log(10)
CL0 = np.load(main + '../data/air_fixedcap.npy')

# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(30, 15))

# Plot the data
ax1.plot(es, CLp3, '-', color='orange',
         label='p=3',
         linewidth=2)
ax1.plot(es, CLp4, '-', color='green',
         label='p=4',
         linewidth=2)
ax1.plot(es, CL, '--', color='blue',
         label='p=5',
         linewidth=2, markersize=3.4)

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

plt.legend(fontsize=20)
# Show figure (needed for running from command line)
plt.show()

# # %%

# # Save cleaned data to numpy arrays for comparison plot

# np.save(os.path.relpath(main + 'data/extra_glass_fixedcap.npy'), CL)


# # %%

# # Save to .dat file for pgfplots

# paper_path = os.path.relpath(os.path.expanduser('~/papers/arf_embedding/\
# figures'))

# mask = ~np.isnan(CL)
# mask[14] = False

# # both = np.concatenate((es[mask][np.newaxis], CL[mask][np.newaxis]), axis=1)
# both = np.column_stack((es[mask], CL[mask]))
# # both = np.column_stack((x,y))
# np.savetxt(paper_path + '/fixed_capillaries.dat', both, fmt='%.8f')
