#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.bragg import Bragg

# Set result arrays
nspan = 4
betas = np.zeros(nspan, dtype=complex)
dofs = np.zeros(1, dtype=float)

# Get exact search centers
centers = np.load('exact_scaled_betas.npy')

# Embedding parameter array
wls = np.linspace(1.4, 2, 301) * 1e-6
wl_idx = 0

wl = wls[wl_idx]

# PML strength
alphas = np.linspace(.1, 15, 101)

if __name__ == '__main__':

    ref, p = int(sys.argv[1]), int(sys.argv[2])
    alpha_idx = int(sys.argv[3])
    t_outer = float(sys.argv[4])

    n_air = 1.00027717
    n_glass = 1.4388164768221814
    ts = [15*2.7183333333333333e-6, 15*2/3*1e-6, 15*1e-6, t_outer]
    ns = [lambda x: n_air, lambda x: n_glass, lambda x: n_air, lambda x: n_air]
    maxhs = [.1, .02, .04, .06]
    scale = 15e-6

    a = Bragg(ts=ts, scale=scale, maxhs=maxhs, ns=ns,
              wl=wl, ref=ref)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', wavelength: ' + str(wl) +
          '#'*8 + '\n', flush=True)

    centers = a.sqrZfrom(centers/a.L).conjugate()
    center = centers[wl_idx]
    radius = 0.05
    npts = 4
    alpha = alphas[alpha_idx]

    beta, _, _, _, _ = a.leakyvecmodes(ctr=center,
                                       rad=radius,
                                       alpha=alpha,
                                       nspan=nspan,
                                       npts=npts,
                                       p=p,
                                       niterations=10,
                                       nrestarts=0,
                                       stop_tol=1e-11,
                                       inverse='pardiso')

    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)

    outdir = 'ref' + str(ref) + 'p' + str(p) + 'T' + str(t_outer)

    if not os.path.isdir(outdir):
        print('Making directory: ' + outdir)
        os.makedirs(outdir)

    np.save(outdir + '/alpha' + str(alpha_idx), betas)
