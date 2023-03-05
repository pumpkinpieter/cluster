#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
from os.path import relpath, expanduser
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator, LogLocator)

plt.close('all')

P = [5, 6]
ref = 0
alphas = [2.5, 5, 7.5, 10]

main = relpath(expanduser('~/local/convergence/arf_fiber/kolyadin/wavelength/\
air/pml_subinterval/data'))

wls = np.linspace(3.44, 3.46, 400) * 1e-6


# Set up the figure and subplots
fig, ax = plt.subplots(len(P), 1, sharex=False, figsize=(22, 18))

# Plot the data
for i, p in enumerate(P):
    for alpha in alphas:
        try:
            name = '/ref%i_p%i_alpha%.2f.npy' % (ref, p, alpha)
            CL = np.load(main + name)

            ax[i].plot(wls, CL, label='alpha=%.2f' % alpha,
                       linewidth=1.5)
        except FileNotFoundError:
            pass

        ax[i].legend(fontsize=18)
        ax[i].set_title('ref = %i, p = %i' % (ref, p),
                        fontsize=22)
        ax[i].set_yscale('log')


# Set up the figure and subplots
fig2, ax2 = plt.subplots(2, 1, sharex=False,
                         gridspec_kw={'height_ratios': [2.5, 1]},
                         figsize=(35, 18))

# Plot the data

p = 6
i = 1

name1 = '/ref%i_p%i_alpha%.2f.npy' % (ref, p, alphas[i])
name2 = '/ref%i_p%i_alpha%.2f.npy' % (ref, p, alphas[i+1])

CL1, CL2 = np.load(main + name1), np.load(main + name2)
res = np.abs(CL2 - CL1) / CL1 * 100

ax2[0].plot(wls, CL1, label='alpha = %.2f' % (alphas[i]), color='blue',
            marker='o',
            linewidth=3, markersize=9)

ax2[0].plot(wls, CL2, label='alpha = %.2f' % alphas[i+1], color='orange',
            marker='o',
            linewidth=0, markersize=8)

ax2[1].plot(wls, res, color='green',
            linewidth=2, label='relative error', markersize=1)

ax2[0].legend(fontsize=18)
ax2[0].set_yscale('log')

ax2[1].legend(fontsize=18)
ax2[1].set_yscale('log')

L, R = ax2[1].get_xlim()
ax2[1].set_xlim(L, R)
ax2[1].plot([L, R], [1, 1], color='gray', linestyle='dashed',
            linewidth=2)


# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("PML stability: compare alpha at fixed order",  fontsize=26)
fig2.suptitle("PML stability: compare alphas at order %i\n" % p,  fontsize=40)


# Set axis labels
ax2[1].set_xlabel("\nWavelength", fontsize=30)
ax2[0].set_ylabel("CL\n", fontsize=30)
ax2[1].set_ylabel("% Error\n", fontsize=30)

# Set up ticks and grids

plt.rc('xtick', labelsize=26)
plt.rc('ytick', labelsize=26)

ax2[0].xaxis.set_major_locator(MultipleLocator(2e-9))
ax2[0].xaxis.set_minor_locator(AutoMinorLocator(5))
# ax2[0].yaxis.set_major_locator(MultipleLocator(1))
# ax2[0].yaxis.set_minor_locator(AutoMinorLocator(0))
ax2[0].grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax2[0].grid(which='minor', color='#CCCCCC', linestyle=':')

# # # Set log scale on y axes
ax2[0].set_yscale('log')
ax2[1].set_yscale('log')


ax2[1].xaxis.set_major_locator(MultipleLocator(2e-9))
ax2[1].xaxis.set_minor_locator(AutoMinorLocator(5))

y_major = LogLocator(base=10)
y_minor = LogLocator(base=10, subs=(2.0, 3., 4., 5., 6., 7., 8., 9.))

ax2[1].yaxis.set_major_locator(y_major)
ax2[1].yaxis.set_minor_locator(y_minor)

ax2[1].grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax2[1].grid(which='minor', color='#CCCCCC', linestyle=':')

# Set log scale on y axes

# Turn on subplot tool when graphing to allow finer control of spacing
# plt.subplot_tool(fig2)

# After fine tuning, these are the values we want (use export from tool)
fig2.subplots_adjust(top=0.91,
                     bottom=0.11,
                     left=0.08,
                     right=0.94,
                     hspace=0.25,
                     wspace=0.2)

ax2[1].set_ylim(1e-4, 1e2)
# ax2[0].set_xlim(3.1e-6, 3.61e-6)
ax2[0].legend(fontsize=35)
ax2[1].legend(fontsize=35, loc='upper right')
# Show figure (needed for running from command line)
plt.show()
