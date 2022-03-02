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

from util import *
from dataset import *
from opt_util import *
from read import *
import os
import re
import random
import string
from netlist_generator import *

topo_dims = 5
random_topo = np.zeros((topo_dims, 1))
for j in range(topo_dims):
    if j <= 1:
        random_topo[j, 0] = np.random.randint(4, 11)
    elif j == 2:
        random_topo[j, 0] = np.random.randint(0, 25)
    else:
        random_topo[j, 0] = np.random.randint(0, 5)
    if random_topo[j, 0] == 4:
        random_topo[j, 0] = 0
# goal, constr, design_id = evaluate_topo(random_topo, constr_num, False)
# design_id = gen_random_id()
# amp_generator(design_id, random_topo)
amp_generator(random_topo)
print(random_topo)
y, z, r, c = sizing()
# os.system('hspice64 -i ./3stage.sp -o 3stage')
print("y:", np.shape(y))
print("y:", y)
print("z:", z)
print("r:", r)
print("c:", c)
