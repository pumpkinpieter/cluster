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
path = os.path.relpath(main + 'polymerN1/k_0.002')

exact = -(np.load(main + 'polymerN1/exact_betas/\
k_002_scaled_betas.npy')/15e-6).imag
exact_CL = 20 * exact[0] / np.log(10)

plt.figure(figsize=(20, 16))

fig = plt.gcf()
ax = plt.gca()

for r in range(2):
    betas = np.load(path + '/ref'+str(r)+'all_betas.npy').imag
    dofs = np.load(path + '/ref'+str(r)+'all_dofs.npy')

    # Filter out bad values

    B = np.where(betas > 0, betas, 1e99)
    BB = np.min(B, axis=1)

    CL = 20 * BB / np.log(10)
    ax.plot(dofs, CL, 'o-', label='refinement: '+str(r),
            linewidth=2.5, markersize=9,  markerfacecolor='white')

    for i, dc in enumerate(zip(dofs, CL)):
        if r == 0:
            ax.annotate('p='+str(i), xy=dc, xytext=(-40, 80),
                        color=plt.gca().lines[-1].get_color(),
                        textcoords='offset points', fontsize=18,
                        arrowprops=dict(arrowstyle="-",
                        connectionstyle="arc3", color='blue')
                        )
        elif r == 1:
            ax.annotate('p=' + str(i), xy=dc, xytext=(0, -90),
                        textcoords='offset points', fontsize=18,
                        color=plt.gca().lines[-1].get_color(),
                        arrowprops=dict(arrowstyle="-",
                        connectionstyle="arc3", color='orange')
                        )

xmin, xmax = ax.get_xlim()

ax.plot([xmin, xmax], [exact_CL, exact_CL], linestyle='--', color='gray',
        label='exact loss', linewidth=2)


plt.legend(fontsize=18)

plt.xlabel('ndofs', fontsize=25)
plt.ylabel('CL', fontsize=25)

plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)

plt.title('Hollow Core Bragg Fiber: $N_1$ Configuration\n\
Fundamental Mode Convergence\n', fontsize=35)

plt.yscale('log')
plt.xscale('log')

s = 'true: {ex:.1f}'.format(ex=exact_CL)

# m, M = ax.get_ylim()
# m = np.floor(np.log10(m))
# M = np.ceil(np.log10(M))
# pows = np.arange(m, M+1, 1)
# tick_list = list(np.sort(np.concatenate((10**pows, [exact_CL]))))

# ax.set_yticks(tick_list,
#               labels=[str(s) for s in tick_list],
#               fontsize=18)

ax.set_yticks([100, exact_CL, 10**3, 2*10**3], labels=['$10^2$', s, '',
                                                       '$2\\cdot10^3$'])
# ax.set_yticks(list(ax.get_yticks()) + [exact_CL],
#               labels=ax.get_yticklabels()+[s])

# plt.xticks([10**5, 10**6], fontsize=16)

plt.grid(which='major', axis='y')
plt.grid(which='major', axis='x')
plt.grid(which='minor', axis='x', linestyle='--', linewidth=.5)
plt.grid(which='minor', axis='y', linestyle='--', linewidth=.5)

plt.show()
