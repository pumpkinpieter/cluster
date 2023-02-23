#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

if not os.path.isdir('outputs'):
    print('Making directory: outputs')
    os.makedirs('outputs')

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

# Center interpolation
wls = np.linspace(.5, 2, 200) * 1e-6
xs = np.array([wls[65], wls[75], wls[100], wls[125],
              wls[150], wls[175], wls[199]])
ys = np.array([4.7, 4.786, 4.9, 4.967, 5.018, 5.071, 5.12])
a, b, c, d = np.polyfit(xs, ys, 3)

# Wavelength array
wls = np.linspace(1, 2, 200) * 1e-6

# Search centers (need to shift later for material change)
centers = a * wls**3 + b * wls**2 + c * wls + d

# PML strength
alpha = 7.5

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    a = ARF2(name='fine_cladding', poly_core=True, refine=ref,
             curve=max(p+1, 8), shift_capillaries=False, wl=wls[i],
             outer_materials=outer_materials)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', wavelength: ' + str(wls[i]) +
          '#'*8 + '\n', flush=True)

    # Shift search center due to material change
    center = a.L**2 * a.k**2 * (n0**2 - n_air**2) + centers[i]
    radius = .05
    npts = 4

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

    np.save('outputs/p%i_alpha%.2f_wl%i' % (p, alpha, i), betas)
