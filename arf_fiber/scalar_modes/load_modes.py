#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:05:08 2022

@author: pv
"""
import ngsolve as ng
import os
from fiberamp.fiber.microstruct.arf import loadarfmode


main = os.path.expanduser('~/local/convergence/arf_fiber')
studyname = 'scalar_modes'
path = main + '/' + studyname + '/modes'

ref, p = 0, 2
arffprefix = path + '/arf__p' + str(p) + '_ref' + str(ref)
modenpzf = arffprefix + '_mde.npz'
a, Y, betas, Zs, p, _, _, _ = loadarfmode(modenpzf, arffprefix)

print("Betas: ", betas, " Zs: ", Zs, " p: ", p)

a.curve(max(p+1, 3))
ng.Draw(a.mesh)
Y.draw()
