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

main = os.path.expanduser('~/local/convergence/bragg_fiber/mode_convergence/')
path = os.path.relpath(main + 'N3/outputs')

exact = -(np.load(main + 'N3/exact_scaled_betas.npy')/15e-6).imag
exact_CL = 20 * exact[0] / np.log(10)

plt.figure(figsize=(20, 16))

fig = plt.gcf()
ax = plt.gca()

for r in range(2):
    betas = np.load(path + '/ref'+str(r)+'all_betas.npy').imag
    dofs = np.load(path + '/ref'+str(r)+'all_dofs.npy')

    # Filter out bad values

    B = np.where(betas != 0, betas, 1e99)
    BB = np.min(B, axis=1)

    CL = 20 * BB / np.log(10)
    ax.plot(dofs[1:], CL[1:], 'o-', label='refinement: '+str(r),
            linewidth=2.5, markersize=9,  markerfacecolor='white')

    for i, dc in enumerate(zip(dofs[1:], CL[1:])):
        if r == 0:
            ax.annotate('p='+str(i+1), xy=dc, xytext=(-40, 60),
                        color=plt.gca().lines[-1].get_color(),
                        textcoords='offset points', fontsize=18,
                        arrowprops=dict(arrowstyle="-",
                        connectionstyle="arc3", color='blue')
                        )
        elif r == 1:
            ax.annotate('p=' + str(i+1), xy=dc, xytext=(0, -60),
                        textcoords='offset points', fontsize=18,
                        color=plt.gca().lines[-1].get_color(),
                        arrowprops=dict(arrowstyle="-",
                        connectionstyle="arc3", color='orange')
                        )

xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()

ax.plot([xmin, xmax], [exact_CL, exact_CL], linestyle='--', color='gray',
        label='exact loss')


plt.legend(fontsize=18, loc='lower left')

plt.xlabel('ndofs', fontsize=25)
plt.ylabel('CL', fontsize=25)

plt.title('Hollow Core Bragg Fiber: $N_3$ Configuration\n\
Fundamental Mode Convergence\n', fontsize=35)

# plt.yscale('log')
plt.xscale('log')

s = 'exact: {ex:.3f}'.format(ex=exact_CL)

yticks_base = list(np.round(np.linspace(.99*ymin, 1.9*ymax, 6),3))
labels = [str(n) for n in yticks_base]

ax.set_yticks(yticks_base + [exact_CL],
              labels=labels+[s],
              fontsize=18)

plt.xticks([10**5, 10**6], fontsize=16)

plt.grid(which='major', axis='y')
plt.grid(which='major', axis='x')
plt.grid(which='minor', axis='x', linestyle='--', linewidth=.5)
plt.grid(which='minor', axis='y', linestyle='--', linewidth=.5)

plt.show()
