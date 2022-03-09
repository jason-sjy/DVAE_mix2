import os
import sys
import argparse
import logging
import time
import math
import traceback
import numpy as np
from scipy.optimize import fmin_l_bfgs_b
from shutil import copy

import igraph
import torch
from torch import nn, optim

from read import *
import os
import re
import random
import string
from netlist_generator import *
from a_matrix import *
from a_matrix_amp_phase import *


def generate_random_topo(topo_dims):
    random_topo = np.zeros(topo_dims)
    for j in range(topo_dims):
        if j <= 1:
            random_topo[j] = np.random.randint(4, 11)
            if random_topo[j] == 4:
                random_topo[j] = 0
        elif j == 2:
            random_topo[j] = np.random.randint(0, 25)
        else:
            random_topo[j] = np.random.randint(0, 5)
    return random_topo


topo_num = 100
sizing_num = 10
topo_dims = 5
topo_list = []
sizing_list = []
performance_list = []
param_list = []
r_list = []
c_list = []
a_matrix_list = []
for i in range(topo_num):
    random_topo = generate_random_topo(topo_dims)
    topo_list.append(random_topo)
    amp_generator(random_topo)
    # print(random_topo)
    for j in range(sizing_num):
        sizing, small_signal_param, performance, r, c = sample_sizing()
        sizing_list.append(sizing)
        param_list.append(small_signal_param)
        performance_list.append(performance)
        r_list.append(r)
        c_list.append(c)

        # print("small_signal_param:", np.shape(small_signal_param))
        # print("small_signal_param:", small_signal_param)
        # print("performance:", performance)
        # print("r:", r)
        # print("c:", c)
        a_matrix = calculate_a_matrix(random_topo, small_signal_param, r, c)
        # print(a_matrix)
        a_matrix_list.append(a_matrix)
# print(np.shape(topo_list))
# print(np.shape(sizing_list))
# print(np.shape(param_list))
# print(np.shape(performance_list))
# print(np.shape(r_list))
# print(np.shape(c_list))
# print(np.shape(a_matrix_list))
# print(topo_list)
# print(param_list)
# print(performance_list)
# print(r_list)
# print(c_list)
# print(a_matrix_list)
'''
for i in range(topo_num * sizing_num):
    if i % sizing_num == 0:
        print("topo:", topo_list[int(i / sizing_num)])
    print("sizing:", np.shape(sizing_list[i]))
    print("param:", np.shape(param_list[i]))
    print("performance:", np.shape(performance_list[i]))
    print("r:", np.shape(r_list[i]))
    print("c:", np.shape(c_list[i]))
    print("a_matrix:", np.shape(a_matrix_list[i]))
'''
np.save("topo{}_{}.npy".format(topo_num, sizing_num), topo_list)
np.save("sizing{}_{}.npy".format(topo_num, sizing_num), sizing_list)
np.save("param{}_{}.npy".format(topo_num, sizing_num), param_list)
np.save("performance{}_{}.npy".format(topo_num, sizing_num), performance_list)
np.save("r{}_{}.npy".format(topo_num, sizing_num), r_list)
np.save("c{}_{}.npy".format(topo_num, sizing_num), c_list)
np.save("a_matrix{}_{}.npy".format(topo_num, sizing_num), a_matrix_list)
# np.save("sizing{}_{}.npy".format(topo_num, sizing_num), sizing_list)
# performance1 = np.load("performance{}_{}.npy".format(topo_num, sizing_num))
# print(performance1)
# r1 = np.load("r{}_{}.npy".format(topo_num, sizing_num), allow_pickle=True)
# print(r1)
calculate_amp_phase(topo_num, sizing_num)
