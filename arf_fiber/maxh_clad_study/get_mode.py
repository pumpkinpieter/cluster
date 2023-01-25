#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

if not os.path.isdir('modes'):
    print('Making directory: ' + 'modes')
    os.makedirs('modes')

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

    if not os.path.isdir('modes'):
        print('Making directory: modes')
        os.makedirs('modes')

    a = ARF2(name='fine_cladding', refine=ref, curve=max(p+1, 8),
             poly_core=True, glass_maxh=maxh)

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + '  ' + '#'*8 + '\n', flush=True)

    _, _, Es, phis, _ = a.leakyvecmodes(p=p, ctr=center, rad=radius,
                                        alpha=alpha,
                                        nspan=nspan, npts=npts,
                                        niterations=15, nrestarts=0,
                                        stop_tol=1e-10,
                                        inverse='pardiso')

    print('\nMethod done, saving modes.\n', flush=True)

    a.save_mesh('modes/mesh_maxh_' + str(maxh) + 'p' + str(p) + '.pkl')
    a.save_modes(Es, 'modes/Es_maxh' + str(maxh) + 'p' + str(p))
    a.save_modes(phis, 'modes/phis_maxh' + str(maxh) + 'p' + str(p))
