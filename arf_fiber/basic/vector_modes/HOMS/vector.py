#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

locations = [12.74372428,
             12.75428731, 12.75442679,
             12.77602774,
             12.80818931, 12.81076203]

outputs = 'outputs'

if not os.path.isdir(outputs):
    print('Making directory: ' + outputs)
    os.makedirs(outputs)

# Center, radius and span
center = 12.77602774    # center of circle to search for Z-resonance values
radius = .005      # search radius
nspan = 4
npts = 4

# PML strength
alpha = 5

# Set result arrays
Zs = np.zeros(nspan, dtype=complex)
betas = np.zeros(nspan, dtype=complex)
dofs = np.zeros(1, dtype=float)

if __name__ == '__main__':

    ref, p = int(sys.argv[1]), int(sys.argv[2])

    a = ARF2(refine=ref, curve=max(p+1, 3), poly_core=True)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + '  ' + '#'*8 + '\n', flush=True)

    beta, Z, _, _, Robj = a.leakyvecmodes(p=p, ctr=center, rad=radius,
                                          alpha=alpha,
                                          #  rhoinv=.95,
                                          #  quadrule='ellipse_trapez_shift',
                                          nspan=nspan, npts=npts,
                                          niterations=20, nrestarts=0,
                                          stop_tol=1e-10, inverse='umfpack')

    Zs[: len(Z)] = Z[:]
    betas[: len(beta)] = beta[:]
    dofs[:] = Robj.XY.ndof

    print('method done, saving.\n', flush=True)
    np.save(outputs + '/ref' + str(ref) + 'p' + str(p) + 'Zs', Zs)
    np.save(outputs + '/ref' + str(ref) + 'p' + str(p) + 'betas', betas)
    np.save(outputs + '/ref' + str(ref) + 'p' + str(p) + 'dofs', dofs)
