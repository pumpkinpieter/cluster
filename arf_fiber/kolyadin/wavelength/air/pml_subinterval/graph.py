#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
from os.path import expanduser, relpath
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

plt.close('all')

# Set up the figure and subplots
fig, ax1 = plt.subplots(1, 1, sharex=False, figsize=(25, 12))

wls = np.linspace(3.44, 3.46, 400) * 1e-6

ref = 0
p = 5
alpha = 2.5

dirname = '/ref%i_p%i_alpha%.2f' % (ref, p, alpha)

main = expanduser('~/local/convergence/arf_fiber/kolyadin/wavelength/air/\
pml_subinterval')
path = relpath(main + dirname)

raw = np.load(path + '/all.npy').imag
base = np.zeros_like(wls)

for j in range(len(wls)):

    b = raw[j, :]
    L = b[np.where((b > 1e-7) * (b < 1e0/8))]
    try:
        base[j] = np.min(L)
    except ValueError:
        base[j] = np.nan


CL = 20 * base / np.log(10)

nnan = ~np.isnan(CL)

ax1.plot(wls[nnan], CL[nnan],
         label=dirname,
         linewidth=1.5, markersize=0)

ref2 = 0
p2 = 5
alpha2 = 5

dirname2 = '/ref%i_p%i_alpha%.2f' % (ref2, p2, alpha2)

path2 = relpath(main + dirname2)

raw = np.load(path2 + '/all.npy').imag
base = np.zeros_like(wls)

for j in range(len(wls)):

    b = raw[j, :]
    L = b[np.where((b > 1e-7) * (b < 1e0/8))]
    try:
        base[j] = np.min(L)
    except ValueError:
        base[j] = np.nan


CL2 = 20 * base / np.log(10)

nnan2 = ~np.isnan(CL2)

ax1.plot(wls[nnan2], CL2[nnan2],
         label=dirname2,
         linewidth=1.5, markersize=0)

msk = nnan*nnan2

err = np.abs(CL - CL2) / CL

# Set Figure and Axes parameters ################################

# Set titles
# fig.suptitle("Wavelength Study: Air outside glass cladding",  fontsize=22)

# Set axis labels
ax1.set_xlabel("\nWavelength", fontsize=28)
ax1.set_ylabel("CL\n", fontsize=28)

# Set up ticks and grids

plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)

ax1.xaxis.set_major_locator(MultipleLocator(2e-9))
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


ax1.legend(fontsize=18)

# Show figure (needed for running from command line)
plt.show()

# Save cleaned data to numpy arrays for comparison plot

np.save(relpath(main + '/data' + dirname), CL)

# %%

# # Save cleaned data to numpy arrays for comparison plot

# np.save(relpath(main + 'wavelength/data/air_CL'), CL0)
# np.save(relpath(main + 'wavelength/data/air_wls'), wls)


# %%

# Save to .dat file for pgfplots

# paper_path = relpath(expanduser('~/papers/outer_materials/\
# figures/data/arf/8tube/pml_stability'))

# slide_path = relpath(expanduser('~/papers/outer_materials/slides/\
# figures/data/arf/8tube/pml_stability'))

# both = np.column_stack((wls[nnan]*1e6, CL[nnan]))
# name = '/cls_p%i_alpha%.2f.dat' % (p, alpha)
# np.savetxt(paper_path + name, both, fmt='%.8f')
# np.savetxt(slide_path + name, both, fmt='%.8f')

# both = np.column_stack((wls[nnan2]*1e6, CL2[nnan2]))
# name = '/cls_p%i_alpha%.2f.dat' % (p2, alpha2)
# np.savetxt(paper_path + name, both, fmt='%.8f')
# np.savetxt(slide_path + name, both, fmt='%.8f')


# both = np.column_stack((wls[msk]*1e6, err[msk]))
# name = '/err_p%i_alphas_%.2f_%.2f.dat' % (p, alpha, alpha2)
# np.savetxt(paper_path + name, both, fmt='%.8f')
# np.savetxt(slide_path + name, both, fmt='%.8f')
