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

main = os.path.expanduser('~/local/convergence/bragg_fiber/wavelength/N0/')
path = os.path.relpath(main + 'outputs')

raw = np.load(path + '/all_wl.npy').imag
exact = -(np.load(main + 'exact_scaled_betas.npy')/15e-6).imag
exact_CL = 20 * exact / np.log(10)
wls = np.linspace(1.4, 2, 301) * 1e-6

base = np.zeros_like(wls)

for j in range(len(wls)):
    if j == 142:
        b = raw[j, :]
        L = b[np.where(b > 0)]
        base[j] = np.nan
    elif j == 123:
        b = raw[j, :]
        L = b[np.where(b > 0)]
        base[j] = np.nan
    elif j == 102:
        b = raw[j, :]
        L = b[np.where(b > 0)]
        base[j] = np.max(L)
    else:
        b = raw[j, :]
        L = b[np.where(b > 0)]
        base[j] = np.min(L)


CL = 20 * base / np.log(10)

# Set up the figure and subplots
# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False,
                               gridspec_kw={'height_ratios': [2.5, 1]},
                               figsize=(35, 18))
# Plot the data
# Plot the data
wls_cl = wls[~np.isnan(CL)]
CL_cl = CL[~np.isnan(CL)]
evens = [n for n in range(0, len(wls_cl), 8)]

ax1.plot(wls, exact_CL, '-', color='blue',
         label='semi-analytic',
         linewidth=2, markersize=0)

ax1.plot(wls_cl[evens], CL_cl[evens],  linestyle='-',
         color='green', label='numerical', markerfacecolor='white',
         linewidth=0, markersize=8, marker='o')

res = 100*(np.abs(CL - exact_CL))/exact_CL

ax2.plot(wls, res, color='green',
         linewidth=2, label='relative error', markersize=1)

# Set Figure and Axes parameters ################################

# Set titles
# fig.suptitle("Bragg $N_0$ Spetral Loss Profile\n", fontsize=32)
ax1.legend(fontsize=25)
# Set axis labels
ax1.set_xlabel("\nWavelength", fontsize=28)
ax1.set_ylabel("CL\n", fontsize=28)

# Set up ticks and grids

plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)

ax1.xaxis.set_major_locator(MultipleLocator(1e-7))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.yaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(AutoMinorLocator(1))
ax1.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax1.grid(which='minor', color='#CCCCCC', linestyle=':')

# # Set log scale on y axes
ax1.set_yscale('log')
ax2.set_yscale('log')

# Turn on subplot tool when graphing to allow finer control of spacing
# plt.subplot_tool(fig)

# After fine tuning, these are the values we want (use export from tool)
# plt.subplots_adjust(top=0.905,
#                     bottom=0.11,
#                     left=0.065,
#                     right=0.95,
#                     hspace=0.2,
#                     wspace=0.2)

# Show figure (needed for running from command line)
plt.show()

# %%

# Save cleaned data to numpy arrays for comparison plot

# np.save(os.path.relpath(main + 'fixed_cap_clean_CL'), CL)
np.save(os.path.relpath(main + 'clean_betas_im'), base)

# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/school/dissertation/figures/\
data/bragg/N0'))

# both = np.column_stack((wls_cl[evens]*1e6, CL_cl[evens]))
# np.savetxt(paper_path + '/numeric.dat', both, fmt='%.8f')

both = np.column_stack((wls[~np.isnan(CL)]*1e6, res[~np.isnan(CL)]))
np.savetxt(paper_path + '/residuals.dat', both, fmt='%.8f')

# both = np.column_stack((wls*1e6, exact_CL))
# np.savetxt(paper_path + '/analytic.dat', both, fmt='%.8f')
