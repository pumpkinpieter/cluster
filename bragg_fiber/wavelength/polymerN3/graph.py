#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, LogLocator

plt.close('all')

main = os.path.expanduser('~/local/convergence/bragg_fiber/wavelength/\
polymerN3')
path = os.path.relpath(main + '/k_0.0025')

raw = np.load(path + '/all_wl.npy').imag
exact = -(np.load(main + '/exact_betas/k_0.0025.npy')/5e-5).imag
exact_CL = 20 * exact / np.log(10)
wls = np.linspace(2.97, 3.42, 401) * 1e-6

base = np.zeros_like(wls)

for j in range(len(wls)):
    if j == 73:
        b = raw[j, :]
        L = b[np.where((b > 0)*(b < .2))]
        base[j] = np.mean(L)

    elif j == 242:
        b = raw[j, :]
        L = b[np.where(b > .07)]
        base[j] = np.mean(L)

    elif j == 350:
        base[j] = np.nan

    elif j == 296:
        b = raw[j, :]
        L = b[np.where(b > 0)]
        base[j] = np.max(L)

    else:
        b = raw[j, :]
        L = b[np.where(b > 0)]
        try:
            base[j] = np.mean(L)
        except ValueError:
            base[j] = np.nan


CL = 20 * base / np.log(10)

# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False,
                               gridspec_kw={'height_ratios': [2.5, 1]},
                               figsize=(35, 18))

evens = np.arange(0, 401, 2)
# Plot the data
ax1.plot(wls, exact_CL, '-', color='blue',
         label='exact loss',
         linewidth=3, markersize=0)
ax1.plot(wls[evens], CL[evens], '-o', color='green',
         label='computed loss', markerfacecolor='white',
         linewidth=0, markersize=7)

evens = [n for n in range(0, len(wls), 2)]


res = 100*(np.abs(CL - exact_CL))/exact_CL

ax2.plot(wls, res, color='green',
         linewidth=2, label='relative error', markersize=1)

# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("Bragg N3 Spectral Loss Numerical Benchmarking",  fontsize=33)

# Set axis labels
ax2.set_xlabel("\nWavelength", fontsize=40)
ax1.set_ylabel("CL\n", fontsize=40)
ax2.set_ylabel("% Error\n", fontsize=40)

# Set log scaling
ax1.set_yscale('log')
ax2.set_yscale('log')

# Set up ticks and grids
plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)

ax1.xaxis.set_major_locator(MultipleLocator(1))
# ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax1.grid(which='minor', color='#CCCCCC', linestyle=':')

ax2.xaxis.set_major_locator(MultipleLocator(5e-8))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))

y_major = LogLocator(base=10)
y_minor = LogLocator(base=10, subs=(2.0, 3., 4., 5., 6., 7., 8., 9.))

ax2.yaxis.set_major_locator(y_major)
ax2.yaxis.set_minor_locator(y_minor)
ax2.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax2.grid(which='minor', color='#CCCCCC', linestyle=':')


ax1.legend(fontsize=22)

# Turn on subplot tool when graphing to allow finer control of spacing
# plt.subplot_tool(fig)

# After fine tuning, these are the values we want (use export from tool)
plt.subplots_adjust(top=0.905,
                    bottom=0.11,
                    left=0.075,
                    right=0.95,
                    hspace=0.2,
                    wspace=0.2)

# Show figure (needed for running from command line)
plt.show()

# %%

# Save cleaned data to numpy arrays for comparison plot

# np.save(os.path.relpath(main + 'fixed_cap_clean_CL'), CL)


# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/papers/outer_materials/\
manuscript/figures/data/bragg/polymerN3'))

mask = ~np.isnan(CL)

both = np.column_stack((wls[evens]*1e6, CL[evens]))
np.savetxt(paper_path + '/numeric.dat', both, fmt='%.8f')

both = np.column_stack((wls*1e6, exact_CL))
np.savetxt(paper_path + '/analytic.dat', both, fmt='%.8f')
