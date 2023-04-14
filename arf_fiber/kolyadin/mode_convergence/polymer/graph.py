#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import os
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

SMALL_SIZE = 14
MEDIUM_SIZE = 18
BIGGER_SIZE = 22

plt.rc('font', size=MEDIUM_SIZE)         # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)   # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


main = os.path.expanduser('~/local/convergence/arf_fiber/kolyadin/modes/\
polymer/outputs')
path = os.path.relpath(main)

plt.figure(figsize=(20, 16))

fig = plt.gcf()
ax = plt.gca()

colors = ['blue', 'firebrick']
for r in range(2):
    betas = np.load(path + '/ref'+str(r)+'all_betas.npy').imag
    dofs = np.load(path + '/ref'+str(r)+'all_dofs.npy')

    # Filter out bad values

    B = np.where(betas != 0, betas, -1e99)
    BB = np.max(B, axis=1)

    CL = 20 * BB / np.log(10)
    ax.plot(dofs, CL, 'o-', label='refinements: '+str(r), color=colors[r],
            linewidth=2.5, markersize=9,  markerfacecolor='white')

    for i, dc in enumerate(zip(dofs, CL)):
        if r == 0:
            ax.annotate('p='+str(i), xy=dc, xytext=(-60, -50),
                        textcoords='offset points',
                        color=plt.gca().lines[-1].get_color(),
                        arrowprops=dict(arrowstyle="-",
                        connectionstyle="arc3",
                        color=plt.gca().lines[-1].get_color())
                        )
        elif r == 1:
            ax.annotate('p=' + str(i), xy=dc, xytext=(20, 50),
                        textcoords='offset points',
                        color=plt.gca().lines[-1].get_color(),
                        arrowprops=dict(arrowstyle="-",
                        connectionstyle="arc3",
                        color=plt.gca().lines[-1].get_color())
                        )

xmin, xmax = ax.get_xlim()

lim = 0.00326808
ax.plot([xmin, xmax], [lim, lim], linestyle='dashdot', color='gray')


plt.legend()

plt.xlabel('ndofs')
plt.ylabel('CL')

plt.title('Kolyadin Fiber Fundamental Mode Convergence\n Lossy polymer, \
with air in outer region\n n_poly = 1.5 + .1j\n')

plt.yscale('log')
plt.xscale('log')

plt.yticks([lim, 1e-3, 1e-1, 1e-2, 1], labels=['lim CL = %.3e' % lim,
                                               '$10^{-3}$',
                                               '$10^{-2}$',
                                               '$10^{-1}$',
                                               '$10^{0}$'])
plt.xticks([10**5, 10**6])

plt.grid(which='major', axis='y')
plt.grid(which='major', axis='x')
plt.grid(which='minor', axis='x', linestyle='--', linewidth=.5)

plt.show()
