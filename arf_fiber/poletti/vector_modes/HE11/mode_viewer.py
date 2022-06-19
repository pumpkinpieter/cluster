#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 18:27:40 2022

@author: pv
"""

import sys
# import netgen.gui
from fiberamp.fiber.microstruct.pbg import ARF2

if __name__ == '__main__':

    # ref, p = int(sys.argv[1]), int(sys.argv[2])
    ref, p = 0, 1
    a = ARF2(refine=ref, curve=max(p+1, 3), poly_core=True)

    mesh_path = 'modes/mesh_ref' + str(ref) + 'p' + str(p) + '.pkl'
    Es_path = 'modes/Es_ref' + str(ref) + 'p' + str(p)
    phis_path = 'modes/phis_ref' + str(ref) + 'p' + str(p)

    mesh = a.load_mesh(mesh_path)
    Es = a.load_E_modes(mesh_path, Es_path, p=1)
    phis = a.load_phi_modes(mesh_path, phis_path, p=1)

Es.draw(name='Es')
phis.draw(name='phis')
