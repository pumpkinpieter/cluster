#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
from os.path import relpath, expanduser
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

plt.close('all')

ref = 0
p = 5
alpha = 10
T = 10

main = expanduser('~/local/convergence/arf_fiber/wavelength/glass/pml_study')
path = relpath(main + '/ref%i_p%i/alpha%.2f_T%.2f' % (ref, p, alpha, T))

raw = np.load(path + '/all.npy').imag

wls = np.linspace(1, 2, 200) * 1e-6
base = np.zeros_like(wls)

for j in range(len(wls)):

    b = raw[j, :]

    b = b[np.where(b > 0)]
    try:
        base[j] = np.mean(b)
    except ValueError:
        base[j] = np.nan
    if j == 12:
        base[j] = np.nan

CL = 20 * base / np.log(10)

mask = ~np.isnan(CL)
wls, CL = wls[mask], CL[mask]
# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(25, 11))

# Plot the data
ax1.plot(wls, CL, '^-', color='blue',
         label='shifting_capillaries',
         linewidth=1.5, markersize=1.4)
# Set Figure and Axes parameters ################################

# Set titles
# fig.suptitle("Wavelength Study: glass cladding to infinity",  fontsize=26)

# Set axis labels
ax1.set_xlabel("\nWavelength", fontsize=18)
ax1.set_ylabel("CL", fontsize=18)

# Set up ticks and grids

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)

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

# Save cleaned data to numpy arrays for comparison plot

np.save(relpath(main + '/data/ref%i_p%i_alpha%.2f_T%.2f' % (ref, p, alpha, T)),
        CL)


# %%

# Save to .dat file for pgfplots

paper_path = relpath(expanduser('~/papers/outer_materials/figures/data/arf/\
6tube/pml/'))

mask = ~np.isnan(CL)

both = np.column_stack((wls[mask], CL[mask]))
np.savetxt(paper_path + '/ref%i_p%i_alpha%.2f_T%.2f.dat' %
           (ref, p, alpha, T), both, fmt='%.8f')
