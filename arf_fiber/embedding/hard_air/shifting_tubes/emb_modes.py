#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

if not os.path.isdir('outputs'):
    print('Making directory: outputs')
    os.makedirs('outputs')

if not os.path.isdir('modes'):
    print('Making directory: modes')
    os.makedirs('modes')

# Set outer materials
scaling = 15
n_glass = 1.4388164768221814
n_air = 1.00027717

n_hard_polymer = 1.56
T_hard_polymer = 10 / scaling

T_outer = 10 / scaling
T_buffer = 10 / scaling
n0 = n_air  # Sets buffer and outer region refractive index.

outer_materials = [

    {'material': 'hard_polymer',
     'n': n_hard_polymer,
     'T': T_hard_polymer,
     'maxh': .04},

    {'material': 'buffer',
     'n': n0,
     'T': T_buffer,
     'maxh': .4},

    {'material': 'Outer',
     'n': n0,
     'T': T_outer,
     'maxh': 1}
]

# Center, radius and span
center0 = 5.066
radius0 = .1
nspan = 4
npts = 4

# Embedding parameter array

E = np.linspace(0.002, .9999, 240)

# Linear fit for finding search centers
m, b = -0.2758566730320395, 5.07341374920433

# Seach centers
centers = b + m * E

# PML strength
alpha = 5

# Set result arrays
betas = np.zeros(nspan, dtype=complex)

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    if len(sys.argv) > 4:
        L, R = float(sys.argv[4]), float(sys.argv[5])
        save_index = np.where((L < E) * (E < R))[0]

    a = ARF2(name='fine_cladding', poly_core=True, refine=ref,
             curve=max(p+1, 8), shift_capillaries=True, e=E[i],
             outer_materials=outer_materials)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', e: ' + str(E[i]) + '#'*8 + '\n',
          flush=True)

    if E[i] < .4:
        center = center0
        radius = radius0

    else:
        center = centers[i]
        radius = .007

    beta, _, Es, _, _ = a.leakyvecmodes(ctr=center,
                                        rad=radius,
                                        alpha=alpha,
                                        nspan=nspan,
                                        npts=npts,
                                        p=p,
                                        niterations=12,
                                        nrestarts=0,
                                        stop_tol=1e-9,
                                        inverse='pardiso')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)

    np.save('outputs/e' + str(i), betas)

    if len(sys.argv) > 4 and i in save_index:
        a.save_mesh('modes/mesh_e' + str(i))
        a.save_modes(Es, 'modes/mode_e' + str(i))
