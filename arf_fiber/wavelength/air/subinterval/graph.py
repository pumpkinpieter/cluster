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
# from sklearn.cluster import KMeans

plt.close('all')

main = os.path.expanduser('~/local/convergence/arf_fiber/wavelength/air/')
path = os.path.relpath(main + 'subinterval/outputs')

raw = np.load(path + '/all_e.npy').imag
wls = np.linspace(1.3, 1.4, 2000) * 1e-6

base = np.zeros_like(wls)
n_clust = 3
err = np.zeros_like(wls)


msk = np.where((wls > 1.3252e-6)*(wls < 1.3257e-6))
for j in range(len(wls)):

    b = raw[j]
    L = b[np.where((b > 2e-4)*(b < .6e0))]

    try:
        if j == 630:
            base[j] = np.nan
            err[j] = 1

        elif j == 93:
            base[j] = np.max(L)

        elif len(L) == 3:  # Median works well if len == 3
            base[j] = np.median(L)

        elif len(L) == 4:  # For 4, we typically have 2 centers
            # means = KMeans(n_clusters=n_clust, random_state=0,
            #                n_init=1).fit(L.reshape(-1, 1))
            # ctrs = np.sort(means.cluster_centers_.flatten())
            # base[j] = ctrs[np.argmin(np.abs(ctrs-base[j-1]))]
            base[j] = L[np.argmin(np.abs(L-base[j-1]))]

        else:
            base[j] = np.min(L)

    except ValueError:
        base[j] = np.nan
        err[j] = 1


bad_ind = np.nonzero(err)[0]

CL = 20 * base / np.log(10)

# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(35, 13))

# Plot the data
ax1.plot(wls[msk], CL[msk], '^-', color='blue',
         # label='shifting_capillaries',
         linewidth=1.5, markersize=2.4)
# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("Wavelength Study: Air outside glass cladding, Poletti Fiber, \
Subinterval", fontsize=26)

# Set axis labels
ax1.set_xlabel("\nWavelength", fontsize=28)
ax1.set_ylabel("CL\n", fontsize=28)


plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)

ax1.xaxis.set_major_locator(MultipleLocator(.005e-8))
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


# ax1.set_xlim(1.3e-6, 1.4e-6)
# ax1.set_ylim(1e-4, 1e2)
# ax1.legend(fontsize=25)
# Show figure (needed for running from command line)
plt.show()

# %%

# Save cleaned data to numpy arrays for comparison plot

# mask = ~np.isnan(CL)

# np.save(os.path.relpath(main + 'data/poletti_sub_CLs'), CL[mask])
# np.save(os.path.relpath(main + 'data/poletti_sub_wls'), wls[mask])

# # %%

# # Save to .dat file for pgfplots

# paper_path = os.path.relpath(os.path.expanduser('~/papers/outer_materials/\
# figures/data'))

# mask = ~np.isnan(CL)

# # both = np.concatenate((es[mask][np.newaxis], CL[mask][np.newaxis]), axis=1)
# both = np.column_stack((wls[mask], CL[mask]))
# # both = np.column_stack((x,y))
# np.savetxt(paper_path + '/polleti_wl_subinterval.dat', both, fmt='%.8f')
