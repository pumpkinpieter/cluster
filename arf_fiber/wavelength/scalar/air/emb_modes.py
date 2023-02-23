#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

if not os.path.isdir('outputs'):
    print('Making directory: outputs')
    os.makedirs('outputs')

# if not os.path.isdir('modes'):
#     print('Making directory: modes')
#     os.makedirs('modes')

# Set result arrays
nspan = 4
betas = np.zeros(nspan, dtype=complex)

# Set outer materials
scaling = 15
n_glass = 1.4388164768221814
n_air = 1.00027717

T_outer = 10 / scaling
n0 = n_glass  # Sets buffer and outer region refractive index.

outer_materials = [

    {'material': 'Outer',
     'n': n0,
     'T': T_outer,
     'maxh': .1}
]


# Wavelength array
wls = np.linspace(1, 2, 200) * 1e-6

# Center interpolation for C1 fiber
ys = np.array([2.204, 2.225,  2.236, 2.246, 2.256])

xs = np.array([wls[0], wls[50], wls[100], wls[150], wls[199]])

a, b, c, d = np.polyfit(xs, ys, 3)
centers = a * wls**3 + b * wls**2 + c * wls + d

# Search centers  for C1 fiber (need to shift later for material change)
centers = a * wls**3 + b * wls**2 + c * wls + d

# PML strength
alpha = 5

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    # if len(sys.argv) > 4:
    #     L, R = float(sys.argv[4]), float(sys.argv[5])
    #     save_index = np.where((L < wls) * (wls < R))[0]

    A = ARF2(name='fine_cladding', poly_core=True, refine=ref,
             curve=max(p+1, 8), shift_capillaries=False, wl=wls[i])

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', wavelength: ' + str(wls[i]) +
          '#'*8 + '\n', flush=True)

    # Shift search center due to material change
    center = centers[i]
    radius = .01
    npts = 4

    _, y, _, beta, _, _ = A.leakymode(p,
                                      ctr=center,
                                      rad=radius,
                                      alpha=alpha,
                                      nspan=nspan,
                                      npts=npts,
                                      niterations=12,
                                      nrestarts=0,
                                      stop_tol=1e-9,
                                      inverse='pardiso')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)

    np.save('outputs/e' + str(i), betas)

    # if len(sys.argv) > 4 and i in save_index:
    #     a.save_mesh('modes/mesh_e' + str(i))
    #     a.save_modes(Es, 'modes/mode_e' + str(i))
