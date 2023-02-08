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
fig, ax1 = plt.subplots(1, 1, figsize=(18, 9))

wls = np.linspace(3.44, 3.46, 400)*1e-6

main = os.path.expanduser('~/local/convergence/arf_fiber/kolyadin/wavelength/')

paper_path = os.path.relpath(os.path.expanduser('~/papers/outer_materials/\
figures/data/arf/8tube/polysubinterval'))


ks = ['0.0', '0.1', '0.01', '0.001', '0.0001']
for k in ks:
    path = os.path.relpath(main + 'subinterval/k_' + k)

    raw = np.load(path + '/all_e.npy').imag
    base = np.zeros_like(wls)

    for j in range(len(wls)):

        b = raw[j, :]
        L = b[np.where((b > 1e-7) * (b < .01))]
        try:
            base[j] = np.min(L)
        except ValueError:
            base[j] = np.nan

    CL = 20 * base / np.log(10)
    msk = ~np.isnan(CL)

    ax1.plot(wls[msk], CL[msk], marker='o', label='k='+k,
             linewidth=1.5, markersize=0)

    # Save cleaned data to numpy arrays for comparison plot
    np.save(os.path.relpath(main + 'subinterval/data/k_'+k+'wls'), wls[msk])
    np.save(os.path.relpath(main + 'subinterval/data/k_'+k+'CL'), CL[msk])

    both = np.column_stack((wls[msk]*1e6, CL[msk]))
    np.savetxt(paper_path + '/k_'+k+'.dat', both, fmt='%.8f')

# Set Figure and Axes parameters ################################

# Set titles
# fig.suptitle("Wavelength Study: Air outside glass cladding",  fontsize=22)

# Set axis labels
ax1.set_ylabel("CL\n", fontsize=28)

# Set up ticks and grids

plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)

ax1.xaxis.set_major_locator(MultipleLocator(5e-9))
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
plt.subplots_adjust(top=0.966,
                    bottom=0.103,
                    left=0.071,
                    right=0.97,
                    hspace=0.138,
                    wspace=0.2)

# ax1.set_ylim(1e-6, 1e2)
# ax1.set_xlim(3.1e-6, 3.61e-6)
ax1.legend(fontsize=18)
# Show figure (needed for running from command line)
plt.show()

# %%

# Save cleaned data to numpy arrays for comparison plot
np.save(os.path.relpath(main + 'subinterval/data/k_'+k+'wls'), wls[msk])
np.save(os.path.relpath(main + 'subinterval/data/k_'+k+'CL'), CL[msk])


# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/papers/outer_materials/\
figures/data/arf/8tube/polysubinterval'))

both = np.column_stack((wls[msk]*1e6, CL[msk]))
np.savetxt(paper_path + '/k_'+k+'.dat', both, fmt='%.8f')
