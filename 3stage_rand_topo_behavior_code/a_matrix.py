import numpy as np


# import torch

def capacitor(c, s):
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1
    a[1] = 0
    a[2] = c * s
    a[3] = 1
    return a


def resistor(r, s):
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1
    a[1] = 0
    a[2] = 1 / r
    a[3] = 1
    return a


def r_c_parallel(r, c, s):
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1
    a[1] = 0
    a[2] = 1.0 * (1.0 * c * r * s + 1.0) / r
    a[3] = 1
    return a


def r_c_series(r, c, s):
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1
    a[1] = 0
    a[2] = 1.0 * c * s / (c * r * s + 1)
    a[3] = 1
    return a


def gm_diff_pos(small_signal_param, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2, gm_b1 = gm
    go_n1, go_n2, go_p1, go_p2, go_b1 = go
    gb_n1, gb_n2, gb_p1, gb_p2, gb_b1 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2, cgs_b1 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = -1.0 * gm_n1 * (-1.0 * cgd_n1 * s ** 2 * (cgd_b1 + cgs_n1 + cgs_n2) / (
                gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2)) + 1.0 + 1.0 * s * (
                                       cgd_b1 * gm_n1 - cgd_n1 * gb_n1 - cgd_n1 * gb_n2 - cgd_n1 * gm_n1 - cgd_n1 * gm_n2 - cgd_n1 * go_b1 - cgd_n1 * go_n1 - cgd_n1 * go_n2 - cgs_n1 * gb_n1 - cgs_n1 * go_n1 + cgs_n2 * gm_n1) / (
                                       gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2))) * (gb_n2 + gm_n2 + go_b1 + go_n2) / ((
                                                                                                                                  s ** 2 * (
                                                                                                                                      cgd_n1 + cgd_p1) * (
                                                                                                                                              cgd_b1 + cgs_n1 + cgs_n2) / (
                                                                                                                                              gb_n1 * go_p1 + gb_n2 * go_n1 + gb_n2 * go_p1 + gm_n1 * go_p1 + gm_n2 * go_n1 + gm_n2 * go_p1 + go_b1 * go_n1 + go_b1 * go_p1 + go_n1 * go_n2 + go_n1 * go_p1 + go_n2 * go_p1) + s * (
                                                                                                                                              cgd_b1 * go_n1 + cgd_b1 * go_p1 + cgd_n1 * gb_n1 + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 + cgd_n1 * go_b1 + cgd_n1 * go_n1 + cgd_n1 * go_n2 + cgd_p1 * gb_n1 + cgd_p1 * gb_n2 + cgd_p1 * gm_n1 + cgd_p1 * gm_n2 + cgd_p1 * go_b1 + cgd_p1 * go_n1 + cgd_p1 * go_n2 + cgs_n1 * go_n1 + cgs_n1 * go_p1 + cgs_n2 * go_n1 + cgs_n2 * go_p1) / (
                                                                                                                                              gb_n1 * go_p1 + gb_n2 * go_n1 + gb_n2 * go_p1 + gm_n1 * go_p1 + gm_n2 * go_n1 + gm_n2 * go_p1 + go_b1 * go_n1 + go_b1 * go_p1 + go_n1 * go_n2 + go_n1 * go_p1 + go_n2 * go_p1) + 1) * (
                                                                                                                                  gb_n1 * go_p1 + gb_n2 * go_n1 + gb_n2 * go_p1 + gm_n1 * go_p1 + gm_n2 * go_n1 + gm_n2 * go_p1 + go_b1 * go_n1 + go_b1 * go_p1 + go_n1 * go_n2 + go_n1 * go_p1 + go_n2 * go_p1))
    a[1] = -1.0 * gm_n1 * (-1.0 * cgd_n1 * s ** 2 * (cgd_b1 + cgs_n1 + cgs_n2) / (
                gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2)) + 1.0 + 1.0 * s * (
                                       cgd_b1 * gm_n1 - cgd_n1 * gb_n1 - cgd_n1 * gb_n2 - cgd_n1 * gm_n1 - cgd_n1 * gm_n2 - cgd_n1 * go_b1 - cgd_n1 * go_n1 - cgd_n1 * go_n2 - cgs_n1 * gb_n1 - cgs_n1 * go_n1 + cgs_n2 * gm_n1) / (
                                       gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2))) * (gb_n2 + gm_n2 + go_b1 + go_n2) / ((
                                                                                                                                  s ** 3 * (
                                                                                                                                      cgd_b1 * cgd_n1 * cgd_p1 + cgd_b1 * cgd_n1 * cgs_n1 + cgd_b1 * cgd_p1 * cgs_n1 + cgd_n1 * cgd_p1 * cgs_n1 + cgd_n1 * cgd_p1 * cgs_n2 + cgd_n1 * cgs_n1 * cgs_n2 + cgd_p1 * cgs_n1 * cgs_n2) / (
                                                                                                                                              cgd_n1 * gb_n1 * go_p1 + cgd_n1 * gb_n2 * gm_n1 + cgd_n1 * gb_n2 * go_n1 + cgd_n1 * gb_n2 * go_p1 + cgd_n1 * gm_n1 * gm_n2 + cgd_n1 * gm_n1 * go_b1 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p1 + cgd_n1 * gm_n2 * go_n1 + cgd_n1 * gm_n2 * go_p1 + cgd_n1 * go_b1 * go_n1 + cgd_n1 * go_b1 * go_p1 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p1 + cgd_n1 * go_n2 * go_p1 + cgs_n1 * gb_n1 * go_p1 + cgs_n1 * gb_n2 * go_n1 + cgs_n1 * gb_n2 * go_p1 + cgs_n1 * gm_n2 * go_n1 + cgs_n1 * gm_n2 * go_p1 + cgs_n1 * go_b1 * go_n1 + cgs_n1 * go_b1 * go_p1 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p1 + cgs_n1 * go_n2 * go_p1) + s ** 2 * (
                                                                                                                                              cgd_b1 * cgd_n1 * gm_n1 + cgd_b1 * cgd_n1 * go_n1 + cgd_b1 * cgd_n1 * go_p1 + cgd_b1 * cgs_n1 * go_n1 + cgd_b1 * cgs_n1 * go_p1 + cgd_n1 * cgd_p1 * gb_n1 + cgd_n1 * cgd_p1 * gb_n2 + cgd_n1 * cgd_p1 * gm_n1 + cgd_n1 * cgd_p1 * gm_n2 + cgd_n1 * cgd_p1 * go_b1 + cgd_n1 * cgd_p1 * go_n1 + cgd_n1 * cgd_p1 * go_n2 + cgd_n1 * cgs_n1 * gb_n2 + cgd_n1 * cgs_n1 * gm_n2 + cgd_n1 * cgs_n1 * go_b1 + cgd_n1 * cgs_n1 * go_n2 + cgd_n1 * cgs_n1 * go_p1 + cgd_n1 * cgs_n2 * gm_n1 + cgd_n1 * cgs_n2 * go_n1 + cgd_n1 * cgs_n2 * go_p1 + cgd_p1 * cgs_n1 * gb_n1 + cgd_p1 * cgs_n1 * gb_n2 + cgd_p1 * cgs_n1 * gm_n2 + cgd_p1 * cgs_n1 * go_b1 + cgd_p1 * cgs_n1 * go_n1 + cgd_p1 * cgs_n1 * go_n2 + cgs_n1 * cgs_n2 * go_n1 + cgs_n1 * cgs_n2 * go_p1) / (
                                                                                                                                              cgd_n1 * gb_n1 * go_p1 + cgd_n1 * gb_n2 * gm_n1 + cgd_n1 * gb_n2 * go_n1 + cgd_n1 * gb_n2 * go_p1 + cgd_n1 * gm_n1 * gm_n2 + cgd_n1 * gm_n1 * go_b1 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p1 + cgd_n1 * gm_n2 * go_n1 + cgd_n1 * gm_n2 * go_p1 + cgd_n1 * go_b1 * go_n1 + cgd_n1 * go_b1 * go_p1 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p1 + cgd_n1 * go_n2 * go_p1 + cgs_n1 * gb_n1 * go_p1 + cgs_n1 * gb_n2 * go_n1 + cgs_n1 * gb_n2 * go_p1 + cgs_n1 * gm_n2 * go_n1 + cgs_n1 * gm_n2 * go_p1 + cgs_n1 * go_b1 * go_n1 + cgs_n1 * go_b1 * go_p1 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p1 + cgs_n1 * go_n2 * go_p1) + s) * (
                                                                                                                                  cgd_n1 * gb_n1 * go_p1 + cgd_n1 * gb_n2 * gm_n1 + cgd_n1 * gb_n2 * go_n1 + cgd_n1 * gb_n2 * go_p1 + cgd_n1 * gm_n1 * gm_n2 + cgd_n1 * gm_n1 * go_b1 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p1 + cgd_n1 * gm_n2 * go_n1 + cgd_n1 * gm_n2 * go_p1 + cgd_n1 * go_b1 * go_n1 + cgd_n1 * go_b1 * go_p1 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p1 + cgd_n1 * go_n2 * go_p1 + cgs_n1 * gb_n1 * go_p1 + cgs_n1 * gb_n2 * go_n1 + cgs_n1 * gb_n2 * go_p1 + cgs_n1 * gm_n2 * go_n1 + cgs_n1 * gm_n2 * go_p1 + cgs_n1 * go_b1 * go_n1 + cgs_n1 * go_b1 * go_p1 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p1 + cgs_n1 * go_n2 * go_p1))
    a[2] = -1.0 * gm_n1 * (-1.0 * cgd_n1 * s ** 2 * (cgd_b1 + cgs_n1 + cgs_n2) / (
                gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2)) + 1.0 + 1.0 * s * (
                                       cgd_b1 * gm_n1 - cgd_n1 * gb_n1 - cgd_n1 * gb_n2 - cgd_n1 * gm_n1 - cgd_n1 * gm_n2 - cgd_n1 * go_b1 - cgd_n1 * go_n1 - cgd_n1 * go_n2 - cgs_n1 * gb_n1 - cgs_n1 * go_n1 + cgs_n2 * gm_n1) / (
                                       gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2))) * (gb_n2 + gm_n2 + go_b1 + go_n2) / ((
                                                                                                                                  1.0 * s * (
                                                                                                                                      cgd_b1 + cgs_n1 + cgs_n2) / (
                                                                                                                                              gb_n1 + gb_n2 + gm_n1 + gm_n2 + go_b1 + go_n1 + go_n2) + 1.0) * (
                                                                                                                                  gb_n1 + gb_n2 + gm_n1 + gm_n2 + go_b1 + go_n1 + go_n2))
    a[3] = -1.0 * gm_n1 * (-1.0 * cgd_n1 * s ** 2 * (cgd_b1 + cgs_n1 + cgs_n2) / (
                gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2)) + 1.0 + 1.0 * s * (
                                       cgd_b1 * gm_n1 - cgd_n1 * gb_n1 - cgd_n1 * gb_n2 - cgd_n1 * gm_n1 - cgd_n1 * gm_n2 - cgd_n1 * go_b1 - cgd_n1 * go_n1 - cgd_n1 * go_n2 - cgs_n1 * gb_n1 - cgs_n1 * go_n1 + cgs_n2 * gm_n1) / (
                                       gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2))) * (gb_n2 + gm_n2 + go_b1 + go_n2) / ((
                                                                                                                                  s ** 2 * (
                                                                                                                                      cgd_b1 * cgd_n1 + cgd_b1 * cgs_n1 + cgd_n1 * cgs_n1 + cgd_n1 * cgs_n2 + cgs_n1 * cgs_n2) / (
                                                                                                                                              cgd_n1 * gb_n1 + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 + cgd_n1 * go_b1 + cgd_n1 * go_n1 + cgd_n1 * go_n2 + cgs_n1 * gb_n1 + cgs_n1 * gb_n2 + cgs_n1 * gm_n2 + cgs_n1 * go_b1 + cgs_n1 * go_n1 + cgs_n1 * go_n2) + s) * (
                                                                                                                                  cgd_n1 * gb_n1 + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 + cgd_n1 * go_b1 + cgd_n1 * go_n1 + cgd_n1 * go_n2 + cgs_n1 * gb_n1 + cgs_n1 * gb_n2 + cgs_n1 * gm_n2 + cgs_n1 * go_b1 + cgs_n1 * go_n1 + cgs_n1 * go_n2))
    return a


def gm_diff_neg(small_signal_param, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2, gm_b1 = gm
    go_n1, go_n2, go_p1, go_p2, go_b1 = go
    gb_n1, gb_n2, gb_p1, gb_p2, gb_b1 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2, cgs_b1 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * gm_n1 * (1.0 * cgs_n1 * s / gm_n1 + 1.0) * (gb_n2 + gm_n2 + go_n2) / ((s ** 2 * (cgd_n2 + cgd_p2) * (
                cgd_b1 + cgs_n1 + cgs_n2) / (
                                                                                                    gb_n1 * go_n2 + gb_n1 * go_p2 + gb_n2 * go_p2 + gm_n1 * go_n2 + gm_n1 * go_p2 + gm_n2 * go_p2 + go_b1 * go_n2 + go_b1 * go_p2 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p2) + s * (
                                                                                                    cgd_b1 * go_n2 + cgd_b1 * go_p2 + cgd_n2 * gb_n1 + cgd_n2 * gb_n2 + cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * go_b1 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_p2 * gb_n1 + cgd_p2 * gb_n2 + cgd_p2 * gm_n1 + cgd_p2 * gm_n2 + cgd_p2 * go_b1 + cgd_p2 * go_n1 + cgd_p2 * go_n2 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2) / (
                                                                                                    gb_n1 * go_n2 + gb_n1 * go_p2 + gb_n2 * go_p2 + gm_n1 * go_n2 + gm_n1 * go_p2 + gm_n2 * go_p2 + go_b1 * go_n2 + go_b1 * go_p2 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p2) + 1) * (
                                                                                                   gb_n1 * go_n2 + gb_n1 * go_p2 + gb_n2 * go_p2 + gm_n1 * go_n2 + gm_n1 * go_p2 + gm_n2 * go_p2 + go_b1 * go_n2 + go_b1 * go_p2 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p2))
    a[1] = 1.0 * gm_n1 * (1.0 * cgs_n1 * s / gm_n1 + 1.0) * (gb_n2 + gm_n2 + go_n2) / ((s ** 3 * (cgd_n2 + cgd_p2) * (
                cgd_b1 * cgd_n1 + cgd_b1 * cgs_n1 + cgd_n1 * cgs_n1 + cgd_n1 * cgs_n2 + cgs_n1 * cgs_n2) / (
                                                                                                    cgd_n1 * gb_n1 * go_n2 + cgd_n1 * gb_n1 * go_p2 + cgd_n1 * gb_n2 * go_p2 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p2 + cgd_n1 * gm_n2 * go_p2 + cgd_n1 * go_b1 * go_n2 + cgd_n1 * go_b1 * go_p2 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p2 + cgd_n1 * go_n2 * go_p2 + cgs_n1 * gb_n1 * go_n2 + cgs_n1 * gb_n1 * go_p2 + cgs_n1 * gb_n2 * go_p2 + cgs_n1 * gm_n2 * go_p2 + cgs_n1 * go_b1 * go_n2 + cgs_n1 * go_b1 * go_p2 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p2 + cgs_n1 * go_n2 * go_p2) + s ** 2 * (
                                                                                                    cgd_b1 * cgd_n1 * go_n2 + cgd_b1 * cgd_n1 * go_p2 + cgd_b1 * cgs_n1 * go_n2 + cgd_b1 * cgs_n1 * go_p2 + cgd_n1 * cgd_n2 * gb_n1 + cgd_n1 * cgd_n2 * gb_n2 + cgd_n1 * cgd_n2 * gm_n1 + cgd_n1 * cgd_n2 * gm_n2 + cgd_n1 * cgd_n2 * go_b1 + cgd_n1 * cgd_n2 * go_n1 + cgd_n1 * cgd_n2 * go_n2 + cgd_n1 * cgd_p2 * gb_n1 + cgd_n1 * cgd_p2 * gb_n2 + cgd_n1 * cgd_p2 * gm_n1 + cgd_n1 * cgd_p2 * gm_n2 + cgd_n1 * cgd_p2 * go_b1 + cgd_n1 * cgd_p2 * go_n1 + cgd_n1 * cgd_p2 * go_n2 + cgd_n1 * cgs_n1 * go_n2 + cgd_n1 * cgs_n1 * go_p2 + cgd_n1 * cgs_n2 * go_n2 + cgd_n1 * cgs_n2 * go_p2 + cgd_n2 * cgs_n1 * gb_n1 + cgd_n2 * cgs_n1 * gb_n2 + cgd_n2 * cgs_n1 * gm_n2 + cgd_n2 * cgs_n1 * go_b1 + cgd_n2 * cgs_n1 * go_n1 + cgd_n2 * cgs_n1 * go_n2 + cgd_p2 * cgs_n1 * gb_n1 + cgd_p2 * cgs_n1 * gb_n2 + cgd_p2 * cgs_n1 * gm_n2 + cgd_p2 * cgs_n1 * go_b1 + cgd_p2 * cgs_n1 * go_n1 + cgd_p2 * cgs_n1 * go_n2 + cgs_n1 * cgs_n2 * go_n2 + cgs_n1 * cgs_n2 * go_p2) / (
                                                                                                    cgd_n1 * gb_n1 * go_n2 + cgd_n1 * gb_n1 * go_p2 + cgd_n1 * gb_n2 * go_p2 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p2 + cgd_n1 * gm_n2 * go_p2 + cgd_n1 * go_b1 * go_n2 + cgd_n1 * go_b1 * go_p2 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p2 + cgd_n1 * go_n2 * go_p2 + cgs_n1 * gb_n1 * go_n2 + cgs_n1 * gb_n1 * go_p2 + cgs_n1 * gb_n2 * go_p2 + cgs_n1 * gm_n2 * go_p2 + cgs_n1 * go_b1 * go_n2 + cgs_n1 * go_b1 * go_p2 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p2 + cgs_n1 * go_n2 * go_p2) + s) * (
                                                                                                   cgd_n1 * gb_n1 * go_n2 + cgd_n1 * gb_n1 * go_p2 + cgd_n1 * gb_n2 * go_p2 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p2 + cgd_n1 * gm_n2 * go_p2 + cgd_n1 * go_b1 * go_n2 + cgd_n1 * go_b1 * go_p2 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p2 + cgd_n1 * go_n2 * go_p2 + cgs_n1 * gb_n1 * go_n2 + cgs_n1 * gb_n1 * go_p2 + cgs_n1 * gb_n2 * go_p2 + cgs_n1 * gm_n2 * go_p2 + cgs_n1 * go_b1 * go_n2 + cgs_n1 * go_b1 * go_p2 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p2 + cgs_n1 * go_n2 * go_p2))
    a[2] = 1.0 * gm_n1 * (1.0 * cgs_n1 * s / gm_n1 + 1.0) * (gb_n2 + gm_n2 + go_n2) / ((1.0 * s * (
                cgd_b1 + cgs_n1 + cgs_n2) / (gb_n1 + gb_n2 + gm_n1 + gm_n2 + go_b1 + go_n1 + go_n2) + 1.0) * (
                                                                                                   gb_n1 + gb_n2 + gm_n1 + gm_n2 + go_b1 + go_n1 + go_n2))
    a[3] = 1.0 * gm_n1 * (1.0 * cgs_n1 * s / gm_n1 + 1.0) * (gb_n2 + gm_n2 + go_n2) / ((s ** 2 * (
                cgd_b1 * cgd_n1 + cgd_b1 * cgs_n1 + cgd_n1 * cgs_n1 + cgd_n1 * cgs_n2 + cgs_n1 * cgs_n2) / (
                                                                                                    cgd_n1 * gb_n1 + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 + cgd_n1 * go_b1 + cgd_n1 * go_n1 + cgd_n1 * go_n2 + cgs_n1 * gb_n1 + cgs_n1 * gb_n2 + cgs_n1 * gm_n2 + cgs_n1 * go_b1 + cgs_n1 * go_n1 + cgs_n1 * go_n2) + s) * (
                                                                                                   cgd_n1 * gb_n1 + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 + cgd_n1 * go_b1 + cgd_n1 * go_n1 + cgd_n1 * go_n2 + cgs_n1 * gb_n1 + cgs_n1 * gb_n2 + cgs_n1 * gm_n2 + cgs_n1 * go_b1 + cgs_n1 * go_n1 + cgs_n1 * go_n2))
    return a


def gm_middle_neg(small_signal_param, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2 = gm
    go_n1, go_n2, go_p1, go_p2 = go
    gb_n1, gb_n2, gb_p1, gb_p2 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * gm_n2 * gm_p1 * (1.0 * cgd_n2 * cgd_p1 * s ** 2 / (gm_n2 * gm_p1) + s * (
                -1.0 * cgd_n2 / gm_n2 - 1.0 * cgd_p1 / gm_p1) + 1.0) / ((go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1) * (
                s ** 2 * (
                    cgd_n2 * cgd_p1 + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_p1 * cgd_p2 + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2) / (
                            (go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1)) + s * (
                            cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_n2 * go_p1 + cgd_n2 * go_p2 + cgd_p1 * go_n2 + cgd_p1 * go_p2 + cgd_p2 * gm_n1 + cgd_p2 * go_n1 + cgd_p2 * go_p1 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2) / (
                            (go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1)) + 1))
    a[1] = 1.0 * gm_n2 * gm_p1 * (1.0 * cgd_n2 * cgd_p1 * s ** 2 / (gm_n2 * gm_p1) + s * (
                -1.0 * cgd_n2 / gm_n2 - 1.0 * cgd_p1 / gm_p1) + 1.0) / ((go_n2 + go_p2) * (s ** 3 * (
                cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                                                       (
                                                                                                                   go_n2 + go_p2) * (
                                                                                                                   cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s ** 2 * (
                                                                                                       cgd_n2 * cgd_p1 * gm_n1 + cgd_n2 * cgd_p1 * gm_n2 + cgd_n2 * cgd_p1 * gm_p1 + cgd_n2 * cgd_p1 * go_n1 + cgd_n2 * cgd_p1 * go_n2 + cgd_n2 * cgd_p1 * go_p1 + cgd_n2 * cgd_p1 * go_p2 + cgd_n2 * cgs_p1 * gm_n1 + cgd_n2 * cgs_p1 * gm_n2 + cgd_n2 * cgs_p1 * go_n1 + cgd_n2 * cgs_p1 * go_n2 + cgd_n2 * cgs_p1 * go_p1 + cgd_n2 * cgs_p1 * go_p2 + cgd_p1 * cgd_p2 * gm_n1 + cgd_p1 * cgd_p2 * gm_p1 + cgd_p1 * cgd_p2 * go_n1 + cgd_p1 * cgd_p2 * go_p1 + cgd_p1 * cgs_n1 * go_n2 + cgd_p1 * cgs_n1 * go_p2 + cgd_p1 * cgs_n2 * go_n2 + cgd_p1 * cgs_n2 * go_p2 + cgd_p1 * cgs_p1 * go_n2 + cgd_p1 * cgs_p1 * go_p2 + cgd_p2 * cgs_p1 * gm_n1 + cgd_p2 * cgs_p1 * go_n1 + cgd_p2 * cgs_p1 * go_p1 + cgs_n1 * cgs_p1 * go_n2 + cgs_n1 * cgs_p1 * go_p2 + cgs_n2 * cgs_p1 * go_n2 + cgs_n2 * cgs_p1 * go_p2) / (
                                                                                                       (
                                                                                                                   go_n2 + go_p2) * (
                                                                                                                   cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s) * (
                                                                                    cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    a[2] = 1.0 * gm_n2 * gm_p1 * (1.0 * cgd_n2 * cgd_p1 * s ** 2 / (gm_n2 * gm_p1) + s * (
                -1.0 * cgd_n2 / gm_n2 - 1.0 * cgd_p1 / gm_p1) + 1.0) / (
                       (1.0 * s * (cgd_n2 + cgd_p1 + cgs_n1 + cgs_n2) / (gm_n1 + go_n1 + go_p1) + 1.0) * (
                           gm_n1 + go_n1 + go_p1))
    a[3] = 1.0 * gm_n2 * gm_p1 * (1.0 * cgd_n2 * cgd_p1 * s ** 2 / (gm_n2 * gm_p1) + s * (
                -1.0 * cgd_n2 / gm_n2 - 1.0 * cgd_p1 / gm_p1) + 1.0) / ((s ** 2 * (
                cgd_n2 * cgd_p1 + cgd_n2 * cgs_p1 + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1) / (
                                                                                     cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1) + s) * (
                                                                                    cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    return a


def gm_middle_pos(small_signal_param, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_p1, gm_b1 = gm
    go_p1, go_b1 = go
    gb_p1, gb_p1 = gb
    cgs_p1, cgs_b1 = cgs
    cgd_p1, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = -1.0 * gm_p1 * (-1.0 * cgd_p1 * s / gm_p1 + 1.0) / (
            (go_b1 + go_p1) * (s * (cgd_b1 + cgd_p1) / (go_b1 + go_p1) + 1))
    a[1] = -1.0 * gm_p1 * (-1.0 * cgd_p1 * s / gm_p1 + 1.0) / ((s ** 2 * (
                cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (
                                                                            cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1) + s) * (
                                                                           cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1))
    a[2] = -1.0 * gm_p1 * (-1.0 * cgd_p1 * s / gm_p1 + 1.0)
    a[3] = -1.0 * gm_p1 * (-1.0 * cgd_p1 * s / gm_p1 + 1.0) / (s * (cgd_p1 + cgs_p1))
    return a


def gm_diff_pos_r_series(small_signal_param, R, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2, gm_b1 = gm
    go_n1, go_n2, go_p1, go_p2, go_b1 = go
    gb_n1, gb_n2, gb_p1, gb_p2, gb_b1 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2, cgs_b1 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = -1.0 * gm_n1 * (-1.0 * cgd_n1 * s ** 2 * (cgd_b1 + cgs_n1 + cgs_n2) / (
                gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2)) + 1.0 + 1.0 * s * (
                                       cgd_b1 * gm_n1 - cgd_n1 * gb_n1 - cgd_n1 * gb_n2 - cgd_n1 * gm_n1 - cgd_n1 * gm_n2 - cgd_n1 * go_b1 - cgd_n1 * go_n1 - cgd_n1 * go_n2 - cgs_n1 * gb_n1 - cgs_n1 * go_n1 + cgs_n2 * gm_n1) / (
                                       gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2))) * (gb_n2 + gm_n2 + go_b1 + go_n2) / ((
                                                                                                                                  s ** 2 * (
                                                                                                                                      cgd_n1 + cgd_p1) * (
                                                                                                                                              cgd_b1 + cgs_n1 + cgs_n2) / (
                                                                                                                                              gb_n1 * go_p1 + gb_n2 * go_n1 + gb_n2 * go_p1 + gm_n1 * go_p1 + gm_n2 * go_n1 + gm_n2 * go_p1 + go_b1 * go_n1 + go_b1 * go_p1 + go_n1 * go_n2 + go_n1 * go_p1 + go_n2 * go_p1) + s * (
                                                                                                                                              cgd_b1 * go_n1 + cgd_b1 * go_p1 + cgd_n1 * gb_n1 + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 + cgd_n1 * go_b1 + cgd_n1 * go_n1 + cgd_n1 * go_n2 + cgd_p1 * gb_n1 + cgd_p1 * gb_n2 + cgd_p1 * gm_n1 + cgd_p1 * gm_n2 + cgd_p1 * go_b1 + cgd_p1 * go_n1 + cgd_p1 * go_n2 + cgs_n1 * go_n1 + cgs_n1 * go_p1 + cgs_n2 * go_n1 + cgs_n2 * go_p1) / (
                                                                                                                                              gb_n1 * go_p1 + gb_n2 * go_n1 + gb_n2 * go_p1 + gm_n1 * go_p1 + gm_n2 * go_n1 + gm_n2 * go_p1 + go_b1 * go_n1 + go_b1 * go_p1 + go_n1 * go_n2 + go_n1 * go_p1 + go_n2 * go_p1) + 1) * (
                                                                                                                                  gb_n1 * go_p1 + gb_n2 * go_n1 + gb_n2 * go_p1 + gm_n1 * go_p1 + gm_n2 * go_n1 + gm_n2 * go_p1 + go_b1 * go_n1 + go_b1 * go_p1 + go_n1 * go_n2 + go_n1 * go_p1 + go_n2 * go_p1))
    a[1] = -1.0 * gm_n1 * (-1.0 * cgd_n1 * s ** 2 * (cgd_b1 + cgs_n1 + cgs_n2) / (
                gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2)) + 1.0 + 1.0 * s * (
                                       cgd_b1 * gm_n1 - cgd_n1 * gb_n1 - cgd_n1 * gb_n2 - cgd_n1 * gm_n1 - cgd_n1 * gm_n2 - cgd_n1 * go_b1 - cgd_n1 * go_n1 - cgd_n1 * go_n2 - cgs_n1 * gb_n1 - cgs_n1 * go_n1 + cgs_n2 * gm_n1) / (
                                       gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2))) * (gb_n2 + gm_n2 + go_b1 + go_n2) / ((
                                                                                                                                  s ** 3 * (
                                                                                                                                      cgd_b1 * cgd_n1 * cgd_p1 + cgd_b1 * cgd_n1 * cgs_n1 + cgd_b1 * cgd_p1 * cgs_n1 + cgd_n1 * cgd_p1 * cgs_n1 + cgd_n1 * cgd_p1 * cgs_n2 + cgd_n1 * cgs_n1 * cgs_n2 + cgd_p1 * cgs_n1 * cgs_n2) / (
                                                                                                                                              cgd_n1 * gb_n1 * go_p1 + cgd_n1 * gb_n2 * gm_n1 + cgd_n1 * gb_n2 * go_n1 + cgd_n1 * gb_n2 * go_p1 + cgd_n1 * gm_n1 * gm_n2 + cgd_n1 * gm_n1 * go_b1 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p1 + cgd_n1 * gm_n2 * go_n1 + cgd_n1 * gm_n2 * go_p1 + cgd_n1 * go_b1 * go_n1 + cgd_n1 * go_b1 * go_p1 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p1 + cgd_n1 * go_n2 * go_p1 + cgs_n1 * gb_n1 * go_p1 + cgs_n1 * gb_n2 * go_n1 + cgs_n1 * gb_n2 * go_p1 + cgs_n1 * gm_n2 * go_n1 + cgs_n1 * gm_n2 * go_p1 + cgs_n1 * go_b1 * go_n1 + cgs_n1 * go_b1 * go_p1 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p1 + cgs_n1 * go_n2 * go_p1) + s ** 2 * (
                                                                                                                                              cgd_b1 * cgd_n1 * gm_n1 + cgd_b1 * cgd_n1 * go_n1 + cgd_b1 * cgd_n1 * go_p1 + cgd_b1 * cgs_n1 * go_n1 + cgd_b1 * cgs_n1 * go_p1 + cgd_n1 * cgd_p1 * gb_n1 + cgd_n1 * cgd_p1 * gb_n2 + cgd_n1 * cgd_p1 * gm_n1 + cgd_n1 * cgd_p1 * gm_n2 + cgd_n1 * cgd_p1 * go_b1 + cgd_n1 * cgd_p1 * go_n1 + cgd_n1 * cgd_p1 * go_n2 + cgd_n1 * cgs_n1 * gb_n2 + cgd_n1 * cgs_n1 * gm_n2 + cgd_n1 * cgs_n1 * go_b1 + cgd_n1 * cgs_n1 * go_n2 + cgd_n1 * cgs_n1 * go_p1 + cgd_n1 * cgs_n2 * gm_n1 + cgd_n1 * cgs_n2 * go_n1 + cgd_n1 * cgs_n2 * go_p1 + cgd_p1 * cgs_n1 * gb_n1 + cgd_p1 * cgs_n1 * gb_n2 + cgd_p1 * cgs_n1 * gm_n2 + cgd_p1 * cgs_n1 * go_b1 + cgd_p1 * cgs_n1 * go_n1 + cgd_p1 * cgs_n1 * go_n2 + cgs_n1 * cgs_n2 * go_n1 + cgs_n1 * cgs_n2 * go_p1) / (
                                                                                                                                              cgd_n1 * gb_n1 * go_p1 + cgd_n1 * gb_n2 * gm_n1 + cgd_n1 * gb_n2 * go_n1 + cgd_n1 * gb_n2 * go_p1 + cgd_n1 * gm_n1 * gm_n2 + cgd_n1 * gm_n1 * go_b1 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p1 + cgd_n1 * gm_n2 * go_n1 + cgd_n1 * gm_n2 * go_p1 + cgd_n1 * go_b1 * go_n1 + cgd_n1 * go_b1 * go_p1 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p1 + cgd_n1 * go_n2 * go_p1 + cgs_n1 * gb_n1 * go_p1 + cgs_n1 * gb_n2 * go_n1 + cgs_n1 * gb_n2 * go_p1 + cgs_n1 * gm_n2 * go_n1 + cgs_n1 * gm_n2 * go_p1 + cgs_n1 * go_b1 * go_n1 + cgs_n1 * go_b1 * go_p1 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p1 + cgs_n1 * go_n2 * go_p1) + s) * (
                                                                                                                                  cgd_n1 * gb_n1 * go_p1 + cgd_n1 * gb_n2 * gm_n1 + cgd_n1 * gb_n2 * go_n1 + cgd_n1 * gb_n2 * go_p1 + cgd_n1 * gm_n1 * gm_n2 + cgd_n1 * gm_n1 * go_b1 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p1 + cgd_n1 * gm_n2 * go_n1 + cgd_n1 * gm_n2 * go_p1 + cgd_n1 * go_b1 * go_n1 + cgd_n1 * go_b1 * go_p1 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p1 + cgd_n1 * go_n2 * go_p1 + cgs_n1 * gb_n1 * go_p1 + cgs_n1 * gb_n2 * go_n1 + cgs_n1 * gb_n2 * go_p1 + cgs_n1 * gm_n2 * go_n1 + cgs_n1 * gm_n2 * go_p1 + cgs_n1 * go_b1 * go_n1 + cgs_n1 * go_b1 * go_p1 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p1 + cgs_n1 * go_n2 * go_p1))
    a[2] = -1.0 * gm_n1 * (-1.0 * cgd_n1 * s ** 2 * (cgd_b1 + cgs_n1 + cgs_n2) / (
                gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2)) + 1.0 + 1.0 * s * (
                                       cgd_b1 * gm_n1 - cgd_n1 * gb_n1 - cgd_n1 * gb_n2 - cgd_n1 * gm_n1 - cgd_n1 * gm_n2 - cgd_n1 * go_b1 - cgd_n1 * go_n1 - cgd_n1 * go_n2 - cgs_n1 * gb_n1 - cgs_n1 * go_n1 + cgs_n2 * gm_n1) / (
                                       gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2))) * (gb_n2 + gm_n2 + go_b1 + go_n2) / ((
                                                                                                                                  R * s ** 2 * (
                                                                                                                                      cgd_n1 + cgd_p1) * (
                                                                                                                                              cgd_b1 + cgs_n1 + cgs_n2) / (
                                                                                                                                              R * gb_n1 * go_p1 + R * gb_n2 * go_n1 + R * gb_n2 * go_p1 + R * gm_n1 * go_p1 + R * gm_n2 * go_n1 + R * gm_n2 * go_p1 + R * go_b1 * go_n1 + R * go_b1 * go_p1 + R * go_n1 * go_n2 + R * go_n1 * go_p1 + R * go_n2 * go_p1 + gb_n1 + gb_n2 + gm_n1 + gm_n2 + go_b1 + go_n1 + go_n2) + s * (
                                                                                                                                              R * cgd_b1 * go_n1 + R * cgd_b1 * go_p1 + R * cgd_n1 * gb_n1 + R * cgd_n1 * gb_n2 + R * cgd_n1 * gm_n1 + R * cgd_n1 * gm_n2 + R * cgd_n1 * go_b1 + R * cgd_n1 * go_n1 + R * cgd_n1 * go_n2 + R * cgd_p1 * gb_n1 + R * cgd_p1 * gb_n2 + R * cgd_p1 * gm_n1 + R * cgd_p1 * gm_n2 + R * cgd_p1 * go_b1 + R * cgd_p1 * go_n1 + R * cgd_p1 * go_n2 + R * cgs_n1 * go_n1 + R * cgs_n1 * go_p1 + R * cgs_n2 * go_n1 + R * cgs_n2 * go_p1 + cgd_b1 + cgs_n1 + cgs_n2) / (
                                                                                                                                              R * gb_n1 * go_p1 + R * gb_n2 * go_n1 + R * gb_n2 * go_p1 + R * gm_n1 * go_p1 + R * gm_n2 * go_n1 + R * gm_n2 * go_p1 + R * go_b1 * go_n1 + R * go_b1 * go_p1 + R * go_n1 * go_n2 + R * go_n1 * go_p1 + R * go_n2 * go_p1 + gb_n1 + gb_n2 + gm_n1 + gm_n2 + go_b1 + go_n1 + go_n2) + 1) * (
                                                                                                                                  R * gb_n1 * go_p1 + R * gb_n2 * go_n1 + R * gb_n2 * go_p1 + R * gm_n1 * go_p1 + R * gm_n2 * go_n1 + R * gm_n2 * go_p1 + R * go_b1 * go_n1 + R * go_b1 * go_p1 + R * go_n1 * go_n2 + R * go_n1 * go_p1 + R * go_n2 * go_p1 + gb_n1 + gb_n2 + gm_n1 + gm_n2 + go_b1 + go_n1 + go_n2))
    a[3] = -1.0 * gm_n1 * (-1.0 * cgd_n1 * s ** 2 * (cgd_b1 + cgs_n1 + cgs_n2) / (
                gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2)) + 1.0 + 1.0 * s * (
                                       cgd_b1 * gm_n1 - cgd_n1 * gb_n1 - cgd_n1 * gb_n2 - cgd_n1 * gm_n1 - cgd_n1 * gm_n2 - cgd_n1 * go_b1 - cgd_n1 * go_n1 - cgd_n1 * go_n2 - cgs_n1 * gb_n1 - cgs_n1 * go_n1 + cgs_n2 * gm_n1) / (
                                       gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2))) * (gb_n2 + gm_n2 + go_b1 + go_n2) / ((
                                                                                                                                  R * s ** 3 * (
                                                                                                                                      cgd_b1 * cgd_n1 * cgd_p1 + cgd_b1 * cgd_n1 * cgs_n1 + cgd_b1 * cgd_p1 * cgs_n1 + cgd_n1 * cgd_p1 * cgs_n1 + cgd_n1 * cgd_p1 * cgs_n2 + cgd_n1 * cgs_n1 * cgs_n2 + cgd_p1 * cgs_n1 * cgs_n2) / (
                                                                                                                                              R * cgd_n1 * gb_n1 * go_p1 + R * cgd_n1 * gb_n2 * gm_n1 + R * cgd_n1 * gb_n2 * go_n1 + R * cgd_n1 * gb_n2 * go_p1 + R * cgd_n1 * gm_n1 * gm_n2 + R * cgd_n1 * gm_n1 * go_b1 + R * cgd_n1 * gm_n1 * go_n2 + R * cgd_n1 * gm_n1 * go_p1 + R * cgd_n1 * gm_n2 * go_n1 + R * cgd_n1 * gm_n2 * go_p1 + R * cgd_n1 * go_b1 * go_n1 + R * cgd_n1 * go_b1 * go_p1 + R * cgd_n1 * go_n1 * go_n2 + R * cgd_n1 * go_n1 * go_p1 + R * cgd_n1 * go_n2 * go_p1 + R * cgs_n1 * gb_n1 * go_p1 + R * cgs_n1 * gb_n2 * go_n1 + R * cgs_n1 * gb_n2 * go_p1 + R * cgs_n1 * gm_n2 * go_n1 + R * cgs_n1 * gm_n2 * go_p1 + R * cgs_n1 * go_b1 * go_n1 + R * cgs_n1 * go_b1 * go_p1 + R * cgs_n1 * go_n1 * go_n2 + R * cgs_n1 * go_n1 * go_p1 + R * cgs_n1 * go_n2 * go_p1 + cgd_n1 * gb_n1 + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 + cgd_n1 * go_b1 + cgd_n1 * go_n1 + cgd_n1 * go_n2 + cgs_n1 * gb_n1 + cgs_n1 * gb_n2 + cgs_n1 * gm_n2 + cgs_n1 * go_b1 + cgs_n1 * go_n1 + cgs_n1 * go_n2) + s ** 2 * (
                                                                                                                                              R * cgd_b1 * cgd_n1 * gm_n1 + R * cgd_b1 * cgd_n1 * go_n1 + R * cgd_b1 * cgd_n1 * go_p1 + R * cgd_b1 * cgs_n1 * go_n1 + R * cgd_b1 * cgs_n1 * go_p1 + R * cgd_n1 * cgd_p1 * gb_n1 + R * cgd_n1 * cgd_p1 * gb_n2 + R * cgd_n1 * cgd_p1 * gm_n1 + R * cgd_n1 * cgd_p1 * gm_n2 + R * cgd_n1 * cgd_p1 * go_b1 + R * cgd_n1 * cgd_p1 * go_n1 + R * cgd_n1 * cgd_p1 * go_n2 + R * cgd_n1 * cgs_n1 * gb_n2 + R * cgd_n1 * cgs_n1 * gm_n2 + R * cgd_n1 * cgs_n1 * go_b1 + R * cgd_n1 * cgs_n1 * go_n2 + R * cgd_n1 * cgs_n1 * go_p1 + R * cgd_n1 * cgs_n2 * gm_n1 + R * cgd_n1 * cgs_n2 * go_n1 + R * cgd_n1 * cgs_n2 * go_p1 + R * cgd_p1 * cgs_n1 * gb_n1 + R * cgd_p1 * cgs_n1 * gb_n2 + R * cgd_p1 * cgs_n1 * gm_n2 + R * cgd_p1 * cgs_n1 * go_b1 + R * cgd_p1 * cgs_n1 * go_n1 + R * cgd_p1 * cgs_n1 * go_n2 + R * cgs_n1 * cgs_n2 * go_n1 + R * cgs_n1 * cgs_n2 * go_p1 + cgd_b1 * cgd_n1 + cgd_b1 * cgs_n1 + cgd_n1 * cgs_n1 + cgd_n1 * cgs_n2 + cgs_n1 * cgs_n2) / (
                                                                                                                                              R * cgd_n1 * gb_n1 * go_p1 + R * cgd_n1 * gb_n2 * gm_n1 + R * cgd_n1 * gb_n2 * go_n1 + R * cgd_n1 * gb_n2 * go_p1 + R * cgd_n1 * gm_n1 * gm_n2 + R * cgd_n1 * gm_n1 * go_b1 + R * cgd_n1 * gm_n1 * go_n2 + R * cgd_n1 * gm_n1 * go_p1 + R * cgd_n1 * gm_n2 * go_n1 + R * cgd_n1 * gm_n2 * go_p1 + R * cgd_n1 * go_b1 * go_n1 + R * cgd_n1 * go_b1 * go_p1 + R * cgd_n1 * go_n1 * go_n2 + R * cgd_n1 * go_n1 * go_p1 + R * cgd_n1 * go_n2 * go_p1 + R * cgs_n1 * gb_n1 * go_p1 + R * cgs_n1 * gb_n2 * go_n1 + R * cgs_n1 * gb_n2 * go_p1 + R * cgs_n1 * gm_n2 * go_n1 + R * cgs_n1 * gm_n2 * go_p1 + R * cgs_n1 * go_b1 * go_n1 + R * cgs_n1 * go_b1 * go_p1 + R * cgs_n1 * go_n1 * go_n2 + R * cgs_n1 * go_n1 * go_p1 + R * cgs_n1 * go_n2 * go_p1 + cgd_n1 * gb_n1 + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 + cgd_n1 * go_b1 + cgd_n1 * go_n1 + cgd_n1 * go_n2 + cgs_n1 * gb_n1 + cgs_n1 * gb_n2 + cgs_n1 * gm_n2 + cgs_n1 * go_b1 + cgs_n1 * go_n1 + cgs_n1 * go_n2) + s) * (
                                                                                                                                  R * cgd_n1 * gb_n1 * go_p1 + R * cgd_n1 * gb_n2 * gm_n1 + R * cgd_n1 * gb_n2 * go_n1 + R * cgd_n1 * gb_n2 * go_p1 + R * cgd_n1 * gm_n1 * gm_n2 + R * cgd_n1 * gm_n1 * go_b1 + R * cgd_n1 * gm_n1 * go_n2 + R * cgd_n1 * gm_n1 * go_p1 + R * cgd_n1 * gm_n2 * go_n1 + R * cgd_n1 * gm_n2 * go_p1 + R * cgd_n1 * go_b1 * go_n1 + R * cgd_n1 * go_b1 * go_p1 + R * cgd_n1 * go_n1 * go_n2 + R * cgd_n1 * go_n1 * go_p1 + R * cgd_n1 * go_n2 * go_p1 + R * cgs_n1 * gb_n1 * go_p1 + R * cgs_n1 * gb_n2 * go_n1 + R * cgs_n1 * gb_n2 * go_p1 + R * cgs_n1 * gm_n2 * go_n1 + R * cgs_n1 * gm_n2 * go_p1 + R * cgs_n1 * go_b1 * go_n1 + R * cgs_n1 * go_b1 * go_p1 + R * cgs_n1 * go_n1 * go_n2 + R * cgs_n1 * go_n1 * go_p1 + R * cgs_n1 * go_n2 * go_p1 + cgd_n1 * gb_n1 + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 + cgd_n1 * go_b1 + cgd_n1 * go_n1 + cgd_n1 * go_n2 + cgs_n1 * gb_n1 + cgs_n1 * gb_n2 + cgs_n1 * gm_n2 + cgs_n1 * go_b1 + cgs_n1 * go_n1 + cgs_n1 * go_n2))
    return a


def gm_middle_pos_r_series(small_signal_param, r, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_p1, gm_b1 = gm
    go_p1, go_b1 = go
    gb_p1, gb_p1 = gb
    cgs_p1, cgs_b1 = cgs
    cgd_p1, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = -1.0 * gm_p1 * (-1.0 * cgd_p1 * s / gm_p1 + 1.0) / (
                (go_b1 + go_p1) * (s * (cgd_b1 + cgd_p1) / (go_b1 + go_p1) + 1))
    a[1] = -1.0 * gm_p1 * (-1.0 * cgd_p1 * s / gm_p1 + 1.0) / ((s ** 2 * (
                cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (
                                                                            cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1) + s) * (
                                                                           cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1))
    a[2] = -1.0 * gm_p1 * (-1.0 * cgd_p1 * s / gm_p1 + 1.0) / (
                (1.0 * r * s * (cgd_b1 + cgd_p1) / (go_b1 * r + go_p1 * r + 1) + 1.0) * (go_b1 * r + go_p1 * r + 1))
    a[3] = -1.0 * gm_p1 * (-1.0 * cgd_p1 * s / gm_p1 + 1.0) / ((r * s ** 2 * (
                cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (
                                                                            cgd_p1 * gm_p1 * r + cgd_p1 * go_b1 * r + cgd_p1 * go_p1 * r + cgd_p1 + cgs_p1 * go_b1 * r + cgs_p1 * go_p1 * r + cgs_p1) + s) * (
                                                                           cgd_p1 * gm_p1 * r + cgd_p1 * go_b1 * r + cgd_p1 * go_p1 * r + cgd_p1 + cgs_p1 * go_b1 * r + cgs_p1 * go_p1 * r + cgs_p1))
    return a


def gm_diff_pos_c_series(small_signal_param, c, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2, gm_b1 = gm
    go_n1, go_n2, go_p1, go_p2, go_b1 = go
    gb_n1, gb_n2, gb_p1, gb_p2, gb_b1 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2, cgs_b1 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = -1.0 * gm_n1 * (-1.0 * cgd_n1 * s ** 2 * (cgd_b1 + cgs_n1 + cgs_n2) / (
                gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2)) + 1.0 + 1.0 * s * (
                                       cgd_b1 * gm_n1 - cgd_n1 * gb_n1 - cgd_n1 * gb_n2 - cgd_n1 * gm_n1 - cgd_n1 * gm_n2 - cgd_n1 * go_b1 - cgd_n1 * go_n1 - cgd_n1 * go_n2 - cgs_n1 * gb_n1 - cgs_n1 * go_n1 + cgs_n2 * gm_n1) / (
                                       gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2))) * (gb_n2 + gm_n2 + go_b1 + go_n2) / ((
                                                                                                                                  s ** 2 * (
                                                                                                                                      cgd_n1 + cgd_p1) * (
                                                                                                                                              cgd_b1 + cgs_n1 + cgs_n2) / (
                                                                                                                                              gb_n1 * go_p1 + gb_n2 * go_n1 + gb_n2 * go_p1 + gm_n1 * go_p1 + gm_n2 * go_n1 + gm_n2 * go_p1 + go_b1 * go_n1 + go_b1 * go_p1 + go_n1 * go_n2 + go_n1 * go_p1 + go_n2 * go_p1) + s * (
                                                                                                                                              cgd_b1 * go_n1 + cgd_b1 * go_p1 + cgd_n1 * gb_n1 + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 + cgd_n1 * go_b1 + cgd_n1 * go_n1 + cgd_n1 * go_n2 + cgd_p1 * gb_n1 + cgd_p1 * gb_n2 + cgd_p1 * gm_n1 + cgd_p1 * gm_n2 + cgd_p1 * go_b1 + cgd_p1 * go_n1 + cgd_p1 * go_n2 + cgs_n1 * go_n1 + cgs_n1 * go_p1 + cgs_n2 * go_n1 + cgs_n2 * go_p1) / (
                                                                                                                                              gb_n1 * go_p1 + gb_n2 * go_n1 + gb_n2 * go_p1 + gm_n1 * go_p1 + gm_n2 * go_n1 + gm_n2 * go_p1 + go_b1 * go_n1 + go_b1 * go_p1 + go_n1 * go_n2 + go_n1 * go_p1 + go_n2 * go_p1) + 1) * (
                                                                                                                                  gb_n1 * go_p1 + gb_n2 * go_n1 + gb_n2 * go_p1 + gm_n1 * go_p1 + gm_n2 * go_n1 + gm_n2 * go_p1 + go_b1 * go_n1 + go_b1 * go_p1 + go_n1 * go_n2 + go_n1 * go_p1 + go_n2 * go_p1))
    a[1] = -1.0 * gm_n1 * (-1.0 * cgd_n1 * s ** 2 * (cgd_b1 + cgs_n1 + cgs_n2) / (
                gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2)) + 1.0 + 1.0 * s * (
                                       cgd_b1 * gm_n1 - cgd_n1 * gb_n1 - cgd_n1 * gb_n2 - cgd_n1 * gm_n1 - cgd_n1 * gm_n2 - cgd_n1 * go_b1 - cgd_n1 * go_n1 - cgd_n1 * go_n2 - cgs_n1 * gb_n1 - cgs_n1 * go_n1 + cgs_n2 * gm_n1) / (
                                       gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2))) * (gb_n2 + gm_n2 + go_b1 + go_n2) / ((
                                                                                                                                  s ** 3 * (
                                                                                                                                      cgd_b1 * cgd_n1 * cgd_p1 + cgd_b1 * cgd_n1 * cgs_n1 + cgd_b1 * cgd_p1 * cgs_n1 + cgd_n1 * cgd_p1 * cgs_n1 + cgd_n1 * cgd_p1 * cgs_n2 + cgd_n1 * cgs_n1 * cgs_n2 + cgd_p1 * cgs_n1 * cgs_n2) / (
                                                                                                                                              cgd_n1 * gb_n1 * go_p1 + cgd_n1 * gb_n2 * gm_n1 + cgd_n1 * gb_n2 * go_n1 + cgd_n1 * gb_n2 * go_p1 + cgd_n1 * gm_n1 * gm_n2 + cgd_n1 * gm_n1 * go_b1 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p1 + cgd_n1 * gm_n2 * go_n1 + cgd_n1 * gm_n2 * go_p1 + cgd_n1 * go_b1 * go_n1 + cgd_n1 * go_b1 * go_p1 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p1 + cgd_n1 * go_n2 * go_p1 + cgs_n1 * gb_n1 * go_p1 + cgs_n1 * gb_n2 * go_n1 + cgs_n1 * gb_n2 * go_p1 + cgs_n1 * gm_n2 * go_n1 + cgs_n1 * gm_n2 * go_p1 + cgs_n1 * go_b1 * go_n1 + cgs_n1 * go_b1 * go_p1 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p1 + cgs_n1 * go_n2 * go_p1) + s ** 2 * (
                                                                                                                                              cgd_b1 * cgd_n1 * gm_n1 + cgd_b1 * cgd_n1 * go_n1 + cgd_b1 * cgd_n1 * go_p1 + cgd_b1 * cgs_n1 * go_n1 + cgd_b1 * cgs_n1 * go_p1 + cgd_n1 * cgd_p1 * gb_n1 + cgd_n1 * cgd_p1 * gb_n2 + cgd_n1 * cgd_p1 * gm_n1 + cgd_n1 * cgd_p1 * gm_n2 + cgd_n1 * cgd_p1 * go_b1 + cgd_n1 * cgd_p1 * go_n1 + cgd_n1 * cgd_p1 * go_n2 + cgd_n1 * cgs_n1 * gb_n2 + cgd_n1 * cgs_n1 * gm_n2 + cgd_n1 * cgs_n1 * go_b1 + cgd_n1 * cgs_n1 * go_n2 + cgd_n1 * cgs_n1 * go_p1 + cgd_n1 * cgs_n2 * gm_n1 + cgd_n1 * cgs_n2 * go_n1 + cgd_n1 * cgs_n2 * go_p1 + cgd_p1 * cgs_n1 * gb_n1 + cgd_p1 * cgs_n1 * gb_n2 + cgd_p1 * cgs_n1 * gm_n2 + cgd_p1 * cgs_n1 * go_b1 + cgd_p1 * cgs_n1 * go_n1 + cgd_p1 * cgs_n1 * go_n2 + cgs_n1 * cgs_n2 * go_n1 + cgs_n1 * cgs_n2 * go_p1) / (
                                                                                                                                              cgd_n1 * gb_n1 * go_p1 + cgd_n1 * gb_n2 * gm_n1 + cgd_n1 * gb_n2 * go_n1 + cgd_n1 * gb_n2 * go_p1 + cgd_n1 * gm_n1 * gm_n2 + cgd_n1 * gm_n1 * go_b1 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p1 + cgd_n1 * gm_n2 * go_n1 + cgd_n1 * gm_n2 * go_p1 + cgd_n1 * go_b1 * go_n1 + cgd_n1 * go_b1 * go_p1 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p1 + cgd_n1 * go_n2 * go_p1 + cgs_n1 * gb_n1 * go_p1 + cgs_n1 * gb_n2 * go_n1 + cgs_n1 * gb_n2 * go_p1 + cgs_n1 * gm_n2 * go_n1 + cgs_n1 * gm_n2 * go_p1 + cgs_n1 * go_b1 * go_n1 + cgs_n1 * go_b1 * go_p1 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p1 + cgs_n1 * go_n2 * go_p1) + s) * (
                                                                                                                                  cgd_n1 * gb_n1 * go_p1 + cgd_n1 * gb_n2 * gm_n1 + cgd_n1 * gb_n2 * go_n1 + cgd_n1 * gb_n2 * go_p1 + cgd_n1 * gm_n1 * gm_n2 + cgd_n1 * gm_n1 * go_b1 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p1 + cgd_n1 * gm_n2 * go_n1 + cgd_n1 * gm_n2 * go_p1 + cgd_n1 * go_b1 * go_n1 + cgd_n1 * go_b1 * go_p1 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p1 + cgd_n1 * go_n2 * go_p1 + cgs_n1 * gb_n1 * go_p1 + cgs_n1 * gb_n2 * go_n1 + cgs_n1 * gb_n2 * go_p1 + cgs_n1 * gm_n2 * go_n1 + cgs_n1 * gm_n2 * go_p1 + cgs_n1 * go_b1 * go_n1 + cgs_n1 * go_b1 * go_p1 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p1 + cgs_n1 * go_n2 * go_p1))
    a[2] = -1.0 * c * gm_n1 * (-1.0 * cgd_n1 * s ** 3 * (cgd_b1 + cgs_n1 + cgs_n2) / (
                gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2)) + 1.0 * s + 1.0 * s ** 2 * (
                                           cgd_b1 * gm_n1 - cgd_n1 * gb_n1 - cgd_n1 * gb_n2 - cgd_n1 * gm_n1 - cgd_n1 * gm_n2 - cgd_n1 * go_b1 - cgd_n1 * go_n1 - cgd_n1 * go_n2 - cgs_n1 * gb_n1 - cgs_n1 * go_n1 + cgs_n2 * gm_n1) / (
                                           gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2))) * (
                       gb_n2 + gm_n2 + go_b1 + go_n2) / ((s ** 2 * (c + cgd_n1 + cgd_p1) * (
                cgd_b1 + cgs_n1 + cgs_n2) / (
                                                                      gb_n1 * go_p1 + gb_n2 * go_n1 + gb_n2 * go_p1 + gm_n1 * go_p1 + gm_n2 * go_n1 + gm_n2 * go_p1 + go_b1 * go_n1 + go_b1 * go_p1 + go_n1 * go_n2 + go_n1 * go_p1 + go_n2 * go_p1) + s * (
                                                                      c * gb_n1 + c * gb_n2 + c * gm_n1 + c * gm_n2 + c * go_b1 + c * go_n1 + c * go_n2 + cgd_b1 * go_n1 + cgd_b1 * go_p1 + cgd_n1 * gb_n1 + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 + cgd_n1 * go_b1 + cgd_n1 * go_n1 + cgd_n1 * go_n2 + cgd_p1 * gb_n1 + cgd_p1 * gb_n2 + cgd_p1 * gm_n1 + cgd_p1 * gm_n2 + cgd_p1 * go_b1 + cgd_p1 * go_n1 + cgd_p1 * go_n2 + cgs_n1 * go_n1 + cgs_n1 * go_p1 + cgs_n2 * go_n1 + cgs_n2 * go_p1) / (
                                                                      gb_n1 * go_p1 + gb_n2 * go_n1 + gb_n2 * go_p1 + gm_n1 * go_p1 + gm_n2 * go_n1 + gm_n2 * go_p1 + go_b1 * go_n1 + go_b1 * go_p1 + go_n1 * go_n2 + go_n1 * go_p1 + go_n2 * go_p1) + 1) * (
                                                                     gb_n1 * go_p1 + gb_n2 * go_n1 + gb_n2 * go_p1 + gm_n1 * go_p1 + gm_n2 * go_n1 + gm_n2 * go_p1 + go_b1 * go_n1 + go_b1 * go_p1 + go_n1 * go_n2 + go_n1 * go_p1 + go_n2 * go_p1))
    a[3] = -1.0 * c * gm_n1 * (-1.0 * cgd_n1 * s ** 2 * (cgd_b1 + cgs_n1 + cgs_n2) / (
                gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2)) + 1.0 + 1.0 * s * (
                                           cgd_b1 * gm_n1 - cgd_n1 * gb_n1 - cgd_n1 * gb_n2 - cgd_n1 * gm_n1 - cgd_n1 * gm_n2 - cgd_n1 * go_b1 - cgd_n1 * go_n1 - cgd_n1 * go_n2 - cgs_n1 * gb_n1 - cgs_n1 * go_n1 + cgs_n2 * gm_n1) / (
                                           gm_n1 * (gb_n2 + gm_n2 + go_b1 + go_n2))) * (
                       gb_n2 + gm_n2 + go_b1 + go_n2) / ((s ** 2 * (
                c * cgd_b1 * cgd_n1 + c * cgd_b1 * cgs_n1 + c * cgd_n1 * cgs_n1 + c * cgd_n1 * cgs_n2 + c * cgs_n1 * cgs_n2 + cgd_b1 * cgd_n1 * cgd_p1 + cgd_b1 * cgd_n1 * cgs_n1 + cgd_b1 * cgd_p1 * cgs_n1 + cgd_n1 * cgd_p1 * cgs_n1 + cgd_n1 * cgd_p1 * cgs_n2 + cgd_n1 * cgs_n1 * cgs_n2 + cgd_p1 * cgs_n1 * cgs_n2) / (
                                                                      cgd_n1 * gb_n1 * go_p1 + cgd_n1 * gb_n2 * gm_n1 + cgd_n1 * gb_n2 * go_n1 + cgd_n1 * gb_n2 * go_p1 + cgd_n1 * gm_n1 * gm_n2 + cgd_n1 * gm_n1 * go_b1 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p1 + cgd_n1 * gm_n2 * go_n1 + cgd_n1 * gm_n2 * go_p1 + cgd_n1 * go_b1 * go_n1 + cgd_n1 * go_b1 * go_p1 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p1 + cgd_n1 * go_n2 * go_p1 + cgs_n1 * gb_n1 * go_p1 + cgs_n1 * gb_n2 * go_n1 + cgs_n1 * gb_n2 * go_p1 + cgs_n1 * gm_n2 * go_n1 + cgs_n1 * gm_n2 * go_p1 + cgs_n1 * go_b1 * go_n1 + cgs_n1 * go_b1 * go_p1 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p1 + cgs_n1 * go_n2 * go_p1) + s * (
                                                                      c * cgd_n1 * gb_n1 + c * cgd_n1 * gb_n2 + c * cgd_n1 * gm_n1 + c * cgd_n1 * gm_n2 + c * cgd_n1 * go_b1 + c * cgd_n1 * go_n1 + c * cgd_n1 * go_n2 + c * cgs_n1 * gb_n1 + c * cgs_n1 * gb_n2 + c * cgs_n1 * gm_n2 + c * cgs_n1 * go_b1 + c * cgs_n1 * go_n1 + c * cgs_n1 * go_n2 + cgd_b1 * cgd_n1 * gm_n1 + cgd_b1 * cgd_n1 * go_n1 + cgd_b1 * cgd_n1 * go_p1 + cgd_b1 * cgs_n1 * go_n1 + cgd_b1 * cgs_n1 * go_p1 + cgd_n1 * cgd_p1 * gb_n1 + cgd_n1 * cgd_p1 * gb_n2 + cgd_n1 * cgd_p1 * gm_n1 + cgd_n1 * cgd_p1 * gm_n2 + cgd_n1 * cgd_p1 * go_b1 + cgd_n1 * cgd_p1 * go_n1 + cgd_n1 * cgd_p1 * go_n2 + cgd_n1 * cgs_n1 * gb_n2 + cgd_n1 * cgs_n1 * gm_n2 + cgd_n1 * cgs_n1 * go_b1 + cgd_n1 * cgs_n1 * go_n2 + cgd_n1 * cgs_n1 * go_p1 + cgd_n1 * cgs_n2 * gm_n1 + cgd_n1 * cgs_n2 * go_n1 + cgd_n1 * cgs_n2 * go_p1 + cgd_p1 * cgs_n1 * gb_n1 + cgd_p1 * cgs_n1 * gb_n2 + cgd_p1 * cgs_n1 * gm_n2 + cgd_p1 * cgs_n1 * go_b1 + cgd_p1 * cgs_n1 * go_n1 + cgd_p1 * cgs_n1 * go_n2 + cgs_n1 * cgs_n2 * go_n1 + cgs_n1 * cgs_n2 * go_p1) / (
                                                                      cgd_n1 * gb_n1 * go_p1 + cgd_n1 * gb_n2 * gm_n1 + cgd_n1 * gb_n2 * go_n1 + cgd_n1 * gb_n2 * go_p1 + cgd_n1 * gm_n1 * gm_n2 + cgd_n1 * gm_n1 * go_b1 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p1 + cgd_n1 * gm_n2 * go_n1 + cgd_n1 * gm_n2 * go_p1 + cgd_n1 * go_b1 * go_n1 + cgd_n1 * go_b1 * go_p1 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p1 + cgd_n1 * go_n2 * go_p1 + cgs_n1 * gb_n1 * go_p1 + cgs_n1 * gb_n2 * go_n1 + cgs_n1 * gb_n2 * go_p1 + cgs_n1 * gm_n2 * go_n1 + cgs_n1 * gm_n2 * go_p1 + cgs_n1 * go_b1 * go_n1 + cgs_n1 * go_b1 * go_p1 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p1 + cgs_n1 * go_n2 * go_p1) + 1) * (
                                                                     cgd_n1 * gb_n1 * go_p1 + cgd_n1 * gb_n2 * gm_n1 + cgd_n1 * gb_n2 * go_n1 + cgd_n1 * gb_n2 * go_p1 + cgd_n1 * gm_n1 * gm_n2 + cgd_n1 * gm_n1 * go_b1 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p1 + cgd_n1 * gm_n2 * go_n1 + cgd_n1 * gm_n2 * go_p1 + cgd_n1 * go_b1 * go_n1 + cgd_n1 * go_b1 * go_p1 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p1 + cgd_n1 * go_n2 * go_p1 + cgs_n1 * gb_n1 * go_p1 + cgs_n1 * gb_n2 * go_n1 + cgs_n1 * gb_n2 * go_p1 + cgs_n1 * gm_n2 * go_n1 + cgs_n1 * gm_n2 * go_p1 + cgs_n1 * go_b1 * go_n1 + cgs_n1 * go_b1 * go_p1 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p1 + cgs_n1 * go_n2 * go_p1))
    return a


def gm_middle_pos_c_series(small_signal_param, c, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_p1, gm_b1 = gm
    go_p1, go_b1 = go
    gb_p1, gb_p1 = gb
    cgs_p1, cgs_b1 = cgs
    cgd_p1, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = -1.0 * gm_p1 * (-1.0 * cgd_p1 * s / gm_p1 + 1.0) / (
                (go_b1 + go_p1) * (s * (cgd_b1 + cgd_p1) / (go_b1 + go_p1) + 1))
    a[1] = -1.0 * gm_p1 * (-1.0 * cgd_p1 * s / gm_p1 + 1.0) / ((s ** 2 * (
                cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (
                                                                            cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1) + s) * (
                                                                           cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1))
    a[2] = -1.0 * c * gm_p1 * (-1.0 * cgd_p1 * s ** 2 / gm_p1 + 1.0 * s) / (
                (go_b1 + go_p1) * (1.0 * s * (c + cgd_b1 + cgd_p1) / (go_b1 + go_p1) + 1.0))
    a[3] = -1.0 * c * gm_p1 * (-1.0 * cgd_p1 * s / gm_p1 + 1.0) / ((s * (
                c * cgd_p1 + c * cgs_p1 + cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (
                                                                                cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1) + 1) * (
                                                                               cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1))
    return a


def gm_diff_neg_r_series(small_signal_param, r, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2, gm_b1 = gm
    go_n1, go_n2, go_p1, go_p2, go_b1 = go
    gb_n1, gb_n2, gb_p1, gb_p2, gb_b1 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2, cgs_b1 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * gm_n1 * (1.0 * cgs_n1 * s / gm_n1 + 1.0) * (gb_n2 + gm_n2 + go_n2) / ((s ** 2 * (cgd_n2 + cgd_p2) * (
                cgd_b1 + cgs_n1 + cgs_n2) / (
                                                                                                    gb_n1 * go_n2 + gb_n1 * go_p2 + gb_n2 * go_p2 + gm_n1 * go_n2 + gm_n1 * go_p2 + gm_n2 * go_p2 + go_b1 * go_n2 + go_b1 * go_p2 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p2) + s * (
                                                                                                    cgd_b1 * go_n2 + cgd_b1 * go_p2 + cgd_n2 * gb_n1 + cgd_n2 * gb_n2 + cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * go_b1 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_p2 * gb_n1 + cgd_p2 * gb_n2 + cgd_p2 * gm_n1 + cgd_p2 * gm_n2 + cgd_p2 * go_b1 + cgd_p2 * go_n1 + cgd_p2 * go_n2 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2) / (
                                                                                                    gb_n1 * go_n2 + gb_n1 * go_p2 + gb_n2 * go_p2 + gm_n1 * go_n2 + gm_n1 * go_p2 + gm_n2 * go_p2 + go_b1 * go_n2 + go_b1 * go_p2 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p2) + 1) * (
                                                                                                   gb_n1 * go_n2 + gb_n1 * go_p2 + gb_n2 * go_p2 + gm_n1 * go_n2 + gm_n1 * go_p2 + gm_n2 * go_p2 + go_b1 * go_n2 + go_b1 * go_p2 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p2))
    a[1] = 1.0 * gm_n1 * (1.0 * cgs_n1 * s / gm_n1 + 1.0) * (gb_n2 + gm_n2 + go_n2) / ((s ** 3 * (cgd_n2 + cgd_p2) * (
                cgd_b1 * cgd_n1 + cgd_b1 * cgs_n1 + cgd_n1 * cgs_n1 + cgd_n1 * cgs_n2 + cgs_n1 * cgs_n2) / (
                                                                                                    cgd_n1 * gb_n1 * go_n2 + cgd_n1 * gb_n1 * go_p2 + cgd_n1 * gb_n2 * go_p2 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p2 + cgd_n1 * gm_n2 * go_p2 + cgd_n1 * go_b1 * go_n2 + cgd_n1 * go_b1 * go_p2 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p2 + cgd_n1 * go_n2 * go_p2 + cgs_n1 * gb_n1 * go_n2 + cgs_n1 * gb_n1 * go_p2 + cgs_n1 * gb_n2 * go_p2 + cgs_n1 * gm_n2 * go_p2 + cgs_n1 * go_b1 * go_n2 + cgs_n1 * go_b1 * go_p2 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p2 + cgs_n1 * go_n2 * go_p2) + s ** 2 * (
                                                                                                    cgd_b1 * cgd_n1 * go_n2 + cgd_b1 * cgd_n1 * go_p2 + cgd_b1 * cgs_n1 * go_n2 + cgd_b1 * cgs_n1 * go_p2 + cgd_n1 * cgd_n2 * gb_n1 + cgd_n1 * cgd_n2 * gb_n2 + cgd_n1 * cgd_n2 * gm_n1 + cgd_n1 * cgd_n2 * gm_n2 + cgd_n1 * cgd_n2 * go_b1 + cgd_n1 * cgd_n2 * go_n1 + cgd_n1 * cgd_n2 * go_n2 + cgd_n1 * cgd_p2 * gb_n1 + cgd_n1 * cgd_p2 * gb_n2 + cgd_n1 * cgd_p2 * gm_n1 + cgd_n1 * cgd_p2 * gm_n2 + cgd_n1 * cgd_p2 * go_b1 + cgd_n1 * cgd_p2 * go_n1 + cgd_n1 * cgd_p2 * go_n2 + cgd_n1 * cgs_n1 * go_n2 + cgd_n1 * cgs_n1 * go_p2 + cgd_n1 * cgs_n2 * go_n2 + cgd_n1 * cgs_n2 * go_p2 + cgd_n2 * cgs_n1 * gb_n1 + cgd_n2 * cgs_n1 * gb_n2 + cgd_n2 * cgs_n1 * gm_n2 + cgd_n2 * cgs_n1 * go_b1 + cgd_n2 * cgs_n1 * go_n1 + cgd_n2 * cgs_n1 * go_n2 + cgd_p2 * cgs_n1 * gb_n1 + cgd_p2 * cgs_n1 * gb_n2 + cgd_p2 * cgs_n1 * gm_n2 + cgd_p2 * cgs_n1 * go_b1 + cgd_p2 * cgs_n1 * go_n1 + cgd_p2 * cgs_n1 * go_n2 + cgs_n1 * cgs_n2 * go_n2 + cgs_n1 * cgs_n2 * go_p2) / (
                                                                                                    cgd_n1 * gb_n1 * go_n2 + cgd_n1 * gb_n1 * go_p2 + cgd_n1 * gb_n2 * go_p2 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p2 + cgd_n1 * gm_n2 * go_p2 + cgd_n1 * go_b1 * go_n2 + cgd_n1 * go_b1 * go_p2 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p2 + cgd_n1 * go_n2 * go_p2 + cgs_n1 * gb_n1 * go_n2 + cgs_n1 * gb_n1 * go_p2 + cgs_n1 * gb_n2 * go_p2 + cgs_n1 * gm_n2 * go_p2 + cgs_n1 * go_b1 * go_n2 + cgs_n1 * go_b1 * go_p2 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p2 + cgs_n1 * go_n2 * go_p2) + s) * (
                                                                                                   cgd_n1 * gb_n1 * go_n2 + cgd_n1 * gb_n1 * go_p2 + cgd_n1 * gb_n2 * go_p2 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p2 + cgd_n1 * gm_n2 * go_p2 + cgd_n1 * go_b1 * go_n2 + cgd_n1 * go_b1 * go_p2 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p2 + cgd_n1 * go_n2 * go_p2 + cgs_n1 * gb_n1 * go_n2 + cgs_n1 * gb_n1 * go_p2 + cgs_n1 * gb_n2 * go_p2 + cgs_n1 * gm_n2 * go_p2 + cgs_n1 * go_b1 * go_n2 + cgs_n1 * go_b1 * go_p2 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p2 + cgs_n1 * go_n2 * go_p2))
    a[2] = 1.0 * gm_n1 * (1.0 * cgs_n1 * s / gm_n1 + 1.0) * (gb_n2 + gm_n2 + go_n2) / ((r * s ** 2 * (
                cgd_n2 + cgd_p2) * (cgd_b1 + cgs_n1 + cgs_n2) / (
                                                                                                    gb_n1 * go_n2 * r + gb_n1 * go_p2 * r + gb_n1 + gb_n2 * go_p2 * r + gb_n2 + gm_n1 * go_n2 * r + gm_n1 * go_p2 * r + gm_n1 + gm_n2 * go_p2 * r + gm_n2 + go_b1 * go_n2 * r + go_b1 * go_p2 * r + go_b1 + go_n1 * go_n2 * r + go_n1 * go_p2 * r + go_n1 + go_n2 * go_p2 * r + go_n2) + s * (
                                                                                                    cgd_b1 * go_n2 * r + cgd_b1 * go_p2 * r + cgd_b1 + cgd_n2 * gb_n1 * r + cgd_n2 * gb_n2 * r + cgd_n2 * gm_n1 * r + cgd_n2 * gm_n2 * r + cgd_n2 * go_b1 * r + cgd_n2 * go_n1 * r + cgd_n2 * go_n2 * r + cgd_p2 * gb_n1 * r + cgd_p2 * gb_n2 * r + cgd_p2 * gm_n1 * r + cgd_p2 * gm_n2 * r + cgd_p2 * go_b1 * r + cgd_p2 * go_n1 * r + cgd_p2 * go_n2 * r + cgs_n1 * go_n2 * r + cgs_n1 * go_p2 * r + cgs_n1 + cgs_n2 * go_n2 * r + cgs_n2 * go_p2 * r + cgs_n2) / (
                                                                                                    gb_n1 * go_n2 * r + gb_n1 * go_p2 * r + gb_n1 + gb_n2 * go_p2 * r + gb_n2 + gm_n1 * go_n2 * r + gm_n1 * go_p2 * r + gm_n1 + gm_n2 * go_p2 * r + gm_n2 + go_b1 * go_n2 * r + go_b1 * go_p2 * r + go_b1 + go_n1 * go_n2 * r + go_n1 * go_p2 * r + go_n1 + go_n2 * go_p2 * r + go_n2) + 1) * (
                                                                                                   gb_n1 * go_n2 * r + gb_n1 * go_p2 * r + gb_n1 + gb_n2 * go_p2 * r + gb_n2 + gm_n1 * go_n2 * r + gm_n1 * go_p2 * r + gm_n1 + gm_n2 * go_p2 * r + gm_n2 + go_b1 * go_n2 * r + go_b1 * go_p2 * r + go_b1 + go_n1 * go_n2 * r + go_n1 * go_p2 * r + go_n1 + go_n2 * go_p2 * r + go_n2))
    a[3] = 1.0 * gm_n1 * (1.0 * cgs_n1 * s / gm_n1 + 1.0) * (gb_n2 + gm_n2 + go_n2) / ((r * s ** 3 * (
                cgd_n2 + cgd_p2) * (
                                                                                                    cgd_b1 * cgd_n1 + cgd_b1 * cgs_n1 + cgd_n1 * cgs_n1 + cgd_n1 * cgs_n2 + cgs_n1 * cgs_n2) / (
                                                                                                    cgd_n1 * gb_n1 * go_n2 * r + cgd_n1 * gb_n1 * go_p2 * r + cgd_n1 * gb_n1 + cgd_n1 * gb_n2 * go_p2 * r + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 * go_n2 * r + cgd_n1 * gm_n1 * go_p2 * r + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 * go_p2 * r + cgd_n1 * gm_n2 + cgd_n1 * go_b1 * go_n2 * r + cgd_n1 * go_b1 * go_p2 * r + cgd_n1 * go_b1 + cgd_n1 * go_n1 * go_n2 * r + cgd_n1 * go_n1 * go_p2 * r + cgd_n1 * go_n1 + cgd_n1 * go_n2 * go_p2 * r + cgd_n1 * go_n2 + cgs_n1 * gb_n1 * go_n2 * r + cgs_n1 * gb_n1 * go_p2 * r + cgs_n1 * gb_n1 + cgs_n1 * gb_n2 * go_p2 * r + cgs_n1 * gb_n2 + cgs_n1 * gm_n2 * go_p2 * r + cgs_n1 * gm_n2 + cgs_n1 * go_b1 * go_n2 * r + cgs_n1 * go_b1 * go_p2 * r + cgs_n1 * go_b1 + cgs_n1 * go_n1 * go_n2 * r + cgs_n1 * go_n1 * go_p2 * r + cgs_n1 * go_n1 + cgs_n1 * go_n2 * go_p2 * r + cgs_n1 * go_n2) + s ** 2 * (
                                                                                                    cgd_b1 * cgd_n1 * go_n2 * r + cgd_b1 * cgd_n1 * go_p2 * r + cgd_b1 * cgd_n1 + cgd_b1 * cgs_n1 * go_n2 * r + cgd_b1 * cgs_n1 * go_p2 * r + cgd_b1 * cgs_n1 + cgd_n1 * cgd_n2 * gb_n1 * r + cgd_n1 * cgd_n2 * gb_n2 * r + cgd_n1 * cgd_n2 * gm_n1 * r + cgd_n1 * cgd_n2 * gm_n2 * r + cgd_n1 * cgd_n2 * go_b1 * r + cgd_n1 * cgd_n2 * go_n1 * r + cgd_n1 * cgd_n2 * go_n2 * r + cgd_n1 * cgd_p2 * gb_n1 * r + cgd_n1 * cgd_p2 * gb_n2 * r + cgd_n1 * cgd_p2 * gm_n1 * r + cgd_n1 * cgd_p2 * gm_n2 * r + cgd_n1 * cgd_p2 * go_b1 * r + cgd_n1 * cgd_p2 * go_n1 * r + cgd_n1 * cgd_p2 * go_n2 * r + cgd_n1 * cgs_n1 * go_n2 * r + cgd_n1 * cgs_n1 * go_p2 * r + cgd_n1 * cgs_n1 + cgd_n1 * cgs_n2 * go_n2 * r + cgd_n1 * cgs_n2 * go_p2 * r + cgd_n1 * cgs_n2 + cgd_n2 * cgs_n1 * gb_n1 * r + cgd_n2 * cgs_n1 * gb_n2 * r + cgd_n2 * cgs_n1 * gm_n2 * r + cgd_n2 * cgs_n1 * go_b1 * r + cgd_n2 * cgs_n1 * go_n1 * r + cgd_n2 * cgs_n1 * go_n2 * r + cgd_p2 * cgs_n1 * gb_n1 * r + cgd_p2 * cgs_n1 * gb_n2 * r + cgd_p2 * cgs_n1 * gm_n2 * r + cgd_p2 * cgs_n1 * go_b1 * r + cgd_p2 * cgs_n1 * go_n1 * r + cgd_p2 * cgs_n1 * go_n2 * r + cgs_n1 * cgs_n2 * go_n2 * r + cgs_n1 * cgs_n2 * go_p2 * r + cgs_n1 * cgs_n2) / (
                                                                                                    cgd_n1 * gb_n1 * go_n2 * r + cgd_n1 * gb_n1 * go_p2 * r + cgd_n1 * gb_n1 + cgd_n1 * gb_n2 * go_p2 * r + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 * go_n2 * r + cgd_n1 * gm_n1 * go_p2 * r + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 * go_p2 * r + cgd_n1 * gm_n2 + cgd_n1 * go_b1 * go_n2 * r + cgd_n1 * go_b1 * go_p2 * r + cgd_n1 * go_b1 + cgd_n1 * go_n1 * go_n2 * r + cgd_n1 * go_n1 * go_p2 * r + cgd_n1 * go_n1 + cgd_n1 * go_n2 * go_p2 * r + cgd_n1 * go_n2 + cgs_n1 * gb_n1 * go_n2 * r + cgs_n1 * gb_n1 * go_p2 * r + cgs_n1 * gb_n1 + cgs_n1 * gb_n2 * go_p2 * r + cgs_n1 * gb_n2 + cgs_n1 * gm_n2 * go_p2 * r + cgs_n1 * gm_n2 + cgs_n1 * go_b1 * go_n2 * r + cgs_n1 * go_b1 * go_p2 * r + cgs_n1 * go_b1 + cgs_n1 * go_n1 * go_n2 * r + cgs_n1 * go_n1 * go_p2 * r + cgs_n1 * go_n1 + cgs_n1 * go_n2 * go_p2 * r + cgs_n1 * go_n2) + s) * (
                                                                                                   cgd_n1 * gb_n1 * go_n2 * r + cgd_n1 * gb_n1 * go_p2 * r + cgd_n1 * gb_n1 + cgd_n1 * gb_n2 * go_p2 * r + cgd_n1 * gb_n2 + cgd_n1 * gm_n1 * go_n2 * r + cgd_n1 * gm_n1 * go_p2 * r + cgd_n1 * gm_n1 + cgd_n1 * gm_n2 * go_p2 * r + cgd_n1 * gm_n2 + cgd_n1 * go_b1 * go_n2 * r + cgd_n1 * go_b1 * go_p2 * r + cgd_n1 * go_b1 + cgd_n1 * go_n1 * go_n2 * r + cgd_n1 * go_n1 * go_p2 * r + cgd_n1 * go_n1 + cgd_n1 * go_n2 * go_p2 * r + cgd_n1 * go_n2 + cgs_n1 * gb_n1 * go_n2 * r + cgs_n1 * gb_n1 * go_p2 * r + cgs_n1 * gb_n1 + cgs_n1 * gb_n2 * go_p2 * r + cgs_n1 * gb_n2 + cgs_n1 * gm_n2 * go_p2 * r + cgs_n1 * gm_n2 + cgs_n1 * go_b1 * go_n2 * r + cgs_n1 * go_b1 * go_p2 * r + cgs_n1 * go_b1 + cgs_n1 * go_n1 * go_n2 * r + cgs_n1 * go_n1 * go_p2 * r + cgs_n1 * go_n1 + cgs_n1 * go_n2 * go_p2 * r + cgs_n1 * go_n2))
    return a


def gm_middle_neg_r_series(small_signal_param, r, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2 = gm
    go_n1, go_n2, go_p1, go_p2 = go
    gb_n1, gb_n2, gb_p1, gb_p2 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * gm_n2 * gm_p1 * (1.0 * cgd_n2 * cgd_p1 * s ** 2 / (gm_n2 * gm_p1) + s * (
                -1.0 * cgd_n2 / gm_n2 - 1.0 * cgd_p1 / gm_p1) + 1.0) / ((go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1) * (
                s ** 2 * (
                    cgd_n2 * cgd_p1 + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_p1 * cgd_p2 + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2) / (
                            (go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1)) + s * (
                            cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_n2 * go_p1 + cgd_n2 * go_p2 + cgd_p1 * go_n2 + cgd_p1 * go_p2 + cgd_p2 * gm_n1 + cgd_p2 * go_n1 + cgd_p2 * go_p1 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2) / (
                            (go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1)) + 1))
    a[1] = 1.0 * gm_n2 * gm_p1 * (1.0 * cgd_n2 * cgd_p1 * s ** 2 / (gm_n2 * gm_p1) + s * (
                -1.0 * cgd_n2 / gm_n2 - 1.0 * cgd_p1 / gm_p1) + 1.0) / ((go_n2 + go_p2) * (s ** 3 * (
                cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                                                       (
                                                                                                                   go_n2 + go_p2) * (
                                                                                                                   cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s ** 2 * (
                                                                                                       cgd_n2 * cgd_p1 * gm_n1 + cgd_n2 * cgd_p1 * gm_n2 + cgd_n2 * cgd_p1 * gm_p1 + cgd_n2 * cgd_p1 * go_n1 + cgd_n2 * cgd_p1 * go_n2 + cgd_n2 * cgd_p1 * go_p1 + cgd_n2 * cgd_p1 * go_p2 + cgd_n2 * cgs_p1 * gm_n1 + cgd_n2 * cgs_p1 * gm_n2 + cgd_n2 * cgs_p1 * go_n1 + cgd_n2 * cgs_p1 * go_n2 + cgd_n2 * cgs_p1 * go_p1 + cgd_n2 * cgs_p1 * go_p2 + cgd_p1 * cgd_p2 * gm_n1 + cgd_p1 * cgd_p2 * gm_p1 + cgd_p1 * cgd_p2 * go_n1 + cgd_p1 * cgd_p2 * go_p1 + cgd_p1 * cgs_n1 * go_n2 + cgd_p1 * cgs_n1 * go_p2 + cgd_p1 * cgs_n2 * go_n2 + cgd_p1 * cgs_n2 * go_p2 + cgd_p1 * cgs_p1 * go_n2 + cgd_p1 * cgs_p1 * go_p2 + cgd_p2 * cgs_p1 * gm_n1 + cgd_p2 * cgs_p1 * go_n1 + cgd_p2 * cgs_p1 * go_p1 + cgs_n1 * cgs_p1 * go_n2 + cgs_n1 * cgs_p1 * go_p2 + cgs_n2 * cgs_p1 * go_n2 + cgs_n2 * cgs_p1 * go_p2) / (
                                                                                                       (
                                                                                                                   go_n2 + go_p2) * (
                                                                                                                   cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s) * (
                                                                                    cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    a[2] = 1.0 * gm_n2 * gm_p1 * (1.0 * cgd_n2 * cgd_p1 * s ** 2 / (gm_n2 * gm_p1) + s * (
                -1.0 * cgd_n2 / gm_n2 - 1.0 * cgd_p1 / gm_p1) + 1.0) / (
                       (gm_n1 + go_n1 + go_p1) * (go_n2 * r + go_p2 * r + 1) * (r * s ** 2 * (
                           cgd_n2 * cgd_p1 + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_p1 * cgd_p2 + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2) / (
                                                                                            (gm_n1 + go_n1 + go_p1) * (
                                                                                                go_n2 * r + go_p2 * r + 1)) + s * (
                                                                                            cgd_n2 * gm_n1 * r + cgd_n2 * gm_n2 * r + cgd_n2 * go_n1 * r + cgd_n2 * go_n2 * r + cgd_n2 * go_p1 * r + cgd_n2 * go_p2 * r + cgd_n2 + cgd_p1 * go_n2 * r + cgd_p1 * go_p2 * r + cgd_p1 + cgd_p2 * gm_n1 * r + cgd_p2 * go_n1 * r + cgd_p2 * go_p1 * r + cgs_n1 * go_n2 * r + cgs_n1 * go_p2 * r + cgs_n1 + cgs_n2 * go_n2 * r + cgs_n2 * go_p2 * r + cgs_n2) / (
                                                                                            (gm_n1 + go_n1 + go_p1) * (
                                                                                                go_n2 * r + go_p2 * r + 1)) + 1))
    a[3] = 1.0 * gm_n2 * gm_p1 * (1.0 * cgd_n2 * cgd_p1 * s ** 2 / (gm_n2 * gm_p1) + s * (
                -1.0 * cgd_n2 / gm_n2 - 1.0 * cgd_p1 / gm_p1) + 1.0) / ((go_n2 * r + go_p2 * r + 1) * (r * s ** 3 * (
                cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                                                                   (
                                                                                                                               go_n2 * r + go_p2 * r + 1) * (
                                                                                                                               cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s ** 2 * (
                                                                                                                   cgd_n2 * cgd_p1 * gm_n1 * r + cgd_n2 * cgd_p1 * gm_n2 * r + cgd_n2 * cgd_p1 * gm_p1 * r + cgd_n2 * cgd_p1 * go_n1 * r + cgd_n2 * cgd_p1 * go_n2 * r + cgd_n2 * cgd_p1 * go_p1 * r + cgd_n2 * cgd_p1 * go_p2 * r + cgd_n2 * cgd_p1 + cgd_n2 * cgs_p1 * gm_n1 * r + cgd_n2 * cgs_p1 * gm_n2 * r + cgd_n2 * cgs_p1 * go_n1 * r + cgd_n2 * cgs_p1 * go_n2 * r + cgd_n2 * cgs_p1 * go_p1 * r + cgd_n2 * cgs_p1 * go_p2 * r + cgd_n2 * cgs_p1 + cgd_p1 * cgd_p2 * gm_n1 * r + cgd_p1 * cgd_p2 * gm_p1 * r + cgd_p1 * cgd_p2 * go_n1 * r + cgd_p1 * cgd_p2 * go_p1 * r + cgd_p1 * cgs_n1 * go_n2 * r + cgd_p1 * cgs_n1 * go_p2 * r + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 * go_n2 * r + cgd_p1 * cgs_n2 * go_p2 * r + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 * go_n2 * r + cgd_p1 * cgs_p1 * go_p2 * r + cgd_p1 * cgs_p1 + cgd_p2 * cgs_p1 * gm_n1 * r + cgd_p2 * cgs_p1 * go_n1 * r + cgd_p2 * cgs_p1 * go_p1 * r + cgs_n1 * cgs_p1 * go_n2 * r + cgs_n1 * cgs_p1 * go_p2 * r + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1 * go_n2 * r + cgs_n2 * cgs_p1 * go_p2 * r + cgs_n2 * cgs_p1) / (
                                                                                                                   (
                                                                                                                               go_n2 * r + go_p2 * r + 1) * (
                                                                                                                               cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s) * (
                                                                                    cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    return a


def gm_diff_neg_c_series(small_signal_param, c, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2, gm_b1 = gm
    go_n1, go_n2, go_p1, go_p2, go_b1 = go
    gb_n1, gb_n2, gb_p1, gb_p2, gb_b1 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2, cgs_b1 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * gm_n1 * (1.0 * cgs_n1 * s / gm_n1 + 1.0) * (gb_n2 + gm_n2 + go_n2) / ((s ** 2 * (cgd_n2 + cgd_p2) * (
                cgd_b1 + cgs_n1 + cgs_n2) / (
                                                                                                    gb_n1 * go_n2 + gb_n1 * go_p2 + gb_n2 * go_p2 + gm_n1 * go_n2 + gm_n1 * go_p2 + gm_n2 * go_p2 + go_b1 * go_n2 + go_b1 * go_p2 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p2) + s * (
                                                                                                    cgd_b1 * go_n2 + cgd_b1 * go_p2 + cgd_n2 * gb_n1 + cgd_n2 * gb_n2 + cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * go_b1 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_p2 * gb_n1 + cgd_p2 * gb_n2 + cgd_p2 * gm_n1 + cgd_p2 * gm_n2 + cgd_p2 * go_b1 + cgd_p2 * go_n1 + cgd_p2 * go_n2 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2) / (
                                                                                                    gb_n1 * go_n2 + gb_n1 * go_p2 + gb_n2 * go_p2 + gm_n1 * go_n2 + gm_n1 * go_p2 + gm_n2 * go_p2 + go_b1 * go_n2 + go_b1 * go_p2 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p2) + 1) * (
                                                                                                   gb_n1 * go_n2 + gb_n1 * go_p2 + gb_n2 * go_p2 + gm_n1 * go_n2 + gm_n1 * go_p2 + gm_n2 * go_p2 + go_b1 * go_n2 + go_b1 * go_p2 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p2))
    a[1] = 1.0 * gm_n1 * (1.0 * cgs_n1 * s / gm_n1 + 1.0) * (gb_n2 + gm_n2 + go_n2) / ((s ** 3 * (cgd_n2 + cgd_p2) * (
                cgd_b1 * cgd_n1 + cgd_b1 * cgs_n1 + cgd_n1 * cgs_n1 + cgd_n1 * cgs_n2 + cgs_n1 * cgs_n2) / (
                                                                                                    cgd_n1 * gb_n1 * go_n2 + cgd_n1 * gb_n1 * go_p2 + cgd_n1 * gb_n2 * go_p2 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p2 + cgd_n1 * gm_n2 * go_p2 + cgd_n1 * go_b1 * go_n2 + cgd_n1 * go_b1 * go_p2 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p2 + cgd_n1 * go_n2 * go_p2 + cgs_n1 * gb_n1 * go_n2 + cgs_n1 * gb_n1 * go_p2 + cgs_n1 * gb_n2 * go_p2 + cgs_n1 * gm_n2 * go_p2 + cgs_n1 * go_b1 * go_n2 + cgs_n1 * go_b1 * go_p2 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p2 + cgs_n1 * go_n2 * go_p2) + s ** 2 * (
                                                                                                    cgd_b1 * cgd_n1 * go_n2 + cgd_b1 * cgd_n1 * go_p2 + cgd_b1 * cgs_n1 * go_n2 + cgd_b1 * cgs_n1 * go_p2 + cgd_n1 * cgd_n2 * gb_n1 + cgd_n1 * cgd_n2 * gb_n2 + cgd_n1 * cgd_n2 * gm_n1 + cgd_n1 * cgd_n2 * gm_n2 + cgd_n1 * cgd_n2 * go_b1 + cgd_n1 * cgd_n2 * go_n1 + cgd_n1 * cgd_n2 * go_n2 + cgd_n1 * cgd_p2 * gb_n1 + cgd_n1 * cgd_p2 * gb_n2 + cgd_n1 * cgd_p2 * gm_n1 + cgd_n1 * cgd_p2 * gm_n2 + cgd_n1 * cgd_p2 * go_b1 + cgd_n1 * cgd_p2 * go_n1 + cgd_n1 * cgd_p2 * go_n2 + cgd_n1 * cgs_n1 * go_n2 + cgd_n1 * cgs_n1 * go_p2 + cgd_n1 * cgs_n2 * go_n2 + cgd_n1 * cgs_n2 * go_p2 + cgd_n2 * cgs_n1 * gb_n1 + cgd_n2 * cgs_n1 * gb_n2 + cgd_n2 * cgs_n1 * gm_n2 + cgd_n2 * cgs_n1 * go_b1 + cgd_n2 * cgs_n1 * go_n1 + cgd_n2 * cgs_n1 * go_n2 + cgd_p2 * cgs_n1 * gb_n1 + cgd_p2 * cgs_n1 * gb_n2 + cgd_p2 * cgs_n1 * gm_n2 + cgd_p2 * cgs_n1 * go_b1 + cgd_p2 * cgs_n1 * go_n1 + cgd_p2 * cgs_n1 * go_n2 + cgs_n1 * cgs_n2 * go_n2 + cgs_n1 * cgs_n2 * go_p2) / (
                                                                                                    cgd_n1 * gb_n1 * go_n2 + cgd_n1 * gb_n1 * go_p2 + cgd_n1 * gb_n2 * go_p2 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p2 + cgd_n1 * gm_n2 * go_p2 + cgd_n1 * go_b1 * go_n2 + cgd_n1 * go_b1 * go_p2 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p2 + cgd_n1 * go_n2 * go_p2 + cgs_n1 * gb_n1 * go_n2 + cgs_n1 * gb_n1 * go_p2 + cgs_n1 * gb_n2 * go_p2 + cgs_n1 * gm_n2 * go_p2 + cgs_n1 * go_b1 * go_n2 + cgs_n1 * go_b1 * go_p2 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p2 + cgs_n1 * go_n2 * go_p2) + s) * (
                                                                                                   cgd_n1 * gb_n1 * go_n2 + cgd_n1 * gb_n1 * go_p2 + cgd_n1 * gb_n2 * go_p2 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p2 + cgd_n1 * gm_n2 * go_p2 + cgd_n1 * go_b1 * go_n2 + cgd_n1 * go_b1 * go_p2 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p2 + cgd_n1 * go_n2 * go_p2 + cgs_n1 * gb_n1 * go_n2 + cgs_n1 * gb_n1 * go_p2 + cgs_n1 * gb_n2 * go_p2 + cgs_n1 * gm_n2 * go_p2 + cgs_n1 * go_b1 * go_n2 + cgs_n1 * go_b1 * go_p2 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p2 + cgs_n1 * go_n2 * go_p2))
    a[2] = 1.0 * c * gm_n1 * (1.0 * cgs_n1 * s ** 2 / gm_n1 + 1.0 * s) * (gb_n2 + gm_n2 + go_n2) / ((s ** 2 * (
                c + cgd_n2 + cgd_p2) * (cgd_b1 + cgs_n1 + cgs_n2) / (
                                                                                                                 gb_n1 * go_n2 + gb_n1 * go_p2 + gb_n2 * go_p2 + gm_n1 * go_n2 + gm_n1 * go_p2 + gm_n2 * go_p2 + go_b1 * go_n2 + go_b1 * go_p2 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p2) + s * (
                                                                                                                 c * gb_n1 + c * gb_n2 + c * gm_n1 + c * gm_n2 + c * go_b1 + c * go_n1 + c * go_n2 + cgd_b1 * go_n2 + cgd_b1 * go_p2 + cgd_n2 * gb_n1 + cgd_n2 * gb_n2 + cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * go_b1 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_p2 * gb_n1 + cgd_p2 * gb_n2 + cgd_p2 * gm_n1 + cgd_p2 * gm_n2 + cgd_p2 * go_b1 + cgd_p2 * go_n1 + cgd_p2 * go_n2 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2) / (
                                                                                                                 gb_n1 * go_n2 + gb_n1 * go_p2 + gb_n2 * go_p2 + gm_n1 * go_n2 + gm_n1 * go_p2 + gm_n2 * go_p2 + go_b1 * go_n2 + go_b1 * go_p2 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p2) + 1) * (
                                                                                                                gb_n1 * go_n2 + gb_n1 * go_p2 + gb_n2 * go_p2 + gm_n1 * go_n2 + gm_n1 * go_p2 + gm_n2 * go_p2 + go_b1 * go_n2 + go_b1 * go_p2 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p2))
    a[3] = 1.0 * c * gm_n1 * (1.0 * cgs_n1 * s / gm_n1 + 1.0) * (gb_n2 + gm_n2 + go_n2) / ((s ** 2 * (
                c + cgd_n2 + cgd_p2) * (
                                                                                                        cgd_b1 * cgd_n1 + cgd_b1 * cgs_n1 + cgd_n1 * cgs_n1 + cgd_n1 * cgs_n2 + cgs_n1 * cgs_n2) / (
                                                                                                        cgd_n1 * gb_n1 * go_n2 + cgd_n1 * gb_n1 * go_p2 + cgd_n1 * gb_n2 * go_p2 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p2 + cgd_n1 * gm_n2 * go_p2 + cgd_n1 * go_b1 * go_n2 + cgd_n1 * go_b1 * go_p2 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p2 + cgd_n1 * go_n2 * go_p2 + cgs_n1 * gb_n1 * go_n2 + cgs_n1 * gb_n1 * go_p2 + cgs_n1 * gb_n2 * go_p2 + cgs_n1 * gm_n2 * go_p2 + cgs_n1 * go_b1 * go_n2 + cgs_n1 * go_b1 * go_p2 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p2 + cgs_n1 * go_n2 * go_p2) + s * (
                                                                                                        c * cgd_n1 * gb_n1 + c * cgd_n1 * gb_n2 + c * cgd_n1 * gm_n1 + c * cgd_n1 * gm_n2 + c * cgd_n1 * go_b1 + c * cgd_n1 * go_n1 + c * cgd_n1 * go_n2 + c * cgs_n1 * gb_n1 + c * cgs_n1 * gb_n2 + c * cgs_n1 * gm_n2 + c * cgs_n1 * go_b1 + c * cgs_n1 * go_n1 + c * cgs_n1 * go_n2 + cgd_b1 * cgd_n1 * go_n2 + cgd_b1 * cgd_n1 * go_p2 + cgd_b1 * cgs_n1 * go_n2 + cgd_b1 * cgs_n1 * go_p2 + cgd_n1 * cgd_n2 * gb_n1 + cgd_n1 * cgd_n2 * gb_n2 + cgd_n1 * cgd_n2 * gm_n1 + cgd_n1 * cgd_n2 * gm_n2 + cgd_n1 * cgd_n2 * go_b1 + cgd_n1 * cgd_n2 * go_n1 + cgd_n1 * cgd_n2 * go_n2 + cgd_n1 * cgd_p2 * gb_n1 + cgd_n1 * cgd_p2 * gb_n2 + cgd_n1 * cgd_p2 * gm_n1 + cgd_n1 * cgd_p2 * gm_n2 + cgd_n1 * cgd_p2 * go_b1 + cgd_n1 * cgd_p2 * go_n1 + cgd_n1 * cgd_p2 * go_n2 + cgd_n1 * cgs_n1 * go_n2 + cgd_n1 * cgs_n1 * go_p2 + cgd_n1 * cgs_n2 * go_n2 + cgd_n1 * cgs_n2 * go_p2 + cgd_n2 * cgs_n1 * gb_n1 + cgd_n2 * cgs_n1 * gb_n2 + cgd_n2 * cgs_n1 * gm_n2 + cgd_n2 * cgs_n1 * go_b1 + cgd_n2 * cgs_n1 * go_n1 + cgd_n2 * cgs_n1 * go_n2 + cgd_p2 * cgs_n1 * gb_n1 + cgd_p2 * cgs_n1 * gb_n2 + cgd_p2 * cgs_n1 * gm_n2 + cgd_p2 * cgs_n1 * go_b1 + cgd_p2 * cgs_n1 * go_n1 + cgd_p2 * cgs_n1 * go_n2 + cgs_n1 * cgs_n2 * go_n2 + cgs_n1 * cgs_n2 * go_p2) / (
                                                                                                        cgd_n1 * gb_n1 * go_n2 + cgd_n1 * gb_n1 * go_p2 + cgd_n1 * gb_n2 * go_p2 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p2 + cgd_n1 * gm_n2 * go_p2 + cgd_n1 * go_b1 * go_n2 + cgd_n1 * go_b1 * go_p2 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p2 + cgd_n1 * go_n2 * go_p2 + cgs_n1 * gb_n1 * go_n2 + cgs_n1 * gb_n1 * go_p2 + cgs_n1 * gb_n2 * go_p2 + cgs_n1 * gm_n2 * go_p2 + cgs_n1 * go_b1 * go_n2 + cgs_n1 * go_b1 * go_p2 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p2 + cgs_n1 * go_n2 * go_p2) + 1) * (
                                                                                                       cgd_n1 * gb_n1 * go_n2 + cgd_n1 * gb_n1 * go_p2 + cgd_n1 * gb_n2 * go_p2 + cgd_n1 * gm_n1 * go_n2 + cgd_n1 * gm_n1 * go_p2 + cgd_n1 * gm_n2 * go_p2 + cgd_n1 * go_b1 * go_n2 + cgd_n1 * go_b1 * go_p2 + cgd_n1 * go_n1 * go_n2 + cgd_n1 * go_n1 * go_p2 + cgd_n1 * go_n2 * go_p2 + cgs_n1 * gb_n1 * go_n2 + cgs_n1 * gb_n1 * go_p2 + cgs_n1 * gb_n2 * go_p2 + cgs_n1 * gm_n2 * go_p2 + cgs_n1 * go_b1 * go_n2 + cgs_n1 * go_b1 * go_p2 + cgs_n1 * go_n1 * go_n2 + cgs_n1 * go_n1 * go_p2 + cgs_n1 * go_n2 * go_p2))
    return a


def gm_middle_neg_c_series(small_signal_param, c, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2 = gm
    go_n1, go_n2, go_p1, go_p2 = go
    gb_n1, gb_n2, gb_p1, gb_p2 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * gm_n2 * gm_p1 * (1.0 * cgd_n2 * cgd_p1 * s ** 2 / (gm_n2 * gm_p1) + s * (
                -1.0 * cgd_n2 / gm_n2 - 1.0 * cgd_p1 / gm_p1) + 1.0) / ((go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1) * (
                s ** 2 * (
                    cgd_n2 * cgd_p1 + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_p1 * cgd_p2 + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2) / (
                            (go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1)) + s * (
                            cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_n2 * go_p1 + cgd_n2 * go_p2 + cgd_p1 * go_n2 + cgd_p1 * go_p2 + cgd_p2 * gm_n1 + cgd_p2 * go_n1 + cgd_p2 * go_p1 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2) / (
                            (go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1)) + 1))
    a[1] = 1.0 * gm_n2 * gm_p1 * (1.0 * cgd_n2 * cgd_p1 * s ** 2 / (gm_n2 * gm_p1) + s * (
                -1.0 * cgd_n2 / gm_n2 - 1.0 * cgd_p1 / gm_p1) + 1.0) / ((go_n2 + go_p2) * (s ** 3 * (
                cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                                                       (
                                                                                                                   go_n2 + go_p2) * (
                                                                                                                   cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s ** 2 * (
                                                                                                       cgd_n2 * cgd_p1 * gm_n1 + cgd_n2 * cgd_p1 * gm_n2 + cgd_n2 * cgd_p1 * gm_p1 + cgd_n2 * cgd_p1 * go_n1 + cgd_n2 * cgd_p1 * go_n2 + cgd_n2 * cgd_p1 * go_p1 + cgd_n2 * cgd_p1 * go_p2 + cgd_n2 * cgs_p1 * gm_n1 + cgd_n2 * cgs_p1 * gm_n2 + cgd_n2 * cgs_p1 * go_n1 + cgd_n2 * cgs_p1 * go_n2 + cgd_n2 * cgs_p1 * go_p1 + cgd_n2 * cgs_p1 * go_p2 + cgd_p1 * cgd_p2 * gm_n1 + cgd_p1 * cgd_p2 * gm_p1 + cgd_p1 * cgd_p2 * go_n1 + cgd_p1 * cgd_p2 * go_p1 + cgd_p1 * cgs_n1 * go_n2 + cgd_p1 * cgs_n1 * go_p2 + cgd_p1 * cgs_n2 * go_n2 + cgd_p1 * cgs_n2 * go_p2 + cgd_p1 * cgs_p1 * go_n2 + cgd_p1 * cgs_p1 * go_p2 + cgd_p2 * cgs_p1 * gm_n1 + cgd_p2 * cgs_p1 * go_n1 + cgd_p2 * cgs_p1 * go_p1 + cgs_n1 * cgs_p1 * go_n2 + cgs_n1 * cgs_p1 * go_p2 + cgs_n2 * cgs_p1 * go_n2 + cgs_n2 * cgs_p1 * go_p2) / (
                                                                                                       (
                                                                                                                   go_n2 + go_p2) * (
                                                                                                                   cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s) * (
                                                                                    cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    a[2] = 1.0 * c * gm_n2 * gm_p1 * (1.0 * cgd_n2 * cgd_p1 * s ** 3 / (gm_n2 * gm_p1) + s ** 2 * (
                -1.0 * cgd_n2 / gm_n2 - 1.0 * cgd_p1 / gm_p1) + 1.0 * s) / (
                       (go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1) * (s ** 2 * (
                           c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1 + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_p1 * cgd_p2 + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2) / (
                                                                                (go_n2 + go_p2) * (
                                                                                    gm_n1 + go_n1 + go_p1)) + s * (
                                                                                c * gm_n1 + c * go_n1 + c * go_p1 + cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_n2 * go_p1 + cgd_n2 * go_p2 + cgd_p1 * go_n2 + cgd_p1 * go_p2 + cgd_p2 * gm_n1 + cgd_p2 * go_n1 + cgd_p2 * go_p1 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2) / (
                                                                                (go_n2 + go_p2) * (
                                                                                    gm_n1 + go_n1 + go_p1)) + 1))
    a[3] = 1.0 * c * gm_n2 * gm_p1 * (1.0 * cgd_n2 * cgd_p1 * s ** 2 / (gm_n2 * gm_p1) + s * (
                -1.0 * cgd_n2 / gm_n2 - 1.0 * cgd_p1 / gm_p1) + 1.0) / ((go_n2 + go_p2) * (s ** 2 * (
                c * cgd_n2 * cgd_p1 + c * cgd_n2 * cgs_p1 + c * cgd_p1 * cgs_n1 + c * cgd_p1 * cgs_n2 + c * cgd_p1 * cgs_p1 + c * cgs_n1 * cgs_p1 + c * cgs_n2 * cgs_p1 + cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                                                       (
                                                                                                                   go_n2 + go_p2) * (
                                                                                                                   cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s * (
                                                                                                       c * cgd_p1 * gm_n1 + c * cgd_p1 * gm_p1 + c * cgd_p1 * go_n1 + c * cgd_p1 * go_p1 + c * cgs_p1 * gm_n1 + c * cgs_p1 * go_n1 + c * cgs_p1 * go_p1 + cgd_n2 * cgd_p1 * gm_n1 + cgd_n2 * cgd_p1 * gm_n2 + cgd_n2 * cgd_p1 * gm_p1 + cgd_n2 * cgd_p1 * go_n1 + cgd_n2 * cgd_p1 * go_n2 + cgd_n2 * cgd_p1 * go_p1 + cgd_n2 * cgd_p1 * go_p2 + cgd_n2 * cgs_p1 * gm_n1 + cgd_n2 * cgs_p1 * gm_n2 + cgd_n2 * cgs_p1 * go_n1 + cgd_n2 * cgs_p1 * go_n2 + cgd_n2 * cgs_p1 * go_p1 + cgd_n2 * cgs_p1 * go_p2 + cgd_p1 * cgd_p2 * gm_n1 + cgd_p1 * cgd_p2 * gm_p1 + cgd_p1 * cgd_p2 * go_n1 + cgd_p1 * cgd_p2 * go_p1 + cgd_p1 * cgs_n1 * go_n2 + cgd_p1 * cgs_n1 * go_p2 + cgd_p1 * cgs_n2 * go_n2 + cgd_p1 * cgs_n2 * go_p2 + cgd_p1 * cgs_p1 * go_n2 + cgd_p1 * cgs_p1 * go_p2 + cgd_p2 * cgs_p1 * gm_n1 + cgd_p2 * cgs_p1 * go_n1 + cgd_p2 * cgs_p1 * go_p1 + cgs_n1 * cgs_p1 * go_n2 + cgs_n1 * cgs_p1 * go_p2 + cgs_n2 * cgs_p1 * go_n2 + cgs_n2 * cgs_p1 * go_p2) / (
                                                                                                       (
                                                                                                                   go_n2 + go_p2) * (
                                                                                                                   cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + 1) * (
                                                                                    cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    return a


def gm_middle_pos_r_parallel(small_signal_param, r, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_p1, gm_b1 = gm
    go_p1, go_b1 = go
    gb_p1, gb_p1 = gb
    cgs_p1, cgs_b1 = cgs
    cgd_p1, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = -1.0 * (gm_p1 * r - 1) * (-1.0 * cgd_p1 * r * s / (gm_p1 * r - 1) + 1.0) / (
                (r * s * (cgd_b1 + cgd_p1) / (go_b1 * r + go_p1 * r + 1) + 1) * (go_b1 * r + go_p1 * r + 1))
    a[1] = -1.0 * (gm_p1 * r - 1) * (-1.0 * cgd_p1 * r * s / (gm_p1 * r - 1) + 1.0) / ((gm_p1 + go_b1 + go_p1) * (
                r * s ** 2 * (cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (gm_p1 + go_b1 + go_p1) + s * (
                    cgd_b1 + cgd_p1 * gm_p1 * r + cgd_p1 * go_b1 * r + cgd_p1 * go_p1 * r + cgs_p1 * go_b1 * r + cgs_p1 * go_p1 * r + cgs_p1) / (
                            gm_p1 + go_b1 + go_p1) + 1))
    a[2] = -1.0 * (gm_p1 * r - 1) * (-1.0 * cgd_p1 * r * s / (gm_p1 * r - 1) + 1.0) / r
    a[3] = -1.0 * (gm_p1 * r - 1) * (-1.0 * cgd_p1 * r * s / (gm_p1 * r - 1) + 1.0) / (r * s * (cgd_p1 + cgs_p1) + 1)
    return a


def gm_middle_pos_c_parallel(small_signal_param, c, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_p1, gm_b1 = gm
    go_p1, go_b1 = go
    gb_p1, gb_p1 = gb
    cgs_p1, cgs_b1 = cgs
    cgd_p1, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = -1.0 * gm_p1 * (1.0 - s * (1.0 * c + 1.0 * cgd_p1) / gm_p1) / (
                (go_b1 + go_p1) * (s * (c + cgd_b1 + cgd_p1) / (go_b1 + go_p1) + 1))
    a[1] = -1.0 * gm_p1 * (1.0 - s * (1.0 * c + 1.0 * cgd_p1) / gm_p1) / ((s ** 2 * (
                c * cgd_b1 + c * cgs_p1 + cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (
                                                                                       c * gm_p1 + c * go_b1 + c * go_p1 + cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1) + s) * (
                                                                                      c * gm_p1 + c * go_b1 + c * go_p1 + cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1))
    a[2] = -1.0 * gm_p1 * (1.0 - s * (1.0 * c + 1.0 * cgd_p1) / gm_p1)
    a[3] = -1.0 * gm_p1 * (1.0 - s * (1.0 * c + 1.0 * cgd_p1) / gm_p1) / (s * (c + cgd_p1 + cgs_p1))
    return a


def gm_middle_neg_r_parallel(small_signal_param, r, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2 = gm
    go_n1, go_n2, go_p1, go_p2 = go
    gb_n1, gb_n2, gb_p1, gb_p2 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * (1.0 * cgd_n2 * cgd_p1 * r * s ** 2 / (gm_n1 + gm_n2 * gm_p1 * r + go_n1 + go_p1) + 1.0 * s * (
                -cgd_n2 * gm_p1 * r + cgd_n2 - cgd_p1 * gm_n2 * r + cgd_p1 + cgs_n1 + cgs_n2) / (
                              gm_n1 + gm_n2 * gm_p1 * r + go_n1 + go_p1) + 1.0) * (
                       gm_n1 + gm_n2 * gm_p1 * r + go_n1 + go_p1) / (
                       (gm_n1 + go_n1 + go_p1) * (go_n2 * r + go_p2 * r + 1) * (r * s ** 2 * (
                           cgd_n2 * cgd_p1 + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_p1 * cgd_p2 + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2) / (
                                                                                            (gm_n1 + go_n1 + go_p1) * (
                                                                                                go_n2 * r + go_p2 * r + 1)) + s * (
                                                                                            cgd_n2 * gm_n1 * r + cgd_n2 * gm_n2 * r + cgd_n2 * go_n1 * r + cgd_n2 * go_n2 * r + cgd_n2 * go_p1 * r + cgd_n2 * go_p2 * r + cgd_n2 + cgd_p1 * go_n2 * r + cgd_p1 * go_p2 * r + cgd_p1 + cgd_p2 * gm_n1 * r + cgd_p2 * go_n1 * r + cgd_p2 * go_p1 * r + cgs_n1 * go_n2 * r + cgs_n1 * go_p2 * r + cgs_n1 + cgs_n2 * go_n2 * r + cgs_n2 * go_p2 * r + cgs_n2) / (
                                                                                            (gm_n1 + go_n1 + go_p1) * (
                                                                                                go_n2 * r + go_p2 * r + 1)) + 1))
    a[1] = 1.0 * (1.0 * cgd_n2 * cgd_p1 * r * s ** 2 / (gm_n1 + gm_n2 * gm_p1 * r + go_n1 + go_p1) + 1.0 * s * (
                -cgd_n2 * gm_p1 * r + cgd_n2 - cgd_p1 * gm_n2 * r + cgd_p1 + cgs_n1 + cgs_n2) / (
                              gm_n1 + gm_n2 * gm_p1 * r + go_n1 + go_p1) + 1.0) * (
                       gm_n1 + gm_n2 * gm_p1 * r + go_n1 + go_p1) / ((r * s ** 3 * (
                cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                                  gm_n1 * go_n2 + gm_n1 * go_p2 - gm_n2 * gm_p1 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p1 + go_p1 * go_p2) + s ** 2 * (
                                                                                  cgd_n2 * cgd_p1 * gm_n1 * r + cgd_n2 * cgd_p1 * gm_n2 * r + cgd_n2 * cgd_p1 * gm_p1 * r + cgd_n2 * cgd_p1 * go_n1 * r + cgd_n2 * cgd_p1 * go_n2 * r + cgd_n2 * cgd_p1 * go_p1 * r + cgd_n2 * cgd_p1 * go_p2 * r + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_n2 * cgs_p1 * gm_n1 * r + cgd_n2 * cgs_p1 * gm_n2 * r + cgd_n2 * cgs_p1 * go_n1 * r + cgd_n2 * cgs_p1 * go_n2 * r + cgd_n2 * cgs_p1 * go_p1 * r + cgd_n2 * cgs_p1 * go_p2 * r + cgd_n2 * cgs_p1 + cgd_p1 * cgd_p2 * gm_n1 * r + cgd_p1 * cgd_p2 * gm_p1 * r + cgd_p1 * cgd_p2 * go_n1 * r + cgd_p1 * cgd_p2 * go_p1 * r + cgd_p1 * cgd_p2 + cgd_p1 * cgs_n1 * go_n2 * r + cgd_p1 * cgs_n1 * go_p2 * r + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 * go_n2 * r + cgd_p1 * cgs_n2 * go_p2 * r + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 * go_n2 * r + cgd_p1 * cgs_p1 * go_p2 * r + cgd_p1 * cgs_p1 + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2 + cgd_p2 * cgs_p1 * gm_n1 * r + cgd_p2 * cgs_p1 * go_n1 * r + cgd_p2 * cgs_p1 * go_p1 * r + cgs_n1 * cgs_p1 * go_n2 * r + cgs_n1 * cgs_p1 * go_p2 * r + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1 * go_n2 * r + cgs_n2 * cgs_p1 * go_p2 * r + cgs_n2 * cgs_p1) / (
                                                                                  gm_n1 * go_n2 + gm_n1 * go_p2 - gm_n2 * gm_p1 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p1 + go_p1 * go_p2) + s * (
                                                                                  cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * gm_p1 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_n2 * go_p1 + cgd_n2 * go_p2 + cgd_p1 * gm_n1 * go_n2 * r + cgd_p1 * gm_n1 * go_p2 * r + cgd_p1 * gm_n1 + cgd_p1 * gm_n2 + cgd_p1 * gm_p1 * go_n2 * r + cgd_p1 * gm_p1 * go_p2 * r + cgd_p1 * gm_p1 + cgd_p1 * go_n1 * go_n2 * r + cgd_p1 * go_n1 * go_p2 * r + cgd_p1 * go_n1 + cgd_p1 * go_n2 * go_p1 * r + cgd_p1 * go_n2 + cgd_p1 * go_p1 * go_p2 * r + cgd_p1 * go_p1 + cgd_p1 * go_p2 + cgd_p2 * gm_n1 + cgd_p2 * go_n1 + cgd_p2 * go_p1 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2 + cgs_p1 * gm_n1 * go_n2 * r + cgs_p1 * gm_n1 * go_p2 * r + cgs_p1 * gm_n1 + cgs_p1 * go_n1 * go_n2 * r + cgs_p1 * go_n1 * go_p2 * r + cgs_p1 * go_n1 + cgs_p1 * go_n2 * go_p1 * r + cgs_p1 * go_p1 * go_p2 * r + cgs_p1 * go_p1) / (
                                                                                  gm_n1 * go_n2 + gm_n1 * go_p2 - gm_n2 * gm_p1 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p1 + go_p1 * go_p2) + 1) * (
                                                                                 gm_n1 * go_n2 + gm_n1 * go_p2 - gm_n2 * gm_p1 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p1 + go_p1 * go_p2))
    a[2] = 1.0 * (1.0 * cgd_n2 * cgd_p1 * r * s ** 2 / (gm_n1 + gm_n2 * gm_p1 * r + go_n1 + go_p1) + 1.0 * s * (
                -cgd_n2 * gm_p1 * r + cgd_n2 - cgd_p1 * gm_n2 * r + cgd_p1 + cgs_n1 + cgs_n2) / (
                              gm_n1 + gm_n2 * gm_p1 * r + go_n1 + go_p1) + 1.0) * (
                       gm_n1 + gm_n2 * gm_p1 * r + go_n1 + go_p1) / (
                       r * (1.0 * s * (cgd_n2 + cgd_p1 + cgs_n1 + cgs_n2) / (gm_n1 + go_n1 + go_p1) + 1.0) * (
                           gm_n1 + go_n1 + go_p1))
    a[3] = 1.0 * (1.0 * cgd_n2 * cgd_p1 * r * s ** 2 / (gm_n1 + gm_n2 * gm_p1 * r + go_n1 + go_p1) + 1.0 * s * (
                -cgd_n2 * gm_p1 * r + cgd_n2 - cgd_p1 * gm_n2 * r + cgd_p1 + cgs_n1 + cgs_n2) / (
                              gm_n1 + gm_n2 * gm_p1 * r + go_n1 + go_p1) + 1.0) * (
                       gm_n1 + gm_n2 * gm_p1 * r + go_n1 + go_p1) / ((gm_n1 + go_n1 + go_p1) * (r * s ** 2 * (
                cgd_n2 * cgd_p1 + cgd_n2 * cgs_p1 + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1) / (
                                                                                                            gm_n1 + go_n1 + go_p1) + s * (
                                                                                                            cgd_n2 + cgd_p1 * gm_n1 * r + cgd_p1 * gm_p1 * r + cgd_p1 * go_n1 * r + cgd_p1 * go_p1 * r + cgd_p1 + cgs_n1 + cgs_n2 + cgs_p1 * gm_n1 * r + cgs_p1 * go_n1 * r + cgs_p1 * go_p1 * r) / (
                                                                                                            gm_n1 + go_n1 + go_p1) + 1))
    return a


def gm_middle_neg_c_parallel(small_signal_param, c, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2 = gm
    go_n1, go_n2, go_p1, go_p2 = go
    gb_n1, gb_n2, gb_p1, gb_p2 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * gm_n2 * gm_p1 * (
                1.0 + 1.0 * s ** 2 * (c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1) / (
                    gm_n2 * gm_p1) + 1.0 * s * (c * gm_n1 + c * go_n1 + c * go_p1 - cgd_n2 * gm_p1 - cgd_p1 * gm_n2) / (
                            gm_n2 * gm_p1)) / ((go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1) * (s ** 2 * (
                c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1 + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_p1 * cgd_p2 + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2) / (
                                                                                                        (
                                                                                                                    go_n2 + go_p2) * (
                                                                                                                    gm_n1 + go_n1 + go_p1)) + s * (
                                                                                                        c * gm_n1 + c * go_n1 + c * go_p1 + cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_n2 * go_p1 + cgd_n2 * go_p2 + cgd_p1 * go_n2 + cgd_p1 * go_p2 + cgd_p2 * gm_n1 + cgd_p2 * go_n1 + cgd_p2 * go_p1 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2) / (
                                                                                                        (
                                                                                                                    go_n2 + go_p2) * (
                                                                                                                    gm_n1 + go_n1 + go_p1)) + 1))
    a[1] = 1.0 * gm_n2 * gm_p1 * (
                1.0 + 1.0 * s ** 2 * (c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1) / (
                    gm_n2 * gm_p1) + 1.0 * s * (c * gm_n1 + c * go_n1 + c * go_p1 - cgd_n2 * gm_p1 - cgd_p1 * gm_n2) / (
                            gm_n2 * gm_p1)) / ((s ** 3 * (
                c * cgd_n2 * cgd_p2 + c * cgd_n2 * cgs_n1 + c * cgd_n2 * cgs_n2 + c * cgd_n2 * cgs_p1 + c * cgd_p1 * cgd_p2 + c * cgd_p1 * cgs_n1 + c * cgd_p1 * cgs_n2 + c * cgd_p1 * cgs_p1 + c * cgd_p2 * cgs_n1 + c * cgd_p2 * cgs_n2 + c * cgs_n1 * cgs_p1 + c * cgs_n2 * cgs_p1 + cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                            c * gm_n1 * go_n2 + c * gm_n1 * go_p2 - c * gm_n2 * gm_p1 + c * go_n1 * go_n2 + c * go_n1 * go_p2 + c * go_n2 * go_p1 + c * go_p1 * go_p2 + cgd_p1 * gm_n1 * go_n2 + cgd_p1 * gm_n1 * go_p2 + cgd_p1 * gm_p1 * go_n2 + cgd_p1 * gm_p1 * go_p2 + cgd_p1 * go_n1 * go_n2 + cgd_p1 * go_n1 * go_p2 + cgd_p1 * go_n2 * go_p1 + cgd_p1 * go_p1 * go_p2 + cgs_p1 * gm_n1 * go_n2 + cgs_p1 * gm_n1 * go_p2 + cgs_p1 * go_n1 * go_n2 + cgs_p1 * go_n1 * go_p2 + cgs_p1 * go_n2 * go_p1 + cgs_p1 * go_p1 * go_p2) + s ** 2 * (
                                                            c * cgd_n2 * gm_n1 + c * cgd_n2 * gm_n2 + c * cgd_n2 * gm_p1 + c * cgd_n2 * go_n1 + c * cgd_n2 * go_n2 + c * cgd_n2 * go_p1 + c * cgd_n2 * go_p2 + c * cgd_p1 * gm_n1 + c * cgd_p1 * gm_n2 + c * cgd_p1 * gm_p1 + c * cgd_p1 * go_n1 + c * cgd_p1 * go_n2 + c * cgd_p1 * go_p1 + c * cgd_p1 * go_p2 + c * cgd_p2 * gm_n1 + c * cgd_p2 * go_n1 + c * cgd_p2 * go_p1 + c * cgs_n1 * go_n2 + c * cgs_n1 * go_p2 + c * cgs_n2 * go_n2 + c * cgs_n2 * go_p2 + c * cgs_p1 * gm_n1 + c * cgs_p1 * go_n1 + c * cgs_p1 * go_p1 + cgd_n2 * cgd_p1 * gm_n1 + cgd_n2 * cgd_p1 * gm_n2 + cgd_n2 * cgd_p1 * gm_p1 + cgd_n2 * cgd_p1 * go_n1 + cgd_n2 * cgd_p1 * go_n2 + cgd_n2 * cgd_p1 * go_p1 + cgd_n2 * cgd_p1 * go_p2 + cgd_n2 * cgs_p1 * gm_n1 + cgd_n2 * cgs_p1 * gm_n2 + cgd_n2 * cgs_p1 * go_n1 + cgd_n2 * cgs_p1 * go_n2 + cgd_n2 * cgs_p1 * go_p1 + cgd_n2 * cgs_p1 * go_p2 + cgd_p1 * cgd_p2 * gm_n1 + cgd_p1 * cgd_p2 * gm_p1 + cgd_p1 * cgd_p2 * go_n1 + cgd_p1 * cgd_p2 * go_p1 + cgd_p1 * cgs_n1 * go_n2 + cgd_p1 * cgs_n1 * go_p2 + cgd_p1 * cgs_n2 * go_n2 + cgd_p1 * cgs_n2 * go_p2 + cgd_p1 * cgs_p1 * go_n2 + cgd_p1 * cgs_p1 * go_p2 + cgd_p2 * cgs_p1 * gm_n1 + cgd_p2 * cgs_p1 * go_n1 + cgd_p2 * cgs_p1 * go_p1 + cgs_n1 * cgs_p1 * go_n2 + cgs_n1 * cgs_p1 * go_p2 + cgs_n2 * cgs_p1 * go_n2 + cgs_n2 * cgs_p1 * go_p2) / (
                                                            c * gm_n1 * go_n2 + c * gm_n1 * go_p2 - c * gm_n2 * gm_p1 + c * go_n1 * go_n2 + c * go_n1 * go_p2 + c * go_n2 * go_p1 + c * go_p1 * go_p2 + cgd_p1 * gm_n1 * go_n2 + cgd_p1 * gm_n1 * go_p2 + cgd_p1 * gm_p1 * go_n2 + cgd_p1 * gm_p1 * go_p2 + cgd_p1 * go_n1 * go_n2 + cgd_p1 * go_n1 * go_p2 + cgd_p1 * go_n2 * go_p1 + cgd_p1 * go_p1 * go_p2 + cgs_p1 * gm_n1 * go_n2 + cgs_p1 * gm_n1 * go_p2 + cgs_p1 * go_n1 * go_n2 + cgs_p1 * go_n1 * go_p2 + cgs_p1 * go_n2 * go_p1 + cgs_p1 * go_p1 * go_p2) + s) * (
                                                           c * gm_n1 * go_n2 + c * gm_n1 * go_p2 - c * gm_n2 * gm_p1 + c * go_n1 * go_n2 + c * go_n1 * go_p2 + c * go_n2 * go_p1 + c * go_p1 * go_p2 + cgd_p1 * gm_n1 * go_n2 + cgd_p1 * gm_n1 * go_p2 + cgd_p1 * gm_p1 * go_n2 + cgd_p1 * gm_p1 * go_p2 + cgd_p1 * go_n1 * go_n2 + cgd_p1 * go_n1 * go_p2 + cgd_p1 * go_n2 * go_p1 + cgd_p1 * go_p1 * go_p2 + cgs_p1 * gm_n1 * go_n2 + cgs_p1 * gm_n1 * go_p2 + cgs_p1 * go_n1 * go_n2 + cgs_p1 * go_n1 * go_p2 + cgs_p1 * go_n2 * go_p1 + cgs_p1 * go_p1 * go_p2))
    a[2] = 1.0 * gm_n2 * gm_p1 * (
                1.0 + 1.0 * s ** 2 * (c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1) / (
                    gm_n2 * gm_p1) + 1.0 * s * (c * gm_n1 + c * go_n1 + c * go_p1 - cgd_n2 * gm_p1 - cgd_p1 * gm_n2) / (
                            gm_n2 * gm_p1)) / (
                       (1.0 * s * (cgd_n2 + cgd_p1 + cgs_n1 + cgs_n2) / (gm_n1 + go_n1 + go_p1) + 1.0) * (
                           gm_n1 + go_n1 + go_p1))
    a[3] = 1.0 * gm_n2 * gm_p1 * (
                1.0 + 1.0 * s ** 2 * (c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1) / (
                    gm_n2 * gm_p1) + 1.0 * s * (c * gm_n1 + c * go_n1 + c * go_p1 - cgd_n2 * gm_p1 - cgd_p1 * gm_n2) / (
                            gm_n2 * gm_p1)) / ((s ** 2 * (
                c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1 + cgd_n2 * cgs_p1 + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1) / (
                                                            c * gm_n1 + c * go_n1 + c * go_p1 + cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1) + s) * (
                                                           c * gm_n1 + c * go_n1 + c * go_p1 + cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    return a


def gm_middle_neg_reverse(small_signal_param, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2 = gm
    go_n1, go_n2, go_p1, go_p2 = go
    gb_n1, gb_n2, gb_p1, gb_p2 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * cgd_n2 * cgd_p1 * s / ((s * (
                cgd_n2 * cgd_p1 + cgd_n2 * cgs_p1 + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1) / (
                                                     cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1) + 1) * (
                                                    cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    a[1] = 1.0 * cgd_n2 * cgd_p1 * s / ((go_n2 + go_p2) * (s ** 2 * (
                cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                       (go_n2 + go_p2) * (
                                                                           cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s * (
                                                                       cgd_n2 * cgd_p1 * gm_n1 + cgd_n2 * cgd_p1 * gm_n2 + cgd_n2 * cgd_p1 * gm_p1 + cgd_n2 * cgd_p1 * go_n1 + cgd_n2 * cgd_p1 * go_n2 + cgd_n2 * cgd_p1 * go_p1 + cgd_n2 * cgd_p1 * go_p2 + cgd_n2 * cgs_p1 * gm_n1 + cgd_n2 * cgs_p1 * gm_n2 + cgd_n2 * cgs_p1 * go_n1 + cgd_n2 * cgs_p1 * go_n2 + cgd_n2 * cgs_p1 * go_p1 + cgd_n2 * cgs_p1 * go_p2 + cgd_p1 * cgd_p2 * gm_n1 + cgd_p1 * cgd_p2 * gm_p1 + cgd_p1 * cgd_p2 * go_n1 + cgd_p1 * cgd_p2 * go_p1 + cgd_p1 * cgs_n1 * go_n2 + cgd_p1 * cgs_n1 * go_p2 + cgd_p1 * cgs_n2 * go_n2 + cgd_p1 * cgs_n2 * go_p2 + cgd_p1 * cgs_p1 * go_n2 + cgd_p1 * cgs_p1 * go_p2 + cgd_p2 * cgs_p1 * gm_n1 + cgd_p2 * cgs_p1 * go_n1 + cgd_p2 * cgs_p1 * go_p1 + cgs_n1 * cgs_p1 * go_n2 + cgs_n1 * cgs_p1 * go_p2 + cgs_n2 * cgs_p1 * go_n2 + cgs_n2 * cgs_p1 * go_p2) / (
                                                                       (go_n2 + go_p2) * (
                                                                           cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + 1) * (
                                                    cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    a[2] = 1.0 * cgd_n2 * cgd_p1 * s ** 2 / (
                (1.0 * s * (cgd_n2 + cgd_p1 + cgs_n1 + cgs_n2) / (gm_n1 + go_n1 + go_p1) + 1.0) * (
                    gm_n1 + go_n1 + go_p1))
    a[3] = 1.0 * cgd_n2 * cgd_p1 * s ** 2 / ((go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1) * (s ** 2 * (
                cgd_n2 * cgd_p1 + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_p1 * cgd_p2 + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2) / (
                                                                                                      (
                                                                                                                  go_n2 + go_p2) * (
                                                                                                                  gm_n1 + go_n1 + go_p1)) + s * (
                                                                                                      cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_n2 * go_p1 + cgd_n2 * go_p2 + cgd_p1 * go_n2 + cgd_p1 * go_p2 + cgd_p2 * gm_n1 + cgd_p2 * go_n1 + cgd_p2 * go_p1 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2) / (
                                                                                                      (
                                                                                                                  go_n2 + go_p2) * (
                                                                                                                  gm_n1 + go_n1 + go_p1)) + 1))
    return a


def gm_middle_pos_reverse(small_signal_param, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_p1, gm_b1 = gm
    go_p1, go_b1 = go
    gb_p1, gb_p1 = gb
    cgs_p1, cgs_b1 = cgs
    cgd_p1, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * cgd_p1 / (cgd_p1 + cgs_p1)
    a[1] = 1.0 * cgd_p1 / ((s * (cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (
                cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1) + 1) * (
                                       cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1))
    a[2] = 1.0 * cgd_p1 * s
    a[3] = 1.0 * cgd_p1 * s / ((go_b1 + go_p1) * (s * (cgd_b1 + cgd_p1) / (go_b1 + go_p1) + 1))
    return a


def gm_middle_pos_reverse_r_parallel(small_signal_param, r, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_p1, gm_b1 = gm
    go_p1, go_b1 = go
    gb_p1, gb_p1 = gb
    cgs_p1, cgs_b1 = cgs
    cgd_p1, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = (1.0 * cgd_p1 * r * s + 1.0) / (r * s * (cgd_p1 + cgs_p1) + 1)
    a[1] = 1.0 * (1.0 * cgd_p1 * r * s + 1.0) / ((gm_p1 + go_b1 + go_p1) * (
                r * s ** 2 * (cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (gm_p1 + go_b1 + go_p1) + s * (
                    cgd_b1 + cgd_p1 * gm_p1 * r + cgd_p1 * go_b1 * r + cgd_p1 * go_p1 * r + cgs_p1 * go_b1 * r + cgs_p1 * go_p1 * r + cgs_p1) / (
                            gm_p1 + go_b1 + go_p1) + 1))
    a[2] = 1.0 * (1.0 * cgd_p1 * r * s + 1.0) / r
    a[3] = 1.0 * (1.0 * cgd_p1 * r * s + 1.0) / (
                (r * s * (cgd_b1 + cgd_p1) / (go_b1 * r + go_p1 * r + 1) + 1) * (go_b1 * r + go_p1 * r + 1))
    return a


def gm_middle_pos_reverse_r_series(small_signal_param, r, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_p1, gm_b1 = gm
    go_p1, go_b1 = go
    gb_p1, gb_p1 = gb
    cgs_p1, cgs_b1 = cgs
    cgd_p1, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * cgd_p1 / (cgd_p1 + cgs_p1)
    a[1] = 1.0 * cgd_p1 / ((s * (cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (
                cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1) + 1) * (
                                       cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1))
    a[2] = 1.0 * cgd_p1 * s / (1.0 * r * s * (cgd_p1 + cgs_p1) + 1.0)
    a[3] = 1.0 * cgd_p1 * s / ((go_b1 + go_p1) * (
                r * s ** 2 * (cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (go_b1 + go_p1) + s * (
                    cgd_b1 + cgd_p1 * gm_p1 * r + cgd_p1 * go_b1 * r + cgd_p1 * go_p1 * r + cgd_p1 + cgs_p1 * go_b1 * r + cgs_p1 * go_p1 * r) / (
                            go_b1 + go_p1) + 1))
    return a


def gm_middle_pos_reverse_c_parallel(small_signal_param, c, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_p1, gm_b1 = gm
    go_p1, go_b1 = go
    gb_p1, gb_p1 = gb
    cgs_p1, cgs_b1 = cgs
    cgd_p1, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * (c + cgd_p1) / (c + cgd_p1 + cgs_p1)
    a[1] = 1.0 * (c + cgd_p1) / ((s * (
                c * cgd_b1 + c * cgs_p1 + cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (
                                              c * gm_p1 + c * go_b1 + c * go_p1 + cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1) + 1) * (
                                             c * gm_p1 + c * go_b1 + c * go_p1 + cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1))
    a[2] = 1.0 * s * (c + cgd_p1)
    a[3] = 1.0 * s * (c + cgd_p1) / ((go_b1 + go_p1) * (s * (c + cgd_b1 + cgd_p1) / (go_b1 + go_p1) + 1))
    return a


def gm_middle_pos_reverse_c_series(small_signal_param, c, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_p1, gm_b1 = gm
    go_p1, go_b1 = go
    gb_p1, gb_p1 = gb
    cgs_p1, cgs_b1 = cgs
    cgd_p1, cgd_b1 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * cgd_p1 / (cgd_p1 + cgs_p1)
    a[1] = 1.0 * cgd_p1 / ((s * (cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (
                cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1) + 1) * (
                                       cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1))
    a[2] = 1.0 * c * cgd_p1 * s / (c + cgd_p1 + cgs_p1)
    a[3] = 1.0 * c * cgd_p1 * s / ((s * (
                c * cgd_b1 + c * cgd_p1 + cgd_b1 * cgd_p1 + cgd_b1 * cgs_p1 + cgd_p1 * cgs_p1) / (
                                                c * go_b1 + c * go_p1 + cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1) + 1) * (
                                               c * go_b1 + c * go_p1 + cgd_p1 * gm_p1 + cgd_p1 * go_b1 + cgd_p1 * go_p1 + cgs_p1 * go_b1 + cgs_p1 * go_p1))
    return a


def gm_middle_neg_reverse_r_parallel(small_signal_param, r, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2 = gm
    go_n1, go_n2, go_p1, go_p2 = go
    gb_n1, gb_n2, gb_p1, gb_p2 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = (1.0 * cgd_n2 * cgd_p1 * r * s ** 2 / (gm_n1 + go_n1 + go_p1) + 1.0 * s * (
                cgd_n2 + cgd_p1 + cgs_n1 + cgs_n2) / (gm_n1 + go_n1 + go_p1) + 1.0) / (r * s ** 2 * (
                cgd_n2 * cgd_p1 + cgd_n2 * cgs_p1 + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1) / (
                                                                                                   gm_n1 + go_n1 + go_p1) + s * (
                                                                                                   cgd_n2 + cgd_p1 * gm_n1 * r + cgd_p1 * gm_p1 * r + cgd_p1 * go_n1 * r + cgd_p1 * go_p1 * r + cgd_p1 + cgs_n1 + cgs_n2 + cgs_p1 * gm_n1 * r + cgs_p1 * go_n1 * r + cgs_p1 * go_p1 * r) / (
                                                                                                   gm_n1 + go_n1 + go_p1) + 1)
    a[1] = 1.0 * (gm_n1 + go_n1 + go_p1) * (1.0 * cgd_n2 * cgd_p1 * r * s ** 2 / (gm_n1 + go_n1 + go_p1) + 1.0 * s * (
                cgd_n2 + cgd_p1 + cgs_n1 + cgs_n2) / (gm_n1 + go_n1 + go_p1) + 1.0) / ((r * s ** 3 * (
                cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                                                    gm_n1 * go_n2 + gm_n1 * go_p2 - gm_n2 * gm_p1 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p1 + go_p1 * go_p2) + s ** 2 * (
                                                                                                    cgd_n2 * cgd_p1 * gm_n1 * r + cgd_n2 * cgd_p1 * gm_n2 * r + cgd_n2 * cgd_p1 * gm_p1 * r + cgd_n2 * cgd_p1 * go_n1 * r + cgd_n2 * cgd_p1 * go_n2 * r + cgd_n2 * cgd_p1 * go_p1 * r + cgd_n2 * cgd_p1 * go_p2 * r + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_n2 * cgs_p1 * gm_n1 * r + cgd_n2 * cgs_p1 * gm_n2 * r + cgd_n2 * cgs_p1 * go_n1 * r + cgd_n2 * cgs_p1 * go_n2 * r + cgd_n2 * cgs_p1 * go_p1 * r + cgd_n2 * cgs_p1 * go_p2 * r + cgd_n2 * cgs_p1 + cgd_p1 * cgd_p2 * gm_n1 * r + cgd_p1 * cgd_p2 * gm_p1 * r + cgd_p1 * cgd_p2 * go_n1 * r + cgd_p1 * cgd_p2 * go_p1 * r + cgd_p1 * cgd_p2 + cgd_p1 * cgs_n1 * go_n2 * r + cgd_p1 * cgs_n1 * go_p2 * r + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 * go_n2 * r + cgd_p1 * cgs_n2 * go_p2 * r + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 * go_n2 * r + cgd_p1 * cgs_p1 * go_p2 * r + cgd_p1 * cgs_p1 + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2 + cgd_p2 * cgs_p1 * gm_n1 * r + cgd_p2 * cgs_p1 * go_n1 * r + cgd_p2 * cgs_p1 * go_p1 * r + cgs_n1 * cgs_p1 * go_n2 * r + cgs_n1 * cgs_p1 * go_p2 * r + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1 * go_n2 * r + cgs_n2 * cgs_p1 * go_p2 * r + cgs_n2 * cgs_p1) / (
                                                                                                    gm_n1 * go_n2 + gm_n1 * go_p2 - gm_n2 * gm_p1 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p1 + go_p1 * go_p2) + s * (
                                                                                                    cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * gm_p1 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_n2 * go_p1 + cgd_n2 * go_p2 + cgd_p1 * gm_n1 * go_n2 * r + cgd_p1 * gm_n1 * go_p2 * r + cgd_p1 * gm_n1 + cgd_p1 * gm_n2 + cgd_p1 * gm_p1 * go_n2 * r + cgd_p1 * gm_p1 * go_p2 * r + cgd_p1 * gm_p1 + cgd_p1 * go_n1 * go_n2 * r + cgd_p1 * go_n1 * go_p2 * r + cgd_p1 * go_n1 + cgd_p1 * go_n2 * go_p1 * r + cgd_p1 * go_n2 + cgd_p1 * go_p1 * go_p2 * r + cgd_p1 * go_p1 + cgd_p1 * go_p2 + cgd_p2 * gm_n1 + cgd_p2 * go_n1 + cgd_p2 * go_p1 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2 + cgs_p1 * gm_n1 * go_n2 * r + cgs_p1 * gm_n1 * go_p2 * r + cgs_p1 * gm_n1 + cgs_p1 * go_n1 * go_n2 * r + cgs_p1 * go_n1 * go_p2 * r + cgs_p1 * go_n1 + cgs_p1 * go_n2 * go_p1 * r + cgs_p1 * go_p1 * go_p2 * r + cgs_p1 * go_p1) / (
                                                                                                    gm_n1 * go_n2 + gm_n1 * go_p2 - gm_n2 * gm_p1 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p1 + go_p1 * go_p2) + 1) * (
                                                                                                   gm_n1 * go_n2 + gm_n1 * go_p2 - gm_n2 * gm_p1 + go_n1 * go_n2 + go_n1 * go_p2 + go_n2 * go_p1 + go_p1 * go_p2))
    a[2] = 1.0 * (1.0 * cgd_n2 * cgd_p1 * r * s ** 2 / (gm_n1 + go_n1 + go_p1) + 1.0 * s * (
                cgd_n2 + cgd_p1 + cgs_n1 + cgs_n2) / (gm_n1 + go_n1 + go_p1) + 1.0) / (
                       r * (1.0 * s * (cgd_n2 + cgd_p1 + cgs_n1 + cgs_n2) / (gm_n1 + go_n1 + go_p1) + 1.0))
    a[3] = 1.0 * (1.0 * cgd_n2 * cgd_p1 * r * s ** 2 / (gm_n1 + go_n1 + go_p1) + 1.0 * s * (
                cgd_n2 + cgd_p1 + cgs_n1 + cgs_n2) / (gm_n1 + go_n1 + go_p1) + 1.0) / ((go_n2 * r + go_p2 * r + 1) * (
                r * s ** 2 * (
                    cgd_n2 * cgd_p1 + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_p1 * cgd_p2 + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2) / (
                            (gm_n1 + go_n1 + go_p1) * (go_n2 * r + go_p2 * r + 1)) + s * (
                            cgd_n2 * gm_n1 * r + cgd_n2 * gm_n2 * r + cgd_n2 * go_n1 * r + cgd_n2 * go_n2 * r + cgd_n2 * go_p1 * r + cgd_n2 * go_p2 * r + cgd_n2 + cgd_p1 * go_n2 * r + cgd_p1 * go_p2 * r + cgd_p1 + cgd_p2 * gm_n1 * r + cgd_p2 * go_n1 * r + cgd_p2 * go_p1 * r + cgs_n1 * go_n2 * r + cgs_n1 * go_p2 * r + cgs_n1 + cgs_n2 * go_n2 * r + cgs_n2 * go_p2 * r + cgs_n2) / (
                            (gm_n1 + go_n1 + go_p1) * (go_n2 * r + go_p2 * r + 1)) + 1))
    return a


def gm_middle_neg_reverse_r_series(small_signal_param, r, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2 = gm
    go_n1, go_n2, go_p1, go_p2 = go
    gb_n1, gb_n2, gb_p1, gb_p2 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * cgd_n2 * cgd_p1 * s / ((s * (
                cgd_n2 * cgd_p1 + cgd_n2 * cgs_p1 + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1) / (
                                                     cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1) + 1) * (
                                                    cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    a[1] = 1.0 * cgd_n2 * cgd_p1 * s / ((go_n2 + go_p2) * (s ** 2 * (
                cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                       (go_n2 + go_p2) * (
                                                                           cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s * (
                                                                       cgd_n2 * cgd_p1 * gm_n1 + cgd_n2 * cgd_p1 * gm_n2 + cgd_n2 * cgd_p1 * gm_p1 + cgd_n2 * cgd_p1 * go_n1 + cgd_n2 * cgd_p1 * go_n2 + cgd_n2 * cgd_p1 * go_p1 + cgd_n2 * cgd_p1 * go_p2 + cgd_n2 * cgs_p1 * gm_n1 + cgd_n2 * cgs_p1 * gm_n2 + cgd_n2 * cgs_p1 * go_n1 + cgd_n2 * cgs_p1 * go_n2 + cgd_n2 * cgs_p1 * go_p1 + cgd_n2 * cgs_p1 * go_p2 + cgd_p1 * cgd_p2 * gm_n1 + cgd_p1 * cgd_p2 * gm_p1 + cgd_p1 * cgd_p2 * go_n1 + cgd_p1 * cgd_p2 * go_p1 + cgd_p1 * cgs_n1 * go_n2 + cgd_p1 * cgs_n1 * go_p2 + cgd_p1 * cgs_n2 * go_n2 + cgd_p1 * cgs_n2 * go_p2 + cgd_p1 * cgs_p1 * go_n2 + cgd_p1 * cgs_p1 * go_p2 + cgd_p2 * cgs_p1 * gm_n1 + cgd_p2 * cgs_p1 * go_n1 + cgd_p2 * cgs_p1 * go_p1 + cgs_n1 * cgs_p1 * go_n2 + cgs_n1 * cgs_p1 * go_p2 + cgs_n2 * cgs_p1 * go_n2 + cgs_n2 * cgs_p1 * go_p2) / (
                                                                       (go_n2 + go_p2) * (
                                                                           cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + 1) * (
                                                    cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    a[2] = 1.0 * cgd_n2 * cgd_p1 * s ** 2 / ((gm_n1 + go_n1 + go_p1) * (r * s ** 2 * (
                cgd_n2 * cgd_p1 + cgd_n2 * cgs_p1 + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1) / (
                                                                                    gm_n1 + go_n1 + go_p1) + s * (
                                                                                    cgd_n2 + cgd_p1 * gm_n1 * r + cgd_p1 * gm_p1 * r + cgd_p1 * go_n1 * r + cgd_p1 * go_p1 * r + cgd_p1 + cgs_n1 + cgs_n2 + cgs_p1 * gm_n1 * r + cgs_p1 * go_n1 * r + cgs_p1 * go_p1 * r) / (
                                                                                    gm_n1 + go_n1 + go_p1) + 1))
    a[3] = 1.0 * cgd_n2 * cgd_p1 * s ** 2 / ((go_n2 + go_p2) * (gm_n1 + go_n1 + go_p1) * (r * s ** 3 * (
                cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                                                      (
                                                                                                                  go_n2 + go_p2) * (
                                                                                                                  gm_n1 + go_n1 + go_p1)) + s ** 2 * (
                                                                                                      cgd_n2 * cgd_p1 * gm_n1 * r + cgd_n2 * cgd_p1 * gm_n2 * r + cgd_n2 * cgd_p1 * gm_p1 * r + cgd_n2 * cgd_p1 * go_n1 * r + cgd_n2 * cgd_p1 * go_n2 * r + cgd_n2 * cgd_p1 * go_p1 * r + cgd_n2 * cgd_p1 * go_p2 * r + cgd_n2 * cgd_p1 + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_n2 * cgs_p1 * gm_n1 * r + cgd_n2 * cgs_p1 * gm_n2 * r + cgd_n2 * cgs_p1 * go_n1 * r + cgd_n2 * cgs_p1 * go_n2 * r + cgd_n2 * cgs_p1 * go_p1 * r + cgd_n2 * cgs_p1 * go_p2 * r + cgd_p1 * cgd_p2 * gm_n1 * r + cgd_p1 * cgd_p2 * gm_p1 * r + cgd_p1 * cgd_p2 * go_n1 * r + cgd_p1 * cgd_p2 * go_p1 * r + cgd_p1 * cgd_p2 + cgd_p1 * cgs_n1 * go_n2 * r + cgd_p1 * cgs_n1 * go_p2 * r + cgd_p1 * cgs_n2 * go_n2 * r + cgd_p1 * cgs_n2 * go_p2 * r + cgd_p1 * cgs_p1 * go_n2 * r + cgd_p1 * cgs_p1 * go_p2 * r + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2 + cgd_p2 * cgs_p1 * gm_n1 * r + cgd_p2 * cgs_p1 * go_n1 * r + cgd_p2 * cgs_p1 * go_p1 * r + cgs_n1 * cgs_p1 * go_n2 * r + cgs_n1 * cgs_p1 * go_p2 * r + cgs_n2 * cgs_p1 * go_n2 * r + cgs_n2 * cgs_p1 * go_p2 * r) / (
                                                                                                      (
                                                                                                                  go_n2 + go_p2) * (
                                                                                                                  gm_n1 + go_n1 + go_p1)) + s * (
                                                                                                      cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_n2 * go_p1 + cgd_n2 * go_p2 + cgd_p1 * gm_n1 * go_n2 * r + cgd_p1 * gm_n1 * go_p2 * r + cgd_p1 * gm_p1 * go_n2 * r + cgd_p1 * gm_p1 * go_p2 * r + cgd_p1 * go_n1 * go_n2 * r + cgd_p1 * go_n1 * go_p2 * r + cgd_p1 * go_n2 * go_p1 * r + cgd_p1 * go_n2 + cgd_p1 * go_p1 * go_p2 * r + cgd_p1 * go_p2 + cgd_p2 * gm_n1 + cgd_p2 * go_n1 + cgd_p2 * go_p1 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2 + cgs_p1 * gm_n1 * go_n2 * r + cgs_p1 * gm_n1 * go_p2 * r + cgs_p1 * go_n1 * go_n2 * r + cgs_p1 * go_n1 * go_p2 * r + cgs_p1 * go_n2 * go_p1 * r + cgs_p1 * go_p1 * go_p2 * r) / (
                                                                                                      (
                                                                                                                  go_n2 + go_p2) * (
                                                                                                                  gm_n1 + go_n1 + go_p1)) + 1))
    return a


def gm_middle_neg_reverse_c_parallel(small_signal_param, c, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2 = gm
    go_n1, go_n2, go_p1, go_p2 = go
    gb_n1, gb_n2, gb_p1, gb_p2 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * c * (1.0 + 1.0 * s * (c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1) / (
                c * (gm_n1 + go_n1 + go_p1))) * (gm_n1 + go_n1 + go_p1) / ((s * (
                c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1 + cgd_n2 * cgs_p1 + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1) / (
                                                                                        c * gm_n1 + c * go_n1 + c * go_p1 + cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1) + 1) * (
                                                                                       c * gm_n1 + c * go_n1 + c * go_p1 + cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    a[1] = 1.0 * c * (1.0 + 1.0 * s * (c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1) / (
                c * (gm_n1 + go_n1 + go_p1))) * (gm_n1 + go_n1 + go_p1) / ((s ** 2 * (
                c * cgd_n2 * cgd_p2 + c * cgd_n2 * cgs_n1 + c * cgd_n2 * cgs_n2 + c * cgd_n2 * cgs_p1 + c * cgd_p1 * cgd_p2 + c * cgd_p1 * cgs_n1 + c * cgd_p1 * cgs_n2 + c * cgd_p1 * cgs_p1 + c * cgd_p2 * cgs_n1 + c * cgd_p2 * cgs_n2 + c * cgs_n1 * cgs_p1 + c * cgs_n2 * cgs_p1 + cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                                        c * gm_n1 * go_n2 + c * gm_n1 * go_p2 - c * gm_n2 * gm_p1 + c * go_n1 * go_n2 + c * go_n1 * go_p2 + c * go_n2 * go_p1 + c * go_p1 * go_p2 + cgd_p1 * gm_n1 * go_n2 + cgd_p1 * gm_n1 * go_p2 + cgd_p1 * gm_p1 * go_n2 + cgd_p1 * gm_p1 * go_p2 + cgd_p1 * go_n1 * go_n2 + cgd_p1 * go_n1 * go_p2 + cgd_p1 * go_n2 * go_p1 + cgd_p1 * go_p1 * go_p2 + cgs_p1 * gm_n1 * go_n2 + cgs_p1 * gm_n1 * go_p2 + cgs_p1 * go_n1 * go_n2 + cgs_p1 * go_n1 * go_p2 + cgs_p1 * go_n2 * go_p1 + cgs_p1 * go_p1 * go_p2) + s * (
                                                                                        c * cgd_n2 * gm_n1 + c * cgd_n2 * gm_n2 + c * cgd_n2 * gm_p1 + c * cgd_n2 * go_n1 + c * cgd_n2 * go_n2 + c * cgd_n2 * go_p1 + c * cgd_n2 * go_p2 + c * cgd_p1 * gm_n1 + c * cgd_p1 * gm_n2 + c * cgd_p1 * gm_p1 + c * cgd_p1 * go_n1 + c * cgd_p1 * go_n2 + c * cgd_p1 * go_p1 + c * cgd_p1 * go_p2 + c * cgd_p2 * gm_n1 + c * cgd_p2 * go_n1 + c * cgd_p2 * go_p1 + c * cgs_n1 * go_n2 + c * cgs_n1 * go_p2 + c * cgs_n2 * go_n2 + c * cgs_n2 * go_p2 + c * cgs_p1 * gm_n1 + c * cgs_p1 * go_n1 + c * cgs_p1 * go_p1 + cgd_n2 * cgd_p1 * gm_n1 + cgd_n2 * cgd_p1 * gm_n2 + cgd_n2 * cgd_p1 * gm_p1 + cgd_n2 * cgd_p1 * go_n1 + cgd_n2 * cgd_p1 * go_n2 + cgd_n2 * cgd_p1 * go_p1 + cgd_n2 * cgd_p1 * go_p2 + cgd_n2 * cgs_p1 * gm_n1 + cgd_n2 * cgs_p1 * gm_n2 + cgd_n2 * cgs_p1 * go_n1 + cgd_n2 * cgs_p1 * go_n2 + cgd_n2 * cgs_p1 * go_p1 + cgd_n2 * cgs_p1 * go_p2 + cgd_p1 * cgd_p2 * gm_n1 + cgd_p1 * cgd_p2 * gm_p1 + cgd_p1 * cgd_p2 * go_n1 + cgd_p1 * cgd_p2 * go_p1 + cgd_p1 * cgs_n1 * go_n2 + cgd_p1 * cgs_n1 * go_p2 + cgd_p1 * cgs_n2 * go_n2 + cgd_p1 * cgs_n2 * go_p2 + cgd_p1 * cgs_p1 * go_n2 + cgd_p1 * cgs_p1 * go_p2 + cgd_p2 * cgs_p1 * gm_n1 + cgd_p2 * cgs_p1 * go_n1 + cgd_p2 * cgs_p1 * go_p1 + cgs_n1 * cgs_p1 * go_n2 + cgs_n1 * cgs_p1 * go_p2 + cgs_n2 * cgs_p1 * go_n2 + cgs_n2 * cgs_p1 * go_p2) / (
                                                                                        c * gm_n1 * go_n2 + c * gm_n1 * go_p2 - c * gm_n2 * gm_p1 + c * go_n1 * go_n2 + c * go_n1 * go_p2 + c * go_n2 * go_p1 + c * go_p1 * go_p2 + cgd_p1 * gm_n1 * go_n2 + cgd_p1 * gm_n1 * go_p2 + cgd_p1 * gm_p1 * go_n2 + cgd_p1 * gm_p1 * go_p2 + cgd_p1 * go_n1 * go_n2 + cgd_p1 * go_n1 * go_p2 + cgd_p1 * go_n2 * go_p1 + cgd_p1 * go_p1 * go_p2 + cgs_p1 * gm_n1 * go_n2 + cgs_p1 * gm_n1 * go_p2 + cgs_p1 * go_n1 * go_n2 + cgs_p1 * go_n1 * go_p2 + cgs_p1 * go_n2 * go_p1 + cgs_p1 * go_p1 * go_p2) + 1) * (
                                                                                       c * gm_n1 * go_n2 + c * gm_n1 * go_p2 - c * gm_n2 * gm_p1 + c * go_n1 * go_n2 + c * go_n1 * go_p2 + c * go_n2 * go_p1 + c * go_p1 * go_p2 + cgd_p1 * gm_n1 * go_n2 + cgd_p1 * gm_n1 * go_p2 + cgd_p1 * gm_p1 * go_n2 + cgd_p1 * gm_p1 * go_p2 + cgd_p1 * go_n1 * go_n2 + cgd_p1 * go_n1 * go_p2 + cgd_p1 * go_n2 * go_p1 + cgd_p1 * go_p1 * go_p2 + cgs_p1 * gm_n1 * go_n2 + cgs_p1 * gm_n1 * go_p2 + cgs_p1 * go_n1 * go_n2 + cgs_p1 * go_n1 * go_p2 + cgs_p1 * go_n2 * go_p1 + cgs_p1 * go_p1 * go_p2))
    a[2] = 1.0 * c * (1.0 * s + 1.0 * s ** 2 * (c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1) / (
                c * (gm_n1 + go_n1 + go_p1))) / (
                       1.0 * s * (cgd_n2 + cgd_p1 + cgs_n1 + cgs_n2) / (gm_n1 + go_n1 + go_p1) + 1.0)
    a[3] = 1.0 * c * (1.0 * s + 1.0 * s ** 2 * (c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1) / (
                c * (gm_n1 + go_n1 + go_p1))) / ((go_n2 + go_p2) * (s ** 2 * (
                c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1 + cgd_n2 * cgd_p2 + cgd_n2 * cgs_n1 + cgd_n2 * cgs_n2 + cgd_p1 * cgd_p2 + cgd_p2 * cgs_n1 + cgd_p2 * cgs_n2) / (
                                                                                (go_n2 + go_p2) * (
                                                                                    gm_n1 + go_n1 + go_p1)) + s * (
                                                                                c * gm_n1 + c * go_n1 + c * go_p1 + cgd_n2 * gm_n1 + cgd_n2 * gm_n2 + cgd_n2 * go_n1 + cgd_n2 * go_n2 + cgd_n2 * go_p1 + cgd_n2 * go_p2 + cgd_p1 * go_n2 + cgd_p1 * go_p2 + cgd_p2 * gm_n1 + cgd_p2 * go_n1 + cgd_p2 * go_p1 + cgs_n1 * go_n2 + cgs_n1 * go_p2 + cgs_n2 * go_n2 + cgs_n2 * go_p2) / (
                                                                                (go_n2 + go_p2) * (
                                                                                    gm_n1 + go_n1 + go_p1)) + 1))
    return a


def gm_middle_neg_reverse_c_series(small_signal_param, c, s):
    gm, go, gb, cgs, cgd = small_signal_param
    gm_n1, gm_n2, gm_p1, gm_p2 = gm
    go_n1, go_n2, go_p1, go_p2 = go
    gb_n1, gb_n2, gb_p1, gb_p2 = gb
    cgs_n1, cgs_n2, cgs_p1, cgs_p2 = cgs
    cgd_n1, cgd_n2, cgd_p1, cgd_p2 = cgd
    a = np.array([0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j])
    a[0] = 1.0 * cgd_n2 * cgd_p1 * s / ((s * (
                cgd_n2 * cgd_p1 + cgd_n2 * cgs_p1 + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1) / (
                                                     cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1) + 1) * (
                                                    cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    a[1] = 1.0 * cgd_n2 * cgd_p1 * s / ((go_n2 + go_p2) * (s ** 2 * (
                cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                       (go_n2 + go_p2) * (
                                                                           cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s * (
                                                                       cgd_n2 * cgd_p1 * gm_n1 + cgd_n2 * cgd_p1 * gm_n2 + cgd_n2 * cgd_p1 * gm_p1 + cgd_n2 * cgd_p1 * go_n1 + cgd_n2 * cgd_p1 * go_n2 + cgd_n2 * cgd_p1 * go_p1 + cgd_n2 * cgd_p1 * go_p2 + cgd_n2 * cgs_p1 * gm_n1 + cgd_n2 * cgs_p1 * gm_n2 + cgd_n2 * cgs_p1 * go_n1 + cgd_n2 * cgs_p1 * go_n2 + cgd_n2 * cgs_p1 * go_p1 + cgd_n2 * cgs_p1 * go_p2 + cgd_p1 * cgd_p2 * gm_n1 + cgd_p1 * cgd_p2 * gm_p1 + cgd_p1 * cgd_p2 * go_n1 + cgd_p1 * cgd_p2 * go_p1 + cgd_p1 * cgs_n1 * go_n2 + cgd_p1 * cgs_n1 * go_p2 + cgd_p1 * cgs_n2 * go_n2 + cgd_p1 * cgs_n2 * go_p2 + cgd_p1 * cgs_p1 * go_n2 + cgd_p1 * cgs_p1 * go_p2 + cgd_p2 * cgs_p1 * gm_n1 + cgd_p2 * cgs_p1 * go_n1 + cgd_p2 * cgs_p1 * go_p1 + cgs_n1 * cgs_p1 * go_n2 + cgs_n1 * cgs_p1 * go_p2 + cgs_n2 * cgs_p1 * go_n2 + cgs_n2 * cgs_p1 * go_p2) / (
                                                                       (go_n2 + go_p2) * (
                                                                           cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + 1) * (
                                                    cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    a[2] = 1.0 * c * cgd_n2 * cgd_p1 * s ** 2 / ((s * (
                c * cgd_n2 + c * cgd_p1 + c * cgs_n1 + c * cgs_n2 + cgd_n2 * cgd_p1 + cgd_n2 * cgs_p1 + cgd_p1 * cgs_n1 + cgd_p1 * cgs_n2 + cgd_p1 * cgs_p1 + cgs_n1 * cgs_p1 + cgs_n2 * cgs_p1) / (
                                                              c * gm_n1 + c * go_n1 + c * go_p1 + cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1) + 1) * (
                                                             c * gm_n1 + c * go_n1 + c * go_p1 + cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    a[3] = 1.0 * c * cgd_n2 * cgd_p1 * s ** 2 / ((go_n2 + go_p2) * (s ** 2 * (
                c * cgd_n2 * cgd_p1 + c * cgd_n2 * cgd_p2 + c * cgd_n2 * cgs_n1 + c * cgd_n2 * cgs_n2 + c * cgd_p1 * cgd_p2 + c * cgd_p2 * cgs_n1 + c * cgd_p2 * cgs_n2 + cgd_n2 * cgd_p1 * cgd_p2 + cgd_n2 * cgd_p1 * cgs_n1 + cgd_n2 * cgd_p1 * cgs_n2 + cgd_n2 * cgd_p1 * cgs_p1 + cgd_n2 * cgd_p2 * cgs_p1 + cgd_n2 * cgs_n1 * cgs_p1 + cgd_n2 * cgs_n2 * cgs_p1 + cgd_p1 * cgd_p2 * cgs_n1 + cgd_p1 * cgd_p2 * cgs_n2 + cgd_p1 * cgd_p2 * cgs_p1 + cgd_p2 * cgs_n1 * cgs_p1 + cgd_p2 * cgs_n2 * cgs_p1) / (
                                                                                (go_n2 + go_p2) * (
                                                                                    c * gm_n1 + c * go_n1 + c * go_p1 + cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + s * (
                                                                                c * cgd_n2 * gm_n1 + c * cgd_n2 * gm_n2 + c * cgd_n2 * go_n1 + c * cgd_n2 * go_n2 + c * cgd_n2 * go_p1 + c * cgd_n2 * go_p2 + c * cgd_p1 * go_n2 + c * cgd_p1 * go_p2 + c * cgd_p2 * gm_n1 + c * cgd_p2 * go_n1 + c * cgd_p2 * go_p1 + c * cgs_n1 * go_n2 + c * cgs_n1 * go_p2 + c * cgs_n2 * go_n2 + c * cgs_n2 * go_p2 + cgd_n2 * cgd_p1 * gm_n1 + cgd_n2 * cgd_p1 * gm_n2 + cgd_n2 * cgd_p1 * gm_p1 + cgd_n2 * cgd_p1 * go_n1 + cgd_n2 * cgd_p1 * go_n2 + cgd_n2 * cgd_p1 * go_p1 + cgd_n2 * cgd_p1 * go_p2 + cgd_n2 * cgs_p1 * gm_n1 + cgd_n2 * cgs_p1 * gm_n2 + cgd_n2 * cgs_p1 * go_n1 + cgd_n2 * cgs_p1 * go_n2 + cgd_n2 * cgs_p1 * go_p1 + cgd_n2 * cgs_p1 * go_p2 + cgd_p1 * cgd_p2 * gm_n1 + cgd_p1 * cgd_p2 * gm_p1 + cgd_p1 * cgd_p2 * go_n1 + cgd_p1 * cgd_p2 * go_p1 + cgd_p1 * cgs_n1 * go_n2 + cgd_p1 * cgs_n1 * go_p2 + cgd_p1 * cgs_n2 * go_n2 + cgd_p1 * cgs_n2 * go_p2 + cgd_p1 * cgs_p1 * go_n2 + cgd_p1 * cgs_p1 * go_p2 + cgd_p2 * cgs_p1 * gm_n1 + cgd_p2 * cgs_p1 * go_n1 + cgd_p2 * cgs_p1 * go_p1 + cgs_n1 * cgs_p1 * go_n2 + cgs_n1 * cgs_p1 * go_p2 + cgs_n2 * cgs_p1 * go_n2 + cgs_n2 * cgs_p1 * go_p2) / (
                                                                                (go_n2 + go_p2) * (
                                                                                    c * gm_n1 + c * go_n1 + c * go_p1 + cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1)) + 1) * (
                                                             c * gm_n1 + c * go_n1 + c * go_p1 + cgd_p1 * gm_n1 + cgd_p1 * gm_p1 + cgd_p1 * go_n1 + cgd_p1 * go_p1 + cgs_p1 * gm_n1 + cgs_p1 * go_n1 + cgs_p1 * go_p1))
    return a


def calculate_a_matrix(random_topo, small_signal_param, r, c):
    small_signal_param = np.array(small_signal_param)
    freq_num = 4
    a_matrix_dim = 2 * 2
    a = np.zeros([freq_num, a_matrix_dim]) + np.zeros([freq_num, a_matrix_dim]) * 1j
    b = np.zeros([freq_num, a_matrix_dim]) + np.zeros([freq_num, a_matrix_dim]) * 1j
    # b = np.zeros([len(p), block_num, 4, freq_num * 2])
    # print(np.shape(b))
    # for i in range(len(small_signal_param)):
    #     gm, go, gb, cgs, cgd = small_signal_param[i]
    mos_id = 0
    r_id = 0
    c_id = 0
    a_matrix = []
    for j in range(freq_num):
        s = 10 ** (j * 3) * 1j
        a[j] = gm_diff_pos(small_signal_param[:, mos_id:mos_id + 5], s)
    # print(small_signal_param[:, mos_id:mos_id + 5])
    mos_id += 5
    a_matrix.append(a)
    a = np.zeros([freq_num, a_matrix_dim]) + np.zeros([freq_num, a_matrix_dim]) * 1j
    for j in range(freq_num):
        s = 10 ** (j * 3) * 1j
        a[j] = gm_middle_neg(small_signal_param[:, mos_id:mos_id + 4], s)
    # print(small_signal_param[:, mos_id:mos_id + 4])
    mos_id += 4
    a_matrix.append(a)
    a = np.zeros([freq_num, a_matrix_dim]) + np.zeros([freq_num, a_matrix_dim]) * 1j
    for j in range(freq_num):
        s = 10 ** (j * 3) * 1j
        a[j] = gm_middle_pos(small_signal_param[:, mos_id:mos_id + 2], s)
    # print(small_signal_param[:, mos_id:mos_id + 2])
    mos_id += 2
    a_matrix.append(a)
    for idx, c_type in enumerate(random_topo):
        a = np.zeros([freq_num, a_matrix_dim]) + np.zeros([freq_num, a_matrix_dim]) * 1j
        if c_type == 0:
            a_matrix.append(a)
        elif c_type == 1:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = resistor(r[r_id], s)
            r_id += 1
            a_matrix.append(a)
        elif c_type == 2:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = capacitor(c[c_id], s)
            c_id += 1
            a_matrix.append(a)
        elif c_type == 3:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = r_c_parallel(r[r_id], c[c_id], s)
            r_id += 1
            c_id += 1
            a_matrix.append(a)
        elif c_type == 4:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = r_c_series(r[r_id], c[c_id], s)
            r_id += 1
            c_id += 1
            a_matrix.append(a)
        elif c_type == 5:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                if idx <= 1:
                    a[j] = gm_diff_pos(small_signal_param[:, mos_id:mos_id + 5], s)
                else:
                    a[j] = gm_middle_pos(small_signal_param[:, mos_id:mos_id + 2], s)
            if idx <= 1:
                mos_id += 5
            else:
                mos_id += 2
            a_matrix.append(a)
        elif c_type == 6:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                if idx <= 1:
                    a[j] = gm_diff_neg(small_signal_param[:, mos_id:mos_id + 5], s)
                else:
                    a[j] = gm_middle_neg(small_signal_param[:, mos_id:mos_id + 4], s)
            if idx <= 1:
                mos_id += 5
            else:
                mos_id += 4
            a_matrix.append(a)
        elif c_type == 7:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                if idx <= 1:
                    a[j] = gm_diff_pos_r_series(small_signal_param[:, mos_id:mos_id + 5], r[r_id], s)
                else:
                    a[j] = gm_middle_pos_r_series(small_signal_param[:, mos_id:mos_id + 2], r[r_id], s)
            if idx <= 1:
                mos_id += 5
            else:
                mos_id += 2
            r_id += 1
            a_matrix.append(a)
        elif c_type == 11:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_pos_r_parallel(small_signal_param[:, mos_id:mos_id + 2], r[r_id], s)
            mos_id += 2
            r_id += 1
            a_matrix.append(a)
        elif c_type == 8:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                if idx <= 1:
                    a[j] = gm_diff_pos_c_series(small_signal_param[:, mos_id:mos_id + 5], c[c_id], s)
                else:
                    a[j] = gm_middle_pos_c_series(small_signal_param[:, mos_id:mos_id + 2], c[c_id], s)
            if idx <= 1:
                mos_id += 5
            else:
                mos_id += 2
            c_id += 1
            a_matrix.append(a)
        elif c_type == 12:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_pos_c_series(small_signal_param[:, mos_id:mos_id + 2], c[c_id], s)
            mos_id += 2
            c_id += 1
            a_matrix.append(a)
        elif c_type == 9 or c_type == 13:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                if idx <= 1:
                    a[j] = gm_diff_neg_r_series(small_signal_param[:, mos_id:mos_id + 5], r[r_id], s)
                else:
                    a[j] = gm_middle_neg_r_series(small_signal_param[:, mos_id:mos_id + 4], r[r_id], s)
            if idx <= 1:
                mos_id += 5
            else:
                mos_id += 4
            r_id += 1
            a_matrix.append(a)
        elif c_type == 13:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_neg_r_parallel(small_signal_param[:, mos_id:mos_id + 4], r[r_id], s)
            mos_id += 4
            r_id += 1
            a_matrix.append(a)
        elif c_type == 10:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                if idx <= 1:
                    a[j] = gm_diff_neg_c_series(small_signal_param[:, mos_id:mos_id + 5], c[c_id], s)
                else:
                    a[j] = gm_middle_neg_c_series(small_signal_param[:, mos_id:mos_id + 4], c[c_id], s)
            if idx <= 1:
                mos_id += 5
            else:
                mos_id += 4
            c_id += 1
            a_matrix.append(a)
        elif c_type == 14:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_neg_c_parallel(small_signal_param[:, mos_id:mos_id + 4], c[c_id], s)
            mos_id += 4
            c_id += 1
            a_matrix.append(a)
        elif c_type == 15:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_pos_reverse(small_signal_param[:, mos_id:mos_id + 2], s)
            mos_id += 2
            a_matrix.append(a)
        elif c_type == 16:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_neg_reverse(small_signal_param[:, mos_id:mos_id + 4], s)
            mos_id += 4
            a_matrix.append(a)
        elif c_type == 17:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_pos_reverse_r_parallel(small_signal_param[:, mos_id:mos_id + 2], r[r_id], s)
            mos_id += 2
            r_id += 1
            a_matrix.append(a)
        elif c_type == 18:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_pos_reverse_r_series(small_signal_param[:, mos_id:mos_id + 2], r[r_id], s)
            mos_id += 2
            r_id += 1
            a_matrix.append(a)
        elif c_type == 19:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_pos_reverse_c_parallel(small_signal_param[:, mos_id:mos_id + 2], c[c_id], s)
            mos_id += 2
            c_id += 1
            a_matrix.append(a)
        elif c_type == 20:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_pos_reverse_c_series(small_signal_param[:, mos_id:mos_id + 2], c[c_id], s)
            mos_id += 2
            c_id += 1
            a_matrix.append(a)
        elif c_type == 21:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_neg_reverse_r_parallel(small_signal_param[:, mos_id:mos_id + 4], r[r_id], s)
            mos_id += 4
            r_id += 1
            a_matrix.append(a)
        elif c_type == 22:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_neg_reverse_r_series(small_signal_param[:, mos_id:mos_id + 4], r[r_id], s)
            mos_id += 4
            r_id += 1
            a_matrix.append(a)
        elif c_type == 23:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_neg_reverse_c_parallel(small_signal_param[:, mos_id:mos_id + 4], c[c_id], s)
            mos_id += 4
            c_id += 1
            a_matrix.append(a)
        elif c_type == 24:
            for j in range(freq_num):
                s = 10 ** (j * 3) * 1j
                a[j] = gm_middle_neg_reverse_c_series(small_signal_param[:, mos_id:mos_id + 4], c[c_id], s)
            mos_id += 4
            c_id += 1
            a_matrix.append(a)

    return a_matrix
