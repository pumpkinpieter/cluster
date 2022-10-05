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

main = os.path.expanduser('~/local/convergence/arf_fiber/clad_embed/')
path = os.path.relpath(main + 'shifting_tubes/outputs')

# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(30, 15))

es = np.linspace(0.002, .9999, 240)
T = np.linspace(10, 10.01, 11)

d = 4  # up to 11
z = plt.get_cmap('plasma')(np.linspace(0.2, .9, d+1))

for i in range(0, d):
    if i == 1:
        pass
    else:
        raw = np.load(path + '/T_'+str(i)+'all_e.npy').imag
        base = np.zeros_like(es)

        for j in range(len(es)):

            b = raw[j, :]
            c = np.where((b > 1e-3) * (b < 3), 1, 0)
            base[j] = np.mean(b, where=list(c))

        CL = 20 * base / np.log(10)

        ax1.plot(es, CL, '-',
                 label='%0.3f' % T[i],
                 linewidth=2.5, c=z[i])

# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("Embedding Sensitivity Profile\
 Changes \nDue to Cladding Thickness\n.",  fontsize=30)

# Set axis labels
ax1.set_xlabel("\nFraction of Capillary Tube Embedded", fontsize=20)
ax1.set_ylabel("CL", fontsize=25)

# Set up ticks and grids

plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)

ax1.xaxis.set_major_locator(MultipleLocator(.05))
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

plt.legend(title_fontsize=20,
           fontsize=16,
           ncol=2,
           title='Cladding Thickness',
           # bbox_to_anchor=(1.0, 1.0)
           )

# Show figure (needed for running from command line)
plt.show()

# # %%

# # Save cleaned data to numpy arrays for comparison plot

# np.save(os.path.relpath(main + 'data/extra_glass_fixedcap.npy'), CL)


# # %%

# # Save to .dat file for pgfplots

# paper_path = os.path.relpath(os.path.expanduser('~/papers/arf_embedding/\
# figures'))

# mask = ~np.isnan(CL)
# mask[14] = False

# # both = np.concatenate((es[mask][np.newaxis], CL[mask][np.newaxis]), axis=1)
# both = np.column_stack((es[mask], CL[mask]))
# # both = np.column_stack((x,y))
# np.savetxt(paper_path + '/fixed_capillaries.dat', both, fmt='%.8f')
