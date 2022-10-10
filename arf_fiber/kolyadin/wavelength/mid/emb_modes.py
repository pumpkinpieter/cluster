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

# Set outer materials
scaling = 59.5
n_glass = 1.4388164768221814
n_air = 1.00027717
T_outer = 1.2 * 25.5 / scaling
n_mid = (n_glass + n_air) / 2
n0 = n_mid

outer_materials = [

    {'material': 'buffer',
     'n': n_mid,
     'T': .75 * T_outer,
     'maxh': .05},

    {'material': 'Outer',
     'n': n0,
     'T': T_outer,
     'maxh': .2}
]

# Embedding parameter array
wls = np.linspace(3.11, 3.6, 300) * 1e-6

# Search centers
inds = [85,   70,    60,    40,    20,    0,  100,  150,   175,   190,
        230,   250,  275,   299]
data = [5.148, 5.131, 5.118, 5.088, 5.05, 4.997, 5.16, 5.21, 5.236, 5.250,
        5.29, 5.317, 5.35, 5.400]
degree = 7
coeffs = np.polyfit(wls[inds], data, degree)
centers = sum([coeffs[-i-1] * wls**i for i in range(0, degree + 1)])

# PML strength
alpha = 5

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    if len(sys.argv) > 4:
        L, R = float(sys.argv[4]), float(sys.argv[5])
        save_index = np.where((L < wls) * (wls < R))[0]

    a = ARF2(name='kolyadin', poly_core=True, refine=ref,
             curve=max(p+1, 8), wl=wls[i],
             outer_materials=outer_materials)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', wavelength: ' + str(wls[i]) +
          '#'*8 + '\n', flush=True)

    center = a.L**2 * a.k**2 * (n0**2 - n_air**2) + centers[i]
    radius = 0.5
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
