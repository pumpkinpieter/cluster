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

main = os.path.expanduser('~/local/convergence/bragg_fiber/wavelength/')
path = os.path.relpath(main + 'N1/outputs')

raw = np.load(path + '/all_wl.npy').imag
exact = -(np.load(main + 'N1/exact_scaled_betas.npy')/15e-6).imag
exact_CL = 20 * exact / np.log(10)
wls = np.linspace(1.4, 2, 301) * 1e-6

base = np.zeros_like(wls)

for j in range(len(wls)):
    # if j == 195:
    #     base[j] = np.nan
    # elif j == 70:
    #     base[j] = np.nan
    # else:
    b = raw[j, :]
    L = b[np.where((b > 0.08) * (b < 8e2))]
    try:
        base[j] = np.min(L)
    except ValueError:
        base[j] = np.nan


CL = 20 * base / np.log(10)

# Formula for loss spikes from article

ms = np.arange(11, 15, 1)
n_air = 1.00027717
n_glass = 1.4388164768221814

n1 = n_air  # Inner (core) index
n2 = n_glass  # Cladding index

d = 15*2/3*1e-6

# when n2 depends on ls, need solver
ls = (2 * n1 * d / ms * ((n2/n1)**2 - 1)**.5)

# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(28, 14))

# Plot the data
wls_cl = wls[~np.isnan(CL)]
CL_cl = CL[~np.isnan(CL)]
evens = [n for n in range(0, len(wls_cl), 2)]

ax1.plot(wls_cl[evens], CL_cl[evens],  linestyle='-',
         color='green', label='numerical', markerfacecolor='white',
         linewidth=0, markersize=8, marker='o')

ax1.plot(wls[~np.isnan(CL)], exact_CL[~np.isnan(CL)], '-', color='blue',
         label='semi-analytic',
         linewidth=2, markersize=0)

m, M = ax1.get_ylim()
ax1.margins(0, 0.02)

for L in ls:
    ax1.plot([L, L], [m, 2*M],  linewidth=2.5, color='orange',
             linestyle=(0, (2, 2)))

rel_error = 100*abs(exact_CL[~np.isnan(CL)]-CL[~np.isnan(CL)])/CL[~np.isnan(CL)]

ax1.plot(wls[~np.isnan(CL)], rel_error,
         '^-', color='green',
         label='residual',
         linewidth=1.5, markersize=2.4)

# Set Figure and Axes parameters ################################

# Set titles
# fig.suptitle("Wavelength Study\nSingle glass tube surrounded by air",
#              fontsize=22)

# fig.suptitle('Hollow Core Bragg Fiber\n$N_1$ Configuration \
# Wavelength Study\n', fontsize=25)


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

# np.save(os.path.relpath(main + 'fixed_cap_clean_CL'), CL)


# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/school/dissertation/figures/\
data/bragg/N1'))

mask = ~np.isnan(CL)

# both = np.column_stack((wls_cl[evens]*1e6, CL_cl[evens]))
# np.savetxt(paper_path + '/numeric.dat', both, fmt='%.8f')

both = np.column_stack((wls[~np.isnan(CL)]*1e6, rel_error))
np.savetxt(paper_path + '/residuals.dat', both, fmt='%.8f')

# both = np.column_stack((wls[~np.isnan(CL)]*1e6, exact_CL[~np.isnan(CL)]))
# np.savetxt(paper_path + '/analytic.dat', both, fmt='%.8f')
