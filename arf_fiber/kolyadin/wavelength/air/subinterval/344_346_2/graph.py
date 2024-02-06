#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:33:33 2022

@author: pv
"""

import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, LogLocator

plt.close('all')

main = os.path.expanduser('~/local/convergence/arf_fiber/kolyadin/wavelength/\
air/subinterval/344_346_2/')

wl64_p7_raw = np.load(main+'badwls/ref0_p7/e64.npy').imag
wl64_p8_raw = np.load(main+'badwls/ref0_p8/e64.npy').imag

CL_64_p7 = 20 * np.mean(wl64_p7_raw[np.where(wl64_p7_raw > 0)]) / np.log(10)
CL_64_p8 = 20 * np.mean(wl64_p8_raw[np.where(wl64_p8_raw > 0)]) / np.log(10)


err_64 = np.abs(CL_64_p8 - CL_64_p7) / CL_64_p7*100

wl108_p7_raw = np.load(main+'badwls/ref0_p7/e108.npy').imag
wl108_p8_raw = np.load(main+'badwls/ref0_p8/e108.npy').imag
wl108_p9_raw = np.load(main+'badwls/ref0_p9/e108.npy').imag
wl108_p10_raw = np.load(main+'badwls/ref0_p10/e108.npy').imag

CL_108_p7 = 20 * np.mean(wl108_p7_raw[
    np.where((wl108_p7_raw > 0) * (wl108_p7_raw < .2))]) / np.log(10)
CL_108_p8 = 20 * np.mean(wl108_p8_raw[
    np.where((wl108_p8_raw > 0) * (wl108_p8_raw < .2))]) / np.log(10)
CL_108_p9 = 20 * np.mean(wl108_p9_raw[
    np.where((wl108_p9_raw > 0) * (wl108_p9_raw < .2))]) / np.log(10)

err_108 = np.abs(CL_108_p9 - CL_108_p8) / CL_108_p8*100

wl347_p7_raw = np.load(main+'badwls/ref0_p7/e347.npy').imag
wl347_p8_raw = np.load(main+'badwls/ref0_p8/e347.npy').imag
wl347_p9_raw = np.load(main+'badwls/ref0_p9/e347.npy').imag
wl347_p10_raw = np.load(main+'badwls/ref0_p10/e347.npy').imag

CL_347_p7 = 20 * np.mean(wl347_p7_raw[
    np.where((wl347_p7_raw > 0) * (wl347_p7_raw < .2))]) / np.log(10)
CL_347_p8 = 20 * np.mean(wl347_p8_raw[
    np.where((wl347_p8_raw > 0) * (wl347_p8_raw < .2))]) / np.log(10)
CL_347_p9 = 20 * np.mean(wl347_p9_raw[
    np.where((wl347_p9_raw > 0) * (wl347_p9_raw < .2))]) / np.log(10)
CL_347_p10 = 20 * np.mean(wl347_p10_raw[
    np.where((wl347_p10_raw > 0) * (wl347_p10_raw < .2))]) / np.log(10)

err_347 = np.abs(CL_347_p10 - CL_347_p9) / CL_347_p9*100


# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False,
                               gridspec_kw={'height_ratios': [2.5, 1]},
                               figsize=(35, 16))

wls = np.linspace(3.44, 3.46, 400) * 1e-6


path = os.path.relpath(main + '/ref0_p5')

# First set of data
raw1 = np.load(path + '/all_e.npy').imag
base1 = np.zeros_like(wls)

for j in range(len(wls)):

    b = raw1[j, :]
    if j == 31:
        L = b[np.where((b > 1.2e-6) * (b < 1e0/8))]
        base1[j] = np.mean(L)

    elif j == 14:
        L = b[np.where((b > .0002) * (b < .1))]
        base1[j] = np.mean(L)

    elif j == 93:
        L = b[np.where((b > 1e-5) * (b < .1))]
        base1[j] = np.mean(L)

    elif j == 71:
        L = b[np.where((b > 1e-6) * (b < .01))]
        base1[j] = np.mean(L)

    elif j == 173:
        L = b[np.where((b > 0) * (b < .03))]
        base1[j] = np.mean(L)

    elif j == 196:
        L = b[np.where((b > 0) * (b < .04))]
        base1[j] = np.mean(L)

    elif j == 245:
        L = b[np.where((b > 0) * (b < .04))]
        base1[j] = np.mean(L)

    else:
        L = b[np.where((b > .5e-6) * (b < 1e0/8))]
        try:
            base1[j] = np.mean(L)
        except ValueError:
            base1[j] = np.nan


# Second set of data
path = os.path.relpath(main + '/ref0_p6')

raw2 = np.load(path + '/all_e.npy').imag
base2 = np.zeros_like(wls)

for j in range(len(wls)):

    b = raw2[j, :]

    if j == 31:
        L = b[np.where((b > 1.2e-6) * (b < 1e0/8))]
        base2[j] = np.mean(L)

    elif j == 14:
        L = b[np.where((b > .0002) * (b < .4))]
        base2[j] = np.mean(L)

    elif j == 108:
        L = b[np.where((b > .0003) * (b < 2))]
        base2[j] = np.mean(L)

    elif j == 93:
        L = b[np.where((b > 1e-5) * (b < .1))]
        base2[j] = np.mean(L)

    elif j == 71:
        L = b[np.where((b > 1e-6) * (b < .01))]
        base2[j] = np.mean(L)

    elif j == 173:
        L = b[np.where((b > 0) * (b < .03))]
        base2[j] = np.mean(L)

    elif j == 196:
        L = b[np.where((b > 0) * (b < .04))]
        base2[j] = np.mean(L)

    elif j == 245:
        L = b[np.where((b > 0) * (b < .04))]
        base2[j] = np.mean(L)

    else:
        L = b[np.where((b > 1e-7) * (b < 1/8))]
        try:
            base2[j] = np.mean(L)
        except ValueError:
            base2[j] = np.nan


CL1 = 20 * base1 / np.log(10)
CL2 = 20 * base2 / np.log(10)

err_orig = 100 * np.abs(CL1 - CL2) / CL1


CL1_fixed = np.zeros_like(CL1)
CL1_fixed[:] = CL1

CL2_fixed = np.zeros_like(CL2)
CL2_fixed[:] = CL2


CL1_fixed[64] = CL_64_p7
CL2_fixed[64] = CL_64_p8

CL1_fixed[108] = CL_108_p8
CL2_fixed[108] = CL_108_p9

CL1_fixed[347] = CL_347_p9
CL2_fixed[347] = CL_347_p10

err_improved = 100 * np.abs(CL1_fixed - CL2_fixed) / CL1_fixed

# # Plot the data


ax1.plot(wls, CL1_fixed, color='blue',
         label='p = 5', marker='o',
         linewidth=3, markersize=9)

ax1.plot(wls, CL2_fixed, color='orange',
         label='p = 6', marker='o',
         linewidth=0, markersize=8)

ax1.plot(wls[64], CL_64_p8, marker='o', linewidth=0,
         markersize=9, color='red',
         label='p > 6')

ax1.plot(wls[108], CL_108_p9, marker='o', linewidth=0,
         markersize=9, color='red')

ax1.plot(wls[347], CL_347_p10, marker='o', linewidth=0,
         markersize=9, color='red')

# Plot the data

ax2.plot(wls, err_improved, color='red',
         linewidth=2)

ax2.plot(wls, err_orig, color='green',
         linewidth=2, label='relative error')


# Set Figure and Axes parameters ################################

# Set titles
fig.suptitle("8 Tube ARF Subinterval with Benchmarking: Better Mesh.\n",
             fontsize=42)

# Set axis labels
ax2.set_xlabel("\nWavelength", fontsize=40)
ax1.set_ylabel("CL\n", fontsize=40)
ax2.set_ylabel("% Error\n", fontsize=40)

# Set up ticks and grids

plt.rc('xtick', labelsize=22,)
plt.rc('ytick', labelsize=22)

ax1.xaxis.set_major_locator(MultipleLocator(2e-9))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
# ax1.yaxis.set_major_locator(MultipleLocator(1))
# ax1.yaxis.set_minor_locator(AutoMinorLocator(0))
ax1.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax1.grid(which='minor', color='#CCCCCC', linestyle=':')

# # # Set log scale on y axes
ax1.set_yscale('log')
ax2.set_yscale('log')


ax2.xaxis.set_major_locator(MultipleLocator(2e-9))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))

y_major = LogLocator(base=10)
# y_minor = LogLocator(base=10, subs=(1., 2.0, 3., 4., 5., 6., 7., 8., 9.))

ax2.yaxis.set_major_locator(y_major)
# ax2.yaxis.set_minor_locator(y_minor)

ax2.grid(which='major', color='#CCCCCC', linewidth=1.2, linestyle='--')
ax2.grid(which='minor', color='#CCCCCC', linestyle=':')

# Set log scale on y axes

# Turn on subplot tool when graphing to allow finer control of spacing
# plt.subplot_tool(fig)

# After fine tuning, these are the values we want (use export from tool)
plt.subplots_adjust(top=0.915,
                    bottom=0.098,
                    left=0.072,
                    right=0.973,
                    hspace=0.146,
                    wspace=0.2)

# ax2.set_ylim(1e-4, 1e2)
ax1.set_xlim(3.4395e-6, 3.4605e-6)
ax2.set_xlim(3.4395e-6, 3.4605e-6)

ax2.plot([3.4395e-6, 3.4605e-6], [1, 1], color='gray',
         linewidth=2.2, linestyle='--', label='$1\\%$')

ax1.legend(fontsize=25)
ax2.legend(fontsize=25, loc='upper right')
ax2.set_ylim(.2e-4, 1e2)

# Show figure (needed for running from command line)
plt.show()


# %%

# Save cleaned data to numpy arrays for comparison plot

# np.save(os.path.relpath(main + 'wavelength/data/air_CL'), CL1)
# np.save(os.path.relpath(main + 'wavelength/data/air_wls'), wls)


# %%

# Save to .dat file for pgfplots

paper_path = os.path.relpath(os.path.expanduser('~/papers/outer_materials/\
manuscript/figures/data/arf/8tube'))

both = np.column_stack((wls*1e6, CL1_fixed))
np.savetxt(paper_path + '/ref0_p5_subint2.dat', both, fmt='%.8f')

both = np.column_stack((wls*1e6, CL2_fixed))
np.savetxt(paper_path + '/ref0_p6_subint2.dat', both, fmt='%.8f')

error_orig = 100*np.abs(CL1 - CL2)/CL1
error_fixed = 100*np.abs(CL1_fixed - CL2_fixed)/CL1_fixed

both = np.column_stack((wls*1e6, error_orig))
np.savetxt(paper_path + '/ref0_p6p5_rel_error2.dat', both, fmt='%.8f')

both = np.column_stack((wls[[64, 108, 347]]*1e6, CL2_fixed[[64, 108, 347]]))
np.savetxt(paper_path + '/single_points.dat', both, fmt='%.8f')

both = np.column_stack((wls[63:66]*1e6, error_fixed[63:66]))
np.savetxt(paper_path + '/bad_interval1.dat', both, fmt='%.8f')

both = np.column_stack((wls[107:110]*1e6, error_fixed[107:110]))
np.savetxt(paper_path + '/bad_interval2.dat', both, fmt='%.8f')

both = np.column_stack((wls[346:349]*1e6, error_fixed[346:349]))
np.savetxt(paper_path + '/bad_interval3.dat', both, fmt='%.8f')
