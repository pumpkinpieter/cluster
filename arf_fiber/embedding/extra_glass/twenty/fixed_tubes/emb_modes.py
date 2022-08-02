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

T_extra = 20 / scaling
T_buffer = 10 / scaling
T_outer = 10 / scaling
n0 = n_air  # Sets buffer and outer region refractive index.

outer_materials = [
    {'material': 'extra_glass',
     'n': n_glass,
     'T': T_extra,
     'maxh': .05},

    {'material': 'buffer',
     'n': n0,
     'T': T_buffer,
     'maxh': .1},

    {'material': 'Outer',
     'n': n0,
     'T': T_outer,
     'maxh': 1}
]

# Set result arrays
nspan = 4
betas = np.zeros(nspan, dtype=complex)

# Embedding parameter array
E = np.linspace(0.002, .9999, 240)

# PML strength
alpha = 5

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    if len(sys.argv) > 4:
        L, R = float(sys.argv[4]), float(sys.argv[5])
        save_index = np.where((L < E) * (E < R))[0]

    a = ARF2(name='fine_cladding', poly_core=True, refine=ref,
             curve=max(p+1, 8), shift_capillaries=False, e=E[i],
             outer_materials=outer_materials)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', e: ' + str(E[i]) + '#'*8 + '\n',
          flush=True)

    center = a.L**2 * a.k**2 * (n0**2 - n_air**2) + 5.066
    radius = .1
    npts = 4
    alpha = 5

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
