#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
import os
import matplotlib.pyplot as plt

plt.close('all')

main = os.path.expanduser('~/local/convergence/bragg_fiber/wavelength/')
path = os.path.relpath(main + 'N2/outputs')

raw = np.load(path + '/all_wl.npy').imag
exact = -(np.load(main + 'N2/exact_scaled_betas.npy')/15e-6).imag
exact_CL = 20 * exact / np.log(10)
wls = np.linspace(1.4, 2, 301) * 1e-6

base = np.zeros_like(wls)

for j in range(len(wls)):
    if j == 22:
        base[j] = np.nan
    elif j == 168:
        b = raw[j, :]
        L = b[np.where((b > 0.1) * (b < 30))]
        base[j] = np.min(L)
    # elif j == 195:
    #     base[j] = np.nan
    # elif j == 123:
    #     b = raw[j, :]
    #     L = b[np.where((b > 0.2) * (b < 2))]
    #     base[j] = np.min(L)
    else:
        b = raw[j, :]
        L = b[np.where((b > 0.006) * (b < 30))]
        try:
            base[j] = np.min(L)
        except ValueError:
            base[j] = np.nan


CL = 20 * base / np.log(10)

wls_cl = wls[~np.isnan(CL)]
CL_cl = CL[~np.isnan(CL)]
evens = [n for n in range(0, len(wls_cl), 2)]

# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(28, 14))

# Plot the data
ax1.plot(wls, exact_CL, '-', color='blue',
         label='exact loss',
         linewidth=3, markersize=0)
ax1.plot(wls_cl[evens], CL_cl[evens], '-o', color='green',
         label='computed loss', markerfacecolor='white',
         linewidth=0, markersize=7)

# ax1.plot(wls[~np.isnan(CL)], abs(exact_CL[~np.isnan(CL)]-CL[~np.isnan(CL)]),
#           '^-', color='green',
#           label='residual',
#           linewidth=1.5, markersize=2.4)

# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("Wavelength Study\nSingle glass tube surrounded by air",
             fontsize=22)

fig.suptitle('Hollow Core Bragg Fiber\n$N_2$ Configuration \
Wavelength Study\n', fontsize=25)

ax1.legend(fontsize=22)

# Set axis labels
ax1.set_xlabel("\nWavelength", fontsize=18)
ax1.set_ylabel("CL", fontsize=18)

# Set up ticks and grids

plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)

# ax1.xaxis.set_major_locator(MultipleLocator(1e-7))
# ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
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

# Show figure (needed for running from command line)
plt.show()

# %%

# Save cleaned data to numpy arrays for comparison plot

np.save(os.path.relpath(main + 'fixed_cap_clean_CL'), CL)


# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/papers/outer_materials/\
figures/data/bragg/N2'))

mask = ~np.isnan(CL)

both = np.column_stack((wls_cl[evens]*1e6, CL_cl[evens]))
np.savetxt(paper_path + '/numeric.dat', both, fmt='%.8f')

both = np.column_stack((wls[~np.isnan(CL)]*1e6, exact_CL[~np.isnan(CL)]))
np.savetxt(paper_path + '/analytic.dat', both, fmt='%.8f')
