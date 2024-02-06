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
centers = np.load('exact_betas/k_002_scaled_betas.npy')

# Embedding parameter array
wls = np.linspace(2.97, 3.42, 401) * 1e-6

# Only doing every 3
evens = np.arange(0, 401, 3)
wls = wls[evens]
centers = centers[evens]

# Fiber Parameters
n_air = 1.00027717
n_glass = 1.4388164768221814
n_poly = n_glass + k*1j
ts = [4.0775e-05, 1e-5, 4.0775e-05, 1e-5, 4.0775e-05, 3e-5, 3e-5]
ns = [n_air, n_glass, n_air, n_glass, n_poly, n_air, n_air]
mats = ['air','glass', 'air', 'glass', 'polymer', 'air', 'Outer']
maxhs = [.2, .02, .2, .02, .04, .08, .1]
scale = 15e-6

# PML strength
alpha = 5

if __name__ == '__main__':

    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    k = float(sys.argv[4])
    outdir = 'k_'+str(k)
    if not os.path.isdir(outdir):
        print('Making output directory.')
        os.makedirs(outdir)

    a = Bragg(ts=ts, scale=scale, maxhs=maxhs, ns=ns, wl=wls[i],
              mats=mats, ref=ref, curve=max(p+1, 8))

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', wavelength: ' + str(wls[i]) +
          '#'*8 + '\n', flush=True)

    centers = a.sqrZfrom(centers/a.L).conjugate()
    center = centers[i]
    radius = 0.02
    npts = 4

    beta, _, Es, _, _ = a.leakyvecmodes(ctr=center,
                                        rad=radius,
                                        alpha=alpha,
                                        nspan=nspan,
                                        npts=npts,
                                        p=p,
                                        niterations=17,
                                        nrestarts=0,
                                        stop_tol=1e-6,
                                        inverse='pardiso')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)

    np.save(outdir+'/wl' + str(i), betas)
