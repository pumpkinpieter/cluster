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
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False,
                               gridspec_kw={'height_ratios': [1.3, 1]},
                               figsize=(35, 18))

wls = np.linspace(3.44, 3.46, 400) * 1e-6

main = os.path.expanduser('~/local/convergence/arf_fiber/kolyadin/wavelength/')
path = os.path.relpath(main + 'air/subinterval/344_346/ref0_p4')

raw = np.load(path + '/all_e.npy').imag
base = np.zeros_like(wls)

for j in range(len(wls)):

    b = raw[j, :]
    if j == 15:
        L = b[np.where((b > 1.2e-6) * (b < 1e0/8))]
    else:
        L = b[np.where((b > .5e-6) * (b < 1e0/8))]
    try:
        base[j] = np.min(L)
    except ValueError:
        base[j] = np.nan


CL0 = 20 * base / np.log(10)


nnan = ~np.isnan(CL0)

ax1.plot(wls[nnan], CL0[nnan], color='blue',
         label='p4_ref0', marker='o',
         linewidth=1.5, markersize=4)

# path = os.path.relpath(main + 'wavelength/air/p5ref0_outputs')

# raw = np.load(path + '/all_e.npy').imag

# base = np.zeros_like(wls)

# for j in range(len(wls)):

#     b = raw[j, :]
#     L = b[np.where((b > 1e-7) * (b < 1e0/8))]
#     try:
#         base[j] = np.min(L)
#     except ValueError:
#         base[j] = np.nan

# CL1 = 20 * base / np.log(10)
# rCL1 = CL1[msk]
# nnan2 = ~np.isnan(rCL1)

# # Plot the data
# ax1.plot(rwls[nnan2], rCL1[nnan2], color='orange',
#          label='p5_ref0', linestyle='--',
#          linewidth=1.5, markersize=0)

# # path = os.path.relpath(main + 'wavelength/air/subinterval/\
# # 343_347/p4ref0_suboutputs')

# # raw = np.load(path + '/all_e.npy').imag
# # subwls = np.linspace(3.43, 3.47, 400) * 1e-6

# # base = np.zeros_like(subwls)

# # for j in range(len(subwls)):

# #     b = raw[j, :]
# #     L = b[np.where((b > 1e-7) * (b < 1e0/8))]
# #     try:
# #         base[j] = np.min(L)
# #     except ValueError:
# #         base[j] = np.nan


# # CL2 = 20 * base / np.log(10)
# # nnan2 = ~np.isnan(CL2)

# # # Plot the data
# # ax1.plot(subwls[nnan2], CL2[nnan2], color='blue',
# #          label='p4_ref0', marker='o',
# #          linewidth=1.5, markersize=4)

# good = ~np.isnan(rCL0) * ~np.isnan(rCL1)

# res = np.abs(rCL1[good] - rCL0[good])
# rel = (rCL1[good] + rCL0[good]) / 2

# # Plot the data
# ax2.plot(rwls[good], res, color='green',
#          linewidth=.9, label='residual', markersize=1)

# Set Figure and Axes parameters ################################

# Set titles
# fig.suptitle("Wavelength Study: Air outside glass cladding",  fontsize=22)

# Set axis labels
ax2.set_xlabel("\nWavelength", fontsize=28)
ax1.set_ylabel("CL\n", fontsize=28)
ax2.set_ylabel("CL\n", fontsize=28)

# Set up ticks and grids

plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)

ax1.xaxis.set_major_locator(MultipleLocator(2e-9))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.yaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(AutoMinorLocator(1))
ax1.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax1.grid(which='minor', color='#CCCCCC', linestyle=':')

# # # Set log scale on y axes
ax1.set_yscale('log')


# ax2.xaxis.set_major_locator(MultipleLocator(1e-6))
# ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax2.yaxis.set_major_locator(MultipleLocator(1))
# ax2.yaxis.set_minor_locator(AutoMinorLocator(0))
# ax2.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
# ax2.grid(which='minor', color='#CCCCCC', linestyle=':')

# # # Set log scale on y axes
ax2.set_yscale('log')

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
ax2.legend(fontsize=18)
# Show figure (needed for running from command line)
plt.show()

# %%

# Save cleaned data to numpy arrays for comparison plot

np.save(os.path.relpath(main + 'wavelength/data/air_CL'), CL0)
np.save(os.path.relpath(main + 'wavelength/data/air_wls'), wls)


# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/papers/outer_materials/\
figures/data/arf/8tube'))

msk = ~np.isnan(CL0)

both = np.column_stack((wls[msk]*1e6, CL0[msk]))
np.savetxt(paper_path + '/N3config_ref0.dat', both, fmt='%.8f')
