#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

# Center, radius and span
center = 5.066       # center of circle to search for Z-resonance values
radius = .1      # search radius
nspan = 4
npts = 4

# PML strength
alpha = 5

# Set result arrays
betas = np.zeros(nspan, dtype=complex)
dofs = np.zeros(1, dtype=float)

if __name__ == '__main__':

    ref, p, maxh = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])

    outputs = 'outputs/maxh_' + str(maxh)

    if not os.path.isdir(outputs):
        print('Making directory: ' + outputs)
        os.makedirs(outputs)

    a = ARF2(name='fine_cladding', refine=ref, curve=max(p+1, 8),
             poly_core=True, glass_maxh=maxh)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + '  ' + '#'*8 + '\n', flush=True)

    beta, _, _, _, Robj = a.leakyvecmodes(p=p, ctr=center, rad=radius,
                                          alpha=alpha,
                                          nspan=nspan, npts=npts,
                                          niterations=30, nrestarts=0,
                                          stop_tol=1e-11, inverse='pardiso')

    betas[: len(beta)] = beta[:]
    dofs[:] = Robj.XY.ndof

    print('method done, saving.\n', flush=True)
    np.save(outputs + '/ref' + str(ref) + 'p' + str(p) + 'betas', betas)
    np.save(outputs + '/ref' + str(ref) + 'p' + str(p) + 'dofs', dofs)
