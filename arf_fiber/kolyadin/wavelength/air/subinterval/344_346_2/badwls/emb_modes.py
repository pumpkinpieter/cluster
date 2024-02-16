#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

# Set result arrays
nspan = 4
betas = np.zeros(nspan, dtype=complex)

# Embedding parameter array
wls = np.linspace(3.11, 3.6, 300) * 1e-6

# Search centers
inds = [85,   70,    60,    40,    20,    0,  100,  150,   175,   190,
        230,   250,  275,   299]
data = [5.148, 5.131, 5.118, 5.088, 5.05, 4.997, 5.16, 5.21, 5.236, 5.250,
        5.29, 5.317, 5.35, 5.400]
degree = 7
coeffs = np.polyfit(wls[inds], data, degree)
wls = np.linspace(3.44, 3.46, 400) * 1e-6
centers = sum([coeffs[-i-1] * wls**i for i in range(0, degree + 1)])

# PML strength
alpha = 5

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    if not os.path.isdir('ref'+str(ref)+'_p'+str(p)):
        print('Making input directory')
        os.makedirs('ref'+str(ref)+'_p'+str(p))

    if len(sys.argv) > 4:
        L, R = float(sys.argv[4]), float(sys.argv[5])
        save_index = np.where((L < wls) * (wls < R))[0]
        if not os.path.isdir('modes'):
            print('Making directory: modes')
            os.makedirs('modes')

    a = ARF2(name='kolyadin',
             refine=ref,
             curve=max(p+1, 8),
             glass_maxh=.025,
             fill_air_maxh=.08,
             inner_air_maxh=.1,
             poly_core=True,
             wl=wls[i]
             )

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
                                        niterations=12,
                                        nrestarts=0,
                                        stop_tol=1e-10,
                                        inverse='pardiso')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)

    np.save('ref'+str(ref)+'_p'+str(p)+'/e'+str(i), betas)

    if len(sys.argv) > 4 and i in save_index:
        a.save_mesh('modes/mesh_e' + str(i))
        a.save_modes(Es, 'modes/mode_e' + str(i))
