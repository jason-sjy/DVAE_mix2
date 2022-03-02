import numpy as np
from read import *
# from a_matrix import *
import time
from tqdm import tqdm


start = time.time()
# bounds = np.array([[1e-12, 2e-12], [1e-12, 2e-12], [10e-6, 100e-6], [10e-6, 100e-6], [10e-6, 100e-6], [10e-6, 100e-6], [10e-6, 100e-6], [10e-6, 100e-6], [100e-6, 500e-6], [100e-6, 500e-6], [10e-6, 100e-6]])
bounds = np.array([[2e-6, 50e-6], [2e-6, 50e-6], [2e-6, 50e-6], [2e-6, 50e-6], [2e-6, 50e-6], [2e-6, 50e-6], [2e-6, 50e-6], [2e-6, 50e-6], [2e-6, 50e-6], [2e-6, 50e-6], [2e-6, 50e-6], [2e-6, 50e-6], [1e-12, 1e-11]])
n_sample = 10000
dataset = get_dataset(n_sample, bounds)
end = time.time()
print("generate data time:", end - start, "s")
'''
print("sizing")
print(dataset['sizing'])
print("small signal parameters")
print(dataset['param'])
print("performance")
print(dataset['performance'])
'''
print("sizing_shape")
print(np.array(dataset['sizing']).shape)
print("param_shape")
print(np.array(dataset['param']).shape)
print("performance_shape")
print(np.array(dataset['performance']).shape)

np.save('sizing{}.npy'.format(n_sample), dataset['sizing'].T)
np.save('small_signal_parameter{}.npy'.format(n_sample), dataset['param'])
np.save('performance{}.npy'.format(n_sample), dataset['performance'])


'''
a_matrix=calculate_a_matrix(dataset['param'])
data_file="data"
np.save('a_matrix.npy',a_matrix)
'''

'''
# g_list = []
value = np.load('value10000.npy')
# print(value[:5])
# print(value[0:5])
# for i in range(np.shape(value)[0]):
value = value[:, :, :, [0, 3, 4, 7]]
# print(value[:5])
value[:, :, :, :2] = np.log10(value[:, :, :, :2])
value[:, :, :, 2:] = (value[:, :, :, 2:] + np.pi) / 2 / np.pi
# print(value[:5])
np.save('amp_phase_processed_10000.npy', value)
# a_matrix1=np.load('a_matrix.npy')
# print(a_matrix1)

# print("row:",row)
# print("performance:",performance)
# print(a_matrix)
# np.save('a_matrix.npy', a_matrix)
'''
