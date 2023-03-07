#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from os.path import relpath, expanduser

plt.close('all')

main = expanduser('~/local/convergence/arf_fiber/modes/vector_modes/\
fine_cladding/pml_study')
path = relpath(main + '/outputs')

# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(36, 14))
alphas = np.linspace(1, 10, 37)


for p in [4, 5, 6]:
    raw = np.load(path + '/ref0_p%s_all_betas.npy' % p).imag

    base = np.zeros_like(alphas)
    err = np.zeros_like(alphas)

    for j in range(len(alphas)):

        b = raw[j]
        L = b[np.where((b > 0))]

        try:
            base[j] = np.mean(L)

        except ValueError:
            base[j] = np.nan
            err[j] = 1

    bad_ind = np.nonzero(err)[0]
    CL = 20 * base / np.log(10)

    # Plot the data
    ax1.plot(alphas, CL,
             label='p=%i' % p, marker='o',
             linewidth=2.5, markersize=5)


# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("PML parameter study, Fundamental Mode 6-tube ARF at wl=1.8e-6.",
             fontsize=26)

# Set axis labels
ax1.set_xlabel("\nalpha", fontsize=20)
ax1.set_ylabel("Loss\n", fontsize=20)


plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)

ax1.xaxis.set_major_locator(MultipleLocator(1))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax1.yaxis.set_major_locator(MultipleLocator(1))
# ax1.yaxis.set_minor_locator(AutoMinorLocator(1))
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

ax1.set_ylim(1.5e-1, 1.6e-1)
ax1.legend(fontsize=25)
# Show figure (needed for running from command line)
plt.show()

# # %%

# # Save cleaned data to numpy arrays for comparison plot
# mask = ~np.isnan(CL)

# np.save(relpath(main + 'data/poletti_CLs'), CL[mask])
# np.save(relpath(main + 'data/poletti_wls'), wls[mask])


# # %%

# # Save to .dat file for pgfplots

# paper_path = relpath(expanduser('~/papers/outer_materials/\
# figures/data'))

# mask = ~np.isnan(CL)

# both = np.column_stack((wls[mask], CL[mask]))
# np.savetxt(paper_path + '/polleti_wl_study.dat', both, fmt='%.8f')
