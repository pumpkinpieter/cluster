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


main = os.path.expanduser('~/local/convergence/arf_fiber/modes/vector_modes/\
HE11/outputs')
path = os.path.relpath(main)

plt.figure(figsize=(20, 16))

fig = plt.gcf()
ax = plt.gca()

pos1 = [(-40, 50), (-40, 50), (-40, 50), (-40, 50),
        (-40, 50), (-40, 50), (-40, 50), (-40, 50),
        (-40, 50), (-40, 50), (-40, 50), (-40, 50),
        (-40, 50), (-40, 50), (-40, 50),
        ]

pos2 = [(0, -40), (0, -40), (0, -40), (0, -40),
        (0, -40), (0, -40), (0, -40), (0, -40),
        (0, -40), (0, -40),
        ]
for r in range(2):
    betas = np.load(path + '/ref'+str(r)+'all_betas.npy').imag
    dofs = np.load(path + '/ref'+str(r)+'all_dofs.npy')

    # Filter out bad values

    B = np.where(betas != 0, betas, 1e99)
    BB = np.min(B, axis=1)

    CL = 20 * BB / np.log(10)
    ax.plot(dofs, CL, 'o-', label='refinements: '+str(r),
            linewidth=2.5, markersize=9,  markerfacecolor='white')

    if r == 0:
        CL1 = CL
        dof1 = dofs
    else:
        CL2 = CL
        dof2 = dofs

    for i, dc in enumerate(zip(dofs, CL)):
        if r == 0:
            ax.annotate('p='+str(i), xy=dc, xytext=pos1[i],
                        textcoords='offset points',
                        color=ax.lines[-1].get_color(),
                        arrowprops=dict(arrowstyle="-",
                        connectionstyle="arc3",
                        color=ax.lines[-1].get_color()),
                        )
        elif r == 1:
            ax.annotate('p='+str(i), xy=dc, xytext=pos2[i],
                        textcoords='offset points',
                        color=ax.lines[-1].get_color(),
                        arrowprops=dict(arrowstyle="-",
                        connectionstyle="arc3",
                        color=ax.lines[-1].get_color())
                        )

xmin, xmax = ax.get_xlim()

ax.plot([xmin, xmax], [.153, .153], linestyle='dashdot', color='gray')


plt.legend()

plt.xlabel('ndofs')
plt.ylabel('CL')

plt.title('Arf Fundamental Mode Convergence\n No polymer, \
air in outer region.\n')

plt.yscale('log')
plt.xscale('log')

plt.yticks([1e-5, .001, .1, .153,  10],
           labels=['$10^{-5}$', '$10^{-3}$', '$10^{-1}$',
                   'lim CL =.153',  '$10^{1}$'])
plt.xticks([10**5, 10**6])

plt.grid(which='major', axis='y')
plt.grid(which='major', axis='x')
plt.grid(which='minor', axis='x', linestyle='--', linewidth=.5)

plt.show()

# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/papers/arf_embedding/\
figures'))

both = np.column_stack((dof1, CL1))
np.savetxt(paper_path + '/coarse_cladding1.dat', both, fmt='%.8f')

both = np.column_stack((dof2, CL2))
np.savetxt(paper_path + '/coarse_cladding2.dat', both, fmt='%.8f')
