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

# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False,
                               gridspec_kw={'height_ratios': [2.5, 1]},
                               figsize=(35, 18))

wls = np.linspace(3.44937, 3.45012, 400) * 1e-6

main = os.path.expanduser('~/local/convergence/arf_fiber/kolyadin/wavelength/')
path = os.path.relpath(main + 'air/subinterval/344_346/subsubinterval/\
ref0_p5')

# First set of data
raw1 = np.load(path + '/all_e.npy').imag
base1 = np.zeros_like(wls)

for j in range(len(wls)):

    b = raw1[j, :]
    if j == 15:
        L = b[np.where((b > 1.2e-6) * (b < 1e0/8))]
    else:
        L = b[np.where((b > .5e-6) * (b < 1e0/8))]
    try:
        base1[j] = np.min(L)
    except ValueError:
        base1[j] = np.nan


CL1 = 20 * base1 / np.log(10)

ax1.plot(CL1, color='blue',
         label='p5_ref0', marker='o',
         linewidth=3, markersize=3)

# ax1.plot(wls[190], 0.008333398249461233, marker='o',
#          markersize=10, color='r')


# Second set of data
path = os.path.relpath(main + 'air/subinterval/344_346/subsubinterval/\
ref0_p6')
raw2 = np.load(path + '/all_e.npy').imag
base2 = np.zeros_like(wls)

for j in range(len(wls)):

    b = raw2[j, :]
    L = b[np.where((b > 1e-7) * (b < 1e0/8))]
    try:
        base2[j] = np.min(L)
    except ValueError:
        base2[j] = np.nan

CL2 = 20 * base2 / np.log(10)

# # Plot the data
ax1.plot(CL2, color='orange',
         label='p6_ref0', marker='o',
         linewidth=0, markersize=8)

# # Residuals (using hausdorff dist)


# def hausdist(A, B):
#     A, B = np.array(A), np.array(B)
#     hmat = np.abs(A[:, np.newaxis] - B[np.newaxis, :])
#     hminA = np.min(hmat, axis=0)
#     hminB = np.min(hmat, axis=1)
#     return max(np.max(hminA), np.max(hminB))


# base3 = np.zeros_like(wls)

# for j in range(len(wls)):

#     b1, b2 = raw1[j, :], raw2[j, :]
#     L1, L2 = b1[np.where((b1 > 1e-7) * (b1 < 1e0/8))
#                 ], b2[np.where((b2 > 1e-7) * (b2 < 1e0/8))]
#     try:
#         base3[j] = hausdist(L1, L2)
#     except ValueError:
#         base3[j] = np.nan

# resCL = 20 * base3 / np.log(10)
# good = ~np.isnan(resCL)

# Plot the data
# ax2.plot(wls[good], resCL[good], color='green',
#           linewidth=.9, label='residual', markersize=1)

good = ~np.isnan(CL1) * ~np.isnan(CL2)
res = np.abs(CL1[good] - CL2[good])
rel = np.abs(CL1[good] + CL2[good])/2

# Plot the data

ax2.plot(wls[good], 100*res/CL1[good], color='green',
         linewidth=2, label='relative error', markersize=1)

# ax2.plot(wls[good], res, color='blue',
#           linewidth=.9, label='residual', markersize=1)

# ax1.plot(wls[good], res, color='green',
#           linewidth=.9, label='residual', markersize=1)
# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("8 Tube ARF Benchmarking: Bad error spike.\n",  fontsize=42)

# Set axis labels
ax2.set_xlabel("\nWavelength", fontsize=40)
ax1.set_ylabel("CL\n", fontsize=40)
ax2.set_ylabel("% Error\n", fontsize=40)

# Set up ticks and grids

plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)

# ax1.xaxis.set_major_locator(MultipleLocator(5e-11))
# ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax1.yaxis.set_major_locator(MultipleLocator(1))
# ax1.yaxis.set_minor_locator(AutoMinorLocator(0))
# ax1.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
# ax1.grid(which='minor', color='#CCCCCC', linestyle=':')

# # # Set log scale on y axes
ax1.set_yscale('log')
ax2.set_yscale('log')


# ax2.xaxis.set_major_locator(MultipleLocator(2e-9))
# ax2.xaxis.set_minor_locator(AutoMinorLocator(5))

y_major = LogLocator(base=10)
y_minor = LogLocator(base=10, subs=(2.0, 3., 4., 5., 6., 7., 8., 9.))

ax2.yaxis.set_major_locator(y_major)
ax2.yaxis.set_minor_locator(y_minor)

ax2.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax2.grid(which='minor', color='#CCCCCC', linestyle=':')

# Set log scale on y axes

# Turn on subplot tool when graphing to allow finer control of spacing
# plt.subplot_tool(fig)

# After fine tuning, these are the values we want (use export from tool)
plt.subplots_adjust(top=0.915,
                    bottom=0.098,
                    left=0.077,
                    right=0.981,
                    hspace=0.095,
                    wspace=0.2)

ax2.set_ylim(1e-4, 1e2)
# ax1.set_xlim(3.1e-6, 3.61e-6)
ax1.legend(fontsize=35)
ax2.legend(fontsize=35, loc='upper right')
# Show figure (needed for running from command line)
plt.show()

# %%

# # Save cleaned data to numpy arrays for comparison plot

# np.save(os.path.relpath(main + 'wavelength/data/air_CL'), CL1)
# np.save(os.path.relpath(main + 'wavelength/data/air_wls'), wls)


# # %%

# # Save to .dat file for pgfplots

# paper_path = os.path.relpath(os.path.expanduser('~/papers/outer_materials/\
# figures/data/arf/8tube'))

# msk = ~np.isnan(CL1)

# both = np.column_stack((wls[msk]*1e6, CL1[msk]))
# np.savetxt(paper_path + '/ref0_p5_subint.dat', both, fmt='%.8f')

# msk = ~np.isnan(CL2)

# both = np.column_stack((wls[msk]*1e6, CL2[msk]))
# np.savetxt(paper_path + '/ref0_p6_subint.dat', both, fmt='%.8f')

# good = ~np.isnan(CL1) * ~np.isnan(CL2)
# res = np.abs(CL1[good] - CL2[good])
# rel = np.abs(CL1[good] + CL2[good])/2

# both = np.column_stack((wls[good]*1e6, 100*res/rel))
# np.savetxt(paper_path + '/ref0_p6p5_rel_error.dat', both, fmt='%.8f')
