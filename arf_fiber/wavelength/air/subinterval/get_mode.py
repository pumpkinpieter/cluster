#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

if not os.path.isdir('modes'):
    print('Making directory: modes')
    os.makedirs('modes')

# Set result arrays
nspan = 4
betas = np.zeros(nspan, dtype=complex)

# Center interpolation
wls = np.linspace(.5, 2, 200) * 1e-6
xs = np.array([wls[65], wls[75], wls[100], wls[125],
              wls[150], wls[175], wls[199]])
ys = np.array([4.7, 4.786, 4.9, 4.967, 5.018, 5.071, 5.12])
a, b, c, d = np.polyfit(xs, ys, 3)

# Embedding parameter array
wls = np.linspace(1.3, 1.4, 2000) * 1e-6

# Search centers
centers = a * wls**3 + b * wls**2 + c * wls + d

# PML strength
alpha = 5

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    a = ARF2(name='fine_cladding', poly_core=True, refine=ref,
             curve=max(p+1, 8), shift_capillaries=False, wl=wls[i])

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', wavelength: ' + str(wls[i]) +
          '#'*8 + '\n', flush=True)

    center = centers[i]
    radius = .02
    npts = 4

    beta, _, Es, phis, _ = a.leakyvecmodes(ctr=center,
                                           rad=radius,
                                           alpha=alpha,
                                           nspan=nspan,
                                           npts=npts,
                                           p=p,
                                           niterations=9,
                                           nrestarts=0,
                                           stop_tol=1e-9,
                                           inverse='pardiso')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)

    a.save_mesh('modes/mesh_index_' + str(i))
    a.save_modes(Es, 'modes/E_modes_index_' + str(i))
    a.save_modes(phis, 'modes/phi_modes_index_' + str(i))
