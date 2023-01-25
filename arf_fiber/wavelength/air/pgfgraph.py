#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:08:11 2023

@author: pv
"""


import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import matplotlib

plt.close('all')

# Set parameters for saving to pgf
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.width': 0.2,
    'xtick.minor.width': 0.2,
    'ytick.major.width': 0.2,
    'ytick.minor.width': 0.2,
    'xtick.color': 'gray',
    'ytick.color': 'gray',
    'xtick.labelcolor': 'black',
    'ytick.labelcolor': 'black',
    'axes.labelpad': 10,
})
matplotlib.rcParams['axes.linewidth'] = 0.4

# Load and prepare data
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

all_wl = np.concatenate((wl_main[L], wl_sub, wl_main[R]))
all_CL = np.concatenate((CL_main[L], CL_sub, CL_main[R]))

# Set up the figure and subplots
s = 6.50127  # \textwidth from latex document (found using layouts package)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False,
                               gridspec_kw={'height_ratios': [1.75, 1]},
                               figsize=(s, s*14/24))

# Plot the data
ax1.plot(wl_main[L], CL_main[L], color='blue',
         linewidth=.2, markersize=.4,
         label='Air Model')

ax1.plot(wl_sub[Wl:Wr], CL_sub[Wl:Wr], color='g',
         linewidth=.3, markersize=.4,
         label='Air Subinterval')

ax1.plot(wl_main[R], CL_main[R], color='blue',
         linewidth=.2, markersize=.4)

ax1.plot(N0_wls, N0_CLs, color='firebrick',
         linewidth=.4, markersize=.4,
         label='Glass Model')

# Plot inset data
ax2.plot(wl_sub[Wl:Wr], CL_sub[Wl:Wr], color='g',
         linewidth=.4)

msk = np.where((N0_wls >= wl_sub[Wl-100]) * (N0_wls <= wl_sub[Wr+100]))

ax2.plot(N0_wls[msk], N0_CLs[msk], color='firebrick',
         linewidth=.4, markersize=.4)

# Set limits before plotting spikes and creating inset window
ax1.set_ylim(1e-3, 1e1)
ax2.set_ylim(.8*np.min(CL_sub), 1.5*np.max(CL_sub))
ax2.set_xlim(wl_sub[Wl], wl_sub[Wr])

# Plot resonant spikes
m, M = ax1.get_ylim()
d = 9.999999999999999
n1, n2 = 1.00027717, 1.4388164768221814
spikes = [2 * n1 * d / m * ((n2/n1)**2 - 1)**.5 for m in range(11, 21)]

for i, spike in enumerate(spikes):
    if i == 0:
        ax1.plot([spike, spike], [m, M], linewidth=.5, label='Spike',
                 color='orange', linestyle='dashed')
    else:
        ax1.plot([spike, spike], [m, M], linewidth=.5,
                 color='orange', linestyle='dashed')

ax2.plot([spikes[4], spikes[4]], [m, M], linewidth=.5,
         color='orange', linestyle='dashed')

# Add inset lines and rectangle
rect, lines = ax1.indicate_inset_zoom(ax2, edgecolor="black",
                                      linewidth=.1)
ax1.autoscale(enable=True, axis='x', tight=True)

for line in lines:
    line.set(linewidth=.1)

# Set Figure and Axes parameters

# Set axis labels
ax2.set_xlabel("Wavelength [$\\mu \\mbox{m}$]", fontsize=8)

fig.text(0.02, 0.5, "Confinement Loss [dB/km]", ha='center',
         va='center', rotation='vertical',
         fontsize=8)

plt.rc('xtick', labelsize=7)
plt.rc('ytick', labelsize=7)

plt.rc('xtick', labelsize=7)
plt.rc('ytick', labelsize=7)

ax1.xaxis.set_major_locator(MultipleLocator(1e-1))
# ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax1.yaxis.set_major_locator(MultipleLocator(10))
# ax1.yaxis.set_minor_locator(AutoMinorLocator(5))
ax1.grid(which='major', color='#CCCCCC', linewidth=.15, linestyle='--')
ax1.grid(which='minor', color='#CCCCCC', linewidth=.1, linestyle=':')

# # Set log scale on y axes
ax1.set_yscale('log')
ax2.set_yscale('log')

ax2.xaxis.set_major_locator(MultipleLocator(1e-2))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax2.yaxis.set_major_locator(MultipleLocator(1))
# ax2.yaxis.set_minor_locator(AutoMinorLocator(1))
ax2.grid(which='major', color='#CCCCCC', linewidth=.15, linestyle='--')
ax2.grid(which='minor', color='#CCCCCC', linewidth=.1, linestyle=':')


# After fine tuning, these are the values we want (use export from tool)
plt.subplots_adjust(top=0.96,
                    bottom=0.102,
                    left=0.09,
                    right=0.94,
                    hspace=0.188,
                    wspace=0.205)

leg = ax1.legend(fontsize=3, ncols=1, fancybox=False)

for line in leg.get_lines():
    line.set_linewidth(.8)

fig.savefig('/home/pv/papers/outer_materials/figures/tikz\
/wlstudies/zoomed_subint.pgf')
