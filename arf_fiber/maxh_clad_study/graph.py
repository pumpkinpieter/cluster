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


main = os.path.expanduser('~/local/convergence/arf_fiber/maxh_clad_study/\
outputs')
path = os.path.relpath(main)

plt.figure(figsize=(22, 12))

fig = plt.gcf()
ax = plt.gca()

maxhs = ['0.0', '0.1']

for maxh in maxhs:
    betas = np.load(path + '/maxh_'+maxh+'/ref0_all_betas.npy').imag
    dofs = np.load(path + '/maxh_'+maxh+'/ref0_all_dofs.npy')

    # Filter out bad values

    B = np.where(betas > 0, betas, 1e99)
    BB = np.min(B, axis=1)

    CL = 20 * BB / np.log(10)
    ax.plot(dofs, CL, 'o-', label='maxh: ' + maxh,
            linewidth=2.5, markersize=5)
# for maxh in ['0.1']:
#     betas = np.load(path + '/maxh_'+maxh+'/ref1_all_betas.npy').imag
#     dofs = np.load(path + '/maxh_'+maxh+'/ref1_all_dofs.npy')

#     # Filter out bad values

#     B = np.where(betas > 0, betas, 1e99)
#     BB = np.min(B, axis=1)

#     CL = 20 * BB / np.log(10)
#     ax.plot(dofs, CL, 'o-', label='maxh: ' + maxh,
#             linewidth=2.5, markersize=5)

xmin, xmax = ax.get_xlim()

ax.plot([xmin, xmax], [.153, .153], linestyle='dashdot', color='gray')


plt.legend()

plt.xlabel('ndofs')
plt.ylabel('CL')

plt.title('Arf Fundamental Mode Convergence\n No polymer, \
air in outer region.\n')

plt.yscale('log')
plt.xscale('log')

plt.yticks([.1, .153, 1, 10], labels=['.1', 'lim CL =.153', '1', '10'])
plt.xticks([10**5, 10**6])

plt.grid(which='major', axis='y')
plt.grid(which='major', axis='x')
plt.grid(which='minor', axis='x', linestyle='--', linewidth=.5)

plt.show()

# %%

# plt.savefig('/home/pv/eps_test/graph.eps', format='eps')
# fig.savefig('/home/pv/eps_test/graph.svg', format='svg', dpi=1200)

# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/papers/outer_materials/\
figures/data/mesh_maxh'))

ref = 0

maxhs = ['0.1']
for i, maxh in enumerate(maxhs):
    betas = np.load(path + '/maxh_'+maxh+'/ref'+str(ref)+'_all_betas.npy').imag
    dofs = np.load(path + '/maxh_'+maxh+'/ref'+str(ref)+'_all_dofs.npy')

    # Filter out bad values

    B = np.where(betas > 0, betas, 1e99)
    BB = np.min(B, axis=1)

    CL = 20 * BB / np.log(10)
    both = np.column_stack((dofs, CL))
    np.savetxt(paper_path + '/maxh_'+str(maxh)+'_ref' +
               str(ref)+'.dat', both, fmt='%.8f')

# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/papers/outer_materials/\
figures/data/mesh_maxh'))

ref = 1

maxhs = ['0.1']
for i, maxh in enumerate(maxhs):
    betas = np.load(path + '/maxh_'+maxh+'/ref'+str(ref)+'_all_betas.npy').imag
    dofs = np.load(path + '/maxh_'+maxh+'/ref'+str(ref)+'_all_dofs.npy')

    # Filter out bad values

    B = np.where(betas > 0, betas, 1e99)
    BB = np.min(B, axis=1)

    CL = 20 * BB / np.log(10)
    both = np.column_stack((dofs, CL))
    np.savetxt(paper_path + '/maxh_'+str(maxh)+'_ref' +
               str(ref)+'.dat', both, fmt='%.8f')
