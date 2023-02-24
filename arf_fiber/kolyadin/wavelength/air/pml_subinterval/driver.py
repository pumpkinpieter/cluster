#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
import netgen.libngpy as libngpy
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


if __name__ == '__main__':

    ref, p, alpha, i = int(sys.argv[1]), int(
        sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])

    dirname = 'ref%i_p%i_alpha%.2f' % (ref, p, alpha)

    if not os.path.isdir(dirname):
        print('Making output directory: %s' % dirname)
        os.makedirs(dirname)

    a = ARF2(name='kolyadin', poly_core=True, refine=ref,
             curve=max(p+1, 8), wl=wls[i])

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', wavelength: ' + str(wls[i]) +
          '#'*8 + '\n', flush=True)

    center = centers[i]
    radius = 0.05
    npts = 4

    try:
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
    except libngpy._meshing.NgException:
        beta, _, Es, _, _ = a.leakyvecmodes(ctr=center,
                                            rad=radius,
                                            alpha=alpha,
                                            nspan=nspan,
                                            npts=npts,
                                            p=p,
                                            niterations=10,
                                            nrestarts=0,
                                            stop_tol=1e-9,
                                            inverse='umfpack')
    betas[: len(beta)] = beta[:]

    print('method done, saving.\n', flush=True)

    np.save(dirname + '/%i' % i, betas)
