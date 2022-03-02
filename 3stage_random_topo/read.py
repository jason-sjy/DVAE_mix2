import numpy as np
import os


def convert_number(x):
    if x[-1:] == "u":
        x = float(x[:-1]) * 10 ** (-6)
    elif x[-1:] == "m":
        x = float(x[:-1]) * 10 ** (-3)
    elif x[-1:] == "n":
        x = float(x[:-1]) * 10 ** (-9)
    elif x[-1:] == "p":
        x = float(x[:-1]) * 10 ** (-12)
    elif x[-1:] == "f":
        x = float(x[:-1]) * 10 ** (-15)
    elif x[-1:] == "a":
        x = float(x[:-1]) * 10 ** (-18)
    else:
        x = float(x)
    return x


def sizing():
    # get param name
    conf_file = './conf'
    param_file = './param'
    performance_file = './3stage.ma0'
    result_file = './3stage.lis'
    name = []
    r = []
    c = []
    value = []

    with open(conf_file, 'r') as f1:
        lines = f1.readlines()
        cnt = len(lines)
        for l in lines:
            l = l.strip().split(' ')
            if l[0] == 'des_var':
                name.append(l[1])
                min = float(l[2])
                max = float(l[3])
                num = min + np.random.rand() * (max - min)
                value.append(num)
                if l[1][0] == 'r':
                    r.append(num)
                elif l[1][0] == 'c':
                    c.append(num)

    with open(param_file, 'w') as f:
        for i in range(cnt):
            f.write('.param ' + name[i] + ' = ' + str(value[i]) + '\n')

    # hspice simulation
    os.system('hspice64 -i ./3stage.sp -o 3stage')

    # get results
    with open(performance_file, 'r') as f:
        line = f.readlines()
        line = line[4].strip().split()
        gain = float(line[0])
        if line[1] == "failed" or line[2] == "failed":
            # print("failed")
            ugf = 0
            pm = -180
        else:
            ugf = float(line[1])
            pm = float(line[2])

    gm = []
    gd = []
    gb = []
    cgs = []
    cgd = []
    with open(result_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip().split()
        if len(line) == 0:
            continue
        if line[0] == "gm":
            for i in range(1, len(line)):
                gm.append(convert_number(line[i]))
        elif line[0] == "gds":
            for i in range(1, len(line)):
                gd.append(convert_number(line[i]))
        elif line[0] == "gmb":
            for i in range(1, len(line)):
                gb.append(convert_number(line[i]))
        elif line[0] == "cgs":
            for i in range(1, len(line)):
                cgs.append(convert_number(line[i]))
        elif line[0] == "cgd":
            for i in range(1, len(line)):
                cgd.append(convert_number(line[i]))
    y = [gm, gd, gb, cgs, cgd]
    z = [gain, ugf, pm]
    return y, z, r, c


def get_eval(x, bounds):
    xwb = (x.T * (bounds[:, 1] - bounds[:, 0]) + bounds[:, 0]).T
    return xwb


def get_rand_dataset(num, dim, bounds):
    x_set = np.zeros((dim, num))
    y_set = []
    z_set = []
    v_set = []
    i = 0
    while i < num:
        x = get_eval(np.random.uniform(0, 1, (dim, 1)), bounds)
        y, z = sizing(x)
        x_set[:, i:i + 1] = x
        y_set.append(y)
        z_set.append(z)
        i = i + 1
    return x_set, y_set, z_set


def get_dataset(num_train, bounds):
    dim = bounds.shape[0]
    train_x, train_y, train_z = get_rand_dataset(num_train, dim, bounds)
    dataset = {}
    dataset['sizing'] = train_x
    dataset['param'] = train_y
    dataset['performance'] = train_z
    return dataset
