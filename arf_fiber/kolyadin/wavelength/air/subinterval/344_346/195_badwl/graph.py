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

main = os.path.expanduser('~/local/convergence/arf_fiber/kolyadin/wavelength/\
air/subinterval/344_346/195_badwl')
path = os.path.relpath(main + '/outputs')

plt.figure(figsize=(20, 16))

fig = plt.gcf()
ax = plt.gca()

colors = ['blue', 'salmon']

for r in range(1):
    
    betas = np.load(path + '/ref'+str(r)+'all_betas.npy').imag
    # dofs = np.load(path + '/ref'+str(r)+'all_dofs.npy')
    CL = np.zeros(len(betas))
    
    for i,l in enumerate(betas):
        
        # Filter out bad values

        CL[i] = 10 * np.mean(l[np.where((l > 2e-5))]) / np.log(10)
    
    ax.plot(CL, 'o-', label='refinements: '+str(r), color=colors[r],
            linewidth=2.5, markersize=9,  markerfacecolor='white')

    # for i, dc in enumerate(zip(dofs, CL)):
    #     if r == 0:
    #         ax.annotate('p='+str(i), xy=dc, xytext=(-40, -50),
    #                     textcoords='offset points',
    #                     color=plt.gca().lines[-1].get_color(),
    #                     arrowprops=dict(arrowstyle="-",
    #                     connectionstyle="arc3",
    #                     color=plt.gca().lines[-1].get_color())
    #                     )
    #     elif r == 1:
    #         ax.annotate('p=' + str(i), xy=dc, xytext=(0, 30),
    #                     textcoords='offset points',
    #                     color=plt.gca().lines[-1].get_color(),
    #                     arrowprops=dict(arrowstyle="-",
    #                     connectionstyle="arc3",
    #                     color=plt.gca().lines[-1].get_color())
    #                     )

# xmin, xmax = ax.get_xlim()

# lim = 7.08052e-06
# ax.plot([xmin, xmax], [lim, lim], linestyle='dashdot', color='gray')


# plt.legend()

# plt.xlabel('ndofs')
# plt.ylabel('CL')

# plt.title('Kolyadin Fiber Fundamental Mode Convergence\n No polymer, \
# air in outer region.\n')

plt.yscale('log')
# plt.xscale('log')

# plt.yticks([1e-6, lim, 1e-4, 1e-2, 1], labels=['$10^{-6}$',
#                                                'lim CL = %.3e' % lim,
#                                                '$10^{-4}$',
#                                                '$10^{-2}$',
#                                                '$10^{0}$'])
# plt.xticks([10**5, 10**6])

# plt.grid(which='major', axis='y')
# plt.grid(which='major', axis='x')
# plt.grid(which='minor', axis='x', linestyle='--', linewidth=.5)

plt.show()
