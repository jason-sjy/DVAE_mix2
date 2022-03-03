import numpy as np
import os

conf_file = './conf'
param_file = './param'
name = []
value = []
#for l in open(conf_file, 'r'):
with open(conf_file, 'r') as f1:
    lines = f1.readlines()
    cnt = len(lines)
    for l in lines:
        l = l.strip().split(' ')
        if l[0] == 'des_var':
            name.append(l[1])
            min = float(l[2])
            max = float(l[3])
            num = min + np.random.rand()*(max-min)
            value.append(num)

with open(param_file, 'w') as f:
    for i in range(cnt):
        f.write('.param ' + name[i] + ' = ' + str(value[i]) + '\n')

