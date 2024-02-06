#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.bragg import Bragg

# Set result arrays
nspan = 4
betas = np.zeros(nspan, dtype=complex)

# Get exact search centers
centers = np.load('exact_scaled_betas.npy')

# Embedding parameter array
wls = np.linspace(1.4, 2, 301) * 1e-6

# PML strength
alpha = 5

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    
    outdir = 'ref'+str(ref)+'_p'+str(p)

    if not os.path.isdir(outdir):
        print('Making directory:'+outdir)
        os.makedirs(outdir)

    if len(sys.argv) > 4:
        L, R = float(sys.argv[4]), float(sys.argv[5])
        save_index = np.where((L < wls) * (wls < R))[0]
        if not os.path.isdir('modes'):
            print('Making directory: modes')
            os.makedirs('modes')


    n_air = 1.00027717
    n_glass = 1.4388164768221814
    ts = [15*2.7183333333333333e-6, 15*2/3*1e-6,
          15*2.7183333333333333e-6, 15*1e-6, 15*2e-6]
    ns = [lambda x: n_air, lambda x: n_glass, lambda x: n_air,
          lambda x: n_glass, lambda x: n_glass]
    mats = ['core', 'glass', 'air', 'buffer', 'Outer']
    maxhs = [.15, .012, .06, .007, .05]
    scale = 15e-6

    a = Bragg(ts=ts, scale=scale, maxhs=maxhs, ns=ns, mats=mats,
              wl=wls[i], ref=ref)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', wavelength: ' + str(wls[i]) +
          '#'*8 + '\n', flush=True)

    centers = a.sqrZfrom(centers/a.L).conjugate()
    center = centers[i]
    radius = 0.05
    npts = 4

    if len(sys.argv) > 4:
        beta, _, Es, phis, _ = a.leakyvecmodes(ctr=center,
                                               rad=radius,
                                               alpha=alpha,
                                               nspan=nspan,
                                               npts=npts,
                                               p=p,
                                               niterations=10,
                                               nrestarts=0,
                                               stop_tol=1e-10,
                                               inverse='pardiso')
    else:
        beta, _, _, _, _ = a.leakyvecmodes(ctr=center,
                                               rad=radius,
                                               alpha=alpha,
                                               nspan=nspan,
                                               npts=npts,
                                               p=p,
                                               niterations=10,
                                               nrestarts=0,
                                               stop_tol=1e-10,
                                               inverse='pardiso')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)

    np.save(outdir+'/e' + str(i), betas)

    if len(sys.argv) > 4 and i in save_index:
        a.save_mesh('modes/mesh_wl' + str(i))
        a.save_modes(Es, 'modes/E_modes_wl' + str(i))
        a.save_modes(phis, 'modes/phi_modes_wl' + str(i))
