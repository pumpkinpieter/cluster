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

# Set result arrays
nspan = 4
betas = np.zeros(nspan, dtype=complex)

# Embedding parameter array
wls = np.linspace(3.11, 3.6, 800) * 1e-6

inds = [1,    50,   100,   150,   200,  250,   299,   400,   500,   600,
        700,  799]
data = [5.1525, 5.17, 5.187, 5.202, 5.217, 5.23, 5.245, 5.275, 5.314, 5.362,
        5.422, 5.528]

degree = 7
coeffs = np.polyfit(wls[inds], data, degree)
centers = sum([coeffs[-i-1] * wls**i for i in range(0, degree + 1)])

n_poly = 1.5 + .1j
n_buffer = 1.00027717
n0 = n_buffer

scaling = 59.5
T_cladding = 1.2 * 25.5 / scaling

T_poly = .5 * T_cladding
T_buffer = .5 * T_cladding
T_outer = .75 * T_cladding

# PML strength
alpha = 5

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    if len(sys.argv) > 4:
        L, R = float(sys.argv[4]), float(sys.argv[5])
        save_index = np.where((L < wls) * (wls < R))[0]

    outer_materials = [

        {'material': 'poly',
         'n': n_poly,
         'T': T_poly,
         'maxh': .03},

        {'material': 'buffer',
         'n': n_buffer,
         'T': T_buffer,
         'maxh': .2},

        {'material': 'Outer',
         'n': n0,
         'T': T_outer,
         'maxh': .2}
    ]

    a = ARF2(name='kolyadin', poly_core=True, refine=ref,
             curve=max(p+1, 8), wl=wls[i],
             outer_materials=outer_materials)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', wavelength: ' + str(wls[i]) +
          '#'*8 + '\n', flush=True)

    center = centers[i]
    radius = 0.05
    npts = 4

    beta, _, Es, _, _ = a.leakyvecmodes(ctr=center,
                                        rad=radius,
                                        alpha=alpha,
                                        nspan=nspan,
                                        npts=npts,
                                        p=p,
                                        niterations=10,
                                        nrestarts=0,
                                        stop_tol=1e-9,
                                        inverse='pardiso')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)

    np.save('outputs/e' + str(i), betas)

    if len(sys.argv) > 4 and i in save_index:
        a.save_mesh('modes/mesh_e' + str(i))
        a.save_modes(Es, 'modes/mode_e' + str(i))
