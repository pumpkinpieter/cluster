#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os
import sys
from fiberamp.fiber.microstruct.pbg import ARF2

main = os.path.expanduser('~/local/convergence/csg_arf/embedding_sensitivity\
/subintervals')

# Center, radius and span
center = 5.066       # center of circle to search for Z-resonance values
radius = .007         # search radius
nspan = 4
npts = 4

# Main array of embedding values
E_main = np.linspace(0.002, .9999, 240)

# PML strength
alpha = 5

# Set result arrays
betas = np.zeros(nspan, dtype=complex)

if __name__ == '__main__':

    # Command Line arguments:
    if len(sys.argv) != 9:
        raise ValueError('Too few or too many command line arguments given.\
 Arguments: refinements, polynomial order, index (for sub interval), L, R,\
 (specify left and right indices to form subarray), N (number of points in sub\
-array), low, high (floats that determine when we save modes).')

    # refinements, polynomial order, index of embedding (for E_sub)
    ref, p, i = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    # Left index, Right index (of E_main) and Number of points
    # This picks out subinterval of E_main to refine.
    L, R, N = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])

    # low, high : limits on e for which we want to save modes
    low, high = float(sys.argv[7]), float(sys.argv[8])

    # Make folders for this subinterval
    studyname = 'index_' + str(L) + '_' + str(R)
    study = main + '/' + studyname
    constants = study + '/outputs'
    modes = study + '/modes'

    if not os.path.isdir(os.path.relpath(study)):
        print('Making study directory tree: ' + studyname)
        os.makedirs(os.path.relpath(constants))
        os.makedirs(os.path.relpath(modes))
        os.makedirs(os.path.relpath(study + '/' + 'errors'))
        os.makedirs(os.path.relpath(study + '/' + 'logs'))

    # Form refined array of e values (with endpoints in E_main)
    E_sub = np.linspace(E_main[L], E_main[R], N)
    save_index = np.where((low < E_sub) * (E_sub < high))[0]

    a = ARF2(poly_core=True, refine=ref, curve=max(p+1, 3), e=E_sub[i])

    print('\n' + '#'*8 + ' refinement: ' + str(ref) +
          ', degree: ' + str(p) + ', e: ' + str(E_sub[i]) + '#'*8 + '\n',
          flush=True)

    beta, _, E_modes, _, _ = a.leakyvecmodes(ctr=center,
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
    np.save(os.path.relpath(constants + '/e_sub_' + str(i)), betas)
    np.save(os.path.relpath(constants + '/E_sub_'+str(L)+'_'+str(R)), E_sub)
    if i in save_index:
        a.save_mesh(os.path.relpath(modes + '/mesh_e_sub' + str(i)))
        a.save_modes(E_modes, os.path.relpath(modes + '/mode_e_sub' + str(i)))
