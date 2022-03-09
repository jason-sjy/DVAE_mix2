import numpy as np


def calculate_amp_phase(topo_num, sizing_num):
    a_matrix = np.load("a_matrix{}_{}.npy".format(topo_num, sizing_num), allow_pickle=True)
    c = []
    for i in range(np.shape(a_matrix)[0]):
        len = np.shape(a_matrix[i])[0]
        d = np.zeros((len, 8)) + np.zeros((len, 8)) * 1j
        for j in range(len):
            d[j] = np.concatenate((a_matrix[i][j][0], a_matrix[i][j][3]))
        c.append(d)
        # print(a_matrix)
    b = []
    for i in range(np.shape(c)[0]):
        # print(np.shape(a_matrix[i]))
        b.append(np.concatenate((np.log10(np.abs(c[i]) + 1e-20), np.angle(c[i])), axis=1))
    for i in range(np.shape(c)[0]):
        print(np.shape(b[i]))
    # print(b[0])
    np.save("amp_phase{}_{}.npy".format(topo_num, sizing_num), b)
    return
