#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2


if not os.path.isdir('outputs'):
    print('Making directory: ' + 'outputs')
    os.makedirs('outputs')
if not os.path.isdir('modes'):
    print('Making directory: ' + 'modes')
    os.makedirs('modes')

# Center, radius and span
center = 5.066       # center of circle to search for Z-resonance values
radius = .05      # search radius
nspan = 4
npts = 4

# PML strength
alpha = 5

# Set result arrays
betas = np.zeros(nspan, dtype=complex)
dofs = np.zeros(1, dtype=float)

if __name__ == '__main__':

    ref, p = int(sys.argv[1]), int(sys.argv[2])

    a = ARF2(refine=ref, curve=max(p+1, 3), poly_core=True)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + '  ' + '#'*8 + '\n', flush=True)

    beta, _, Es, phis, Robj = a.leakyvecmodes(p=p, ctr=center, rad=radius,
                                              alpha=alpha,
                                              nspan=nspan, npts=npts,
                                              niterations=30, nrestarts=0,
                                              stop_tol=1e-11,
                                              inverse='pardiso')

    betas[: len(beta)] = beta[:]
    dofs[:] = Robj.XY.ndof

    print('\nMethod done, saving values and modes.\n', flush=True)

    np.save('outputs/ref' + str(ref) + 'p' + str(p) + 'betas', betas)
    np.save('outputs/ref' + str(ref) + 'p' + str(p) + 'dofs', dofs)

    a.save_mesh('modes/mesh_ref' + str(ref) + 'p' + str(p) + '.pkl')
    a.save_modes(Es, 'modes/Es_ref' + str(ref) + 'p' + str(p))
    a.save_modes(phis, 'modes/phis_ref' + str(ref) + 'p' + str(p))
