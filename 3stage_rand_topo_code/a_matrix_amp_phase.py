import numpy as np

topo_num = 200
sizing_num = 5
a_matrix = np.load("a_matrix{}_{}.npy".format(topo_num, sizing_num), allow_pickle=True)
for i in range(np.shape(a_matrix)[0]):
    for j in range(np.shape(a_matrix[i])[0]):
        a_matrix[i][j] = np.concatenate((a_matrix[i][j][0], a_matrix[i][j][3]), axis=0)
# print(a_matrix)
b = []
for i in range(np.shape(a_matrix)[0]):
    # print(np.shape(a_matrix[i]))
    b.append(np.concatenate((np.log10(np.abs(a_matrix[i]) + 1e-20), np.angle(a_matrix[i])), axis=1))
for i in range(np.shape(a_matrix)[0]):
    print(np.shape(b[i]))
# print(b[0])
np.save("amp_phase{}_{}.npy".format(topo_num, sizing_num), b)