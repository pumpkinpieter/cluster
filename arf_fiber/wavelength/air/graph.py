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
# from fiberamp.fiber.microstruct.pbg import ARF2
import matplotlib
matplotlib.use("Qt5Agg")

plt.close('all')

main = os.path.expanduser('~/local/convergence/arf_fiber/wavelength/air/')
path = os.path.relpath(main + 'outputs')

raw = np.load(path + '/all_e.npy').imag
wls = np.linspace(1, 2, 2000) * 1e-6

base = np.zeros_like(wls)
err = np.zeros_like(wls)

# A = ARF2(name='fine_cladding', poly_core=True, refine=0,
#          curve=8, shift_capillaries=False, e=1)

# d = (A.T_cladding+A.T_tube)* A.scale
d = 9.999999999999999e-06
# d = (A.T_cladding+A.T_tube)* A.scale

n1, n2 = 1.00027717, 1.4388164768221814
lines = [2 * n1 * d / m * ((n2/n1)**2 - 1)**.5 for m in range(11, 21)]

for j in range(len(wls)):

    b = raw[j]
    L = b[np.where((b > 2e-4)*(b < .6e0))]

    try:
        if len(L) == 3:  # Median works well if len == 3
            base[j] = np.median(L)

        elif len(L) == 4:  # For 4, we find closest to previous
            base[j] = L[np.argmin(np.abs(L-base[j-1]))]

        else:
            base[j] = np.min(L)

    except ValueError:
        base[j] = np.nan
        err[j] = 1

bad_ind = np.nonzero(err)[0]
CL = 20 * base / np.log(10)

# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(32, 14))

# Plot the data
ax1.plot(wls, CL, '^-', color='blue',
         # label='shifting_capillaries',
         linewidth=1.5, markersize=.4)

m, M = ax1.get_ylim()
for line in lines:
    ax1.plot([line, line], [m, M])

# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("Wavelength Study: Air outside glass cladding, Poletti Fiber",
             fontsize=26)

# Set axis labels
ax1.set_xlabel("\nWavelength", fontsize=28)
ax1.set_ylabel("CL\n", fontsize=28)


plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=22)

ax1.xaxis.set_major_locator(MultipleLocator(5e-8))
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

# ax1.set_ylim(1e-7, 1e3)
ax1.legend(fontsize=25)
# Show figure (needed for running from command line)
plt.show()

# %%

# Save cleaned data to numpy arrays for comparison plot
mask = ~np.isnan(CL)

np.save(os.path.relpath(main + 'data/poletti_CLs'), CL[mask])
np.save(os.path.relpath(main + 'data/poletti_wls'), wls[mask])


# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/papers/outer_materials/\
figures/data'))

mask = ~np.isnan(CL)

both = np.column_stack((wls[mask], CL[mask]))
np.savetxt(paper_path + '/polleti_wl_study.dat', both, fmt='%.8f')
