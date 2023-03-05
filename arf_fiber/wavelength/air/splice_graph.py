#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 23:56:36 2023

@author: pv
"""


import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
matplotlib.use("Qt5Agg")

main = os.path.expanduser('~/local/convergence/arf_fiber/wavelength/air/')
path = os.path.relpath(main + 'outputs')

CL_main = np.load(os.path.relpath(main+'data/poletti_CLs.npy'))
wl_main = np.load(os.path.relpath(main+'data/poletti_wls.npy'))*1e6

N0_CLs = np.load(os.path.relpath(main+'../glass/data/poletti_N0_CLs.npy'))
N0_wls = np.load(os.path.relpath(main+'../glass/data/poletti_N0_wls.npy'))*1e6

CL_sub = np.load(os.path.relpath(main+'data/poletti_sub_CLs.npy'))
wl_sub = np.load(os.path.relpath(main+'data/poletti_sub_wls.npy'))*1e6

Wl, Wr = 400, -351
L = np.where(wl_main <= wl_sub[Wl])
R = np.where((wl_main >= wl_sub[Wr]))
N0_sub_msk = np.where((N0_wls > wl_sub[Wl-100]) * (N0_wls < wl_sub[Wr+100]))


all_wl = np.concatenate((wl_main[L], wl_sub, wl_main[R]))
all_CL = np.concatenate((CL_main[L], CL_sub, CL_main[R]))

# %%
plt.close('all')

# Set up the figure and subplots
fig, (ax1) = plt.subplots(1, 1, sharex=False, figsize=(32, 14))

# Plot the data
ax1.plot(wl_main[L], CL_main[L], color='blue',
         linewidth=1.5, markersize=.4)
ax1.plot(wl_sub[Wl:Wr], CL_sub[Wl:Wr], color='g',
         linewidth=1.5, markersize=.4)
ax1.plot(wl_main[R], CL_main[R], color='blue',
         linewidth=1.5, markersize=.4)

ax1.set_ylim(7e-6, 1e1)

# Plot inset data
axin = ax1.inset_axes([.03, .04, .94, .32])
axin.plot(wl_sub[Wl:Wr], CL_sub[Wl:Wr],
          color='g', linewidth=1.5, markersize=.4)

axin.set_ylim(.8*np.min(CL_sub), 1.5*np.max(CL_sub))
axin.autoscale(enable=True, axis='x', tight=True)


# ax1.indicate_inset([1.3e-6, 1.3e-3, .1e-6, 6], axin, edgecolor="black")
ax1.indicate_inset_zoom(axin, edgecolor="black")
# Set Figure and Axes parameters

# Set titles
fig.suptitle("Wavelength Study: Air outside glass cladding, Poletti Fiber",
             fontsize=26)

# Set axis labels
ax1.set_xlabel("\nWavelength", fontsize=28)
ax1.set_ylabel("CL\n", fontsize=28)


plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=22)

ax1.xaxis.set_major_locator(MultipleLocator(5e-2))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.yaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(AutoMinorLocator(1))
ax1.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax1.grid(which='minor', color='#CCCCCC', linestyle=':')

# # Set log scale on y axes
ax1.set_yscale('log')
axin.set_yscale('log')

axin.set_xticks([])
axin.set_yticks([])

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
# ax1.legend(fontsize=25)
# Show figure (needed for running from command line)
plt.show()

# %%
plt.close('all')

# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False,
                               gridspec_kw={'height_ratios': [1.75, 1]},
                               figsize=(34, 16))

# Plot the data
ax1.plot(wl_main[L], CL_main[L], color='blue',
         linewidth=1., markersize=.4, label='$N1$ Model')
ax1.plot(wl_sub[Wl:Wr], CL_sub[Wl:Wr],
         color='g', linewidth=1., markersize=.4, label='$N1$ Subinterval')
ax1.plot(wl_main[R], CL_main[R], color='blue',
         linewidth=1., markersize=.4)

ax1.plot(N0_wls, N0_CLs, color='firebrick',
         linewidth=2., markersize=.4, label='$N0$ Model')

ax1.set_ylim(7e-4, 1e1)


ax2.plot(wl_sub[Wl:Wr], CL_sub[Wl:Wr], color='g', linewidth=1.5,
         # marker='+',
         markersize=4)

msk = np.where((N0_wls >= wl_sub[Wl-100]) * (N0_wls <= wl_sub[Wr+100]))

ax2.plot(N0_wls[msk], N0_CLs[msk], color='firebrick',
         linewidth=2, markersize=.4)

# Plot resonant spikes
m, M = ax1.get_ylim()
d = 9.999999999999999
n1, n2 = 1.00027717, 1.4388164768221814
spikes = [2 * n1 * d / m * ((n2/n1)**2 - 1)**.5 for m in range(11, 21)]

for i, spike in enumerate(spikes):
    if i == 0:
        ax1.plot([spike, spike], [m, M], linewidth=2, label='Spike',
                 color='orange', linestyle='dashed')
    else:
        ax1.plot([spike, spike], [m, M], linewidth=2,
                 color='orange', linestyle='dashed')

ax2.plot([spikes[4], spikes[4]], [m, M], linewidth=2,
         color='orange', linestyle='dashed')


ax2.set_ylim(.8*np.min(CL_sub), 1.5*np.max(CL_sub))
ax2.set_xlim(wl_sub[Wl], wl_sub[Wr])
# ax2.autoscale(enable=True, axis='x', tight=True)
# ax1.autoscale(enable=True, axis='x', tight=True)
ax1.set_xmargin(0.03)

fig.suptitle("Spectral Loss Profile: 6-Tube ARF",
             fontsize=36)

# Set Figure and Axes parameters

ax1.indicate_inset_zoom(ax2, edgecolor="black")

# Set axis labels
ax2.set_xlabel("Wavelength [$\\mu m$]", fontsize=28, labelpad=30)

fig.text(0.025, 0.5, "Confinement Loss [dB/km]", ha='center',
         va='center', rotation='vertical', fontsize=28)

plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=22)

ax1.xaxis.set_major_locator(MultipleLocator(5e-2))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.yaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_minor_locator(AutoMinorLocator(1))
ax1.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax1.grid(which='minor', color='#CCCCCC', linestyle=':')

# # Set log scale on y axes
ax1.set_yscale('log')
ax2.set_yscale('log')

ax2.xaxis.set_major_locator(MultipleLocator(1e-2))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax2.yaxis.set_major_locator(MultipleLocator(1))
# ax2.yaxis.set_minor_locator(AutoMinorLocator(1))
ax2.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax2.grid(which='minor', color='#CCCCCC', linestyle=':')

# Turn on subplot tool when graphing to allow finer control of spacing
# plt.subplot_tool(fig)

# After fine tuning, these are the values we want (use export from tool)
plt.subplots_adjust(top=0.92,
                    bottom=0.102,
                    left=0.062,
                    right=0.978,
                    hspace=0.188,
                    wspace=0.205)

leg = ax1.legend(fontsize=18, ncols=2, fancybox=False,
                 loc='lower right')

for line in leg.get_lines():
    line.set_linewidth(3)

# Show figure (needed for running from command line)
plt.show()

# %%

# # Save cleaned data to numpy arrays for comparison plot
# np.save(os.path.relpath(main + 'data/polleti_all_CLs'), all_CL)
# np.save(os.path.relpath(main + 'data/polleti_all_wls'), all_wl)


# %%

# Save to .dat file for pgfplots

# paper_path = os.path.relpath(os.path.expanduser('~/papers/outer_materials/\
# figures/data/arf/6tube/'))

# both = np.column_stack((wl_main[L], CL_main[L]))
# np.savetxt(paper_path + '/C1L.dat', both, fmt='%.8f')

# both = np.column_stack((wl_sub[Wl:Wr], CL_sub[Wl:Wr]))
# np.savetxt(paper_path + '/C1_subinterval.dat', both, fmt='%.8f')

# both = np.column_stack((wl_main[R], CL_main[R]))
# np.savetxt(paper_path + '/C1R.dat', both, fmt='%.8f')

# both = np.column_stack((N0_wls, N0_CLs))
# np.savetxt(paper_path + '/C0.dat', both, fmt='%.8f')

# both = np.column_stack((N0_wls[N0_sub_msk], N0_CLs[N0_sub_msk]))
# np.savetxt(paper_path + '/C0_subinterval.dat', both, fmt='%.8f')

# msk = np.where((wl_sub > 1.3535)*(wl_sub < 1.3555))

# both = np.column_stack((wl_sub[msk], CL_sub[msk]))
# np.savetxt(paper_path + '/spike_subint.dat', both, fmt='%.8f')
