import math
import random
import torch
from torch import nn
from torch.nn import functional as F, MSELoss as MSE
import torch.nn.init as init
import numpy as np
import pdb
import argparse

value = np.load("value1000.npy")
value_new = np.zeros((1000, 10, 4, 8))
z = np.zeros((4, 8))
for value_, value_new_ in zip(value, value_new):
    value_new_[1] = z
    value_new_[6] = z
    value_new_[7] = z
    value_new_[8] = z
    value_new_[9] = z
    value_new_[0] = value_[0]
    value_new_[2] = value_[1]
    value_new_[3] = value_[4]
    value_new_[4] = value_[3]
    value_new_[5] = value_[2]

print(value[0])
print(value_new[0])

np.save("value1000_10block.npy", value_new)
'''
print("average distance between z0 and z1: 0.21638306975364685")
print("average distance between z0 and z2: 2.387143850326538")
print("average distance between performance p0 and p1: 3038490.0000010855")
print("average distance between performance p0 and p2: 27316777.000007942")


a_matrix1=np.load('D:/documents/lab/performance/a_matrix10000.npy')
print(a_matrix1.shape)
print(a_matrix1[:10])

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

idx=[2,4,7,5]
if type(idx) in [list, range]:
    idx = torch.LongTensor(idx).unsqueeze(0).t()
    print(idx)
    x = torch.zeros((len(idx), 10)).scatter_(1, idx, 1)
    print(x)
else:
    idx = torch.LongTensor([idx]).unsqueeze(0)
    x = torch.zeros((1, length)).scatter_(1, idx, 1).to(self.get_device())


a=torch.Tensor([[[2,4],[5,7]],[[3,1],[9,6]]])
b=torch.Tensor([[3,1],[9,2]])
#c=torch.cat([a, b], 1)
#print(c)
#d=torch.cat([a, b], 0)
#print(d)
#a=torch.zeros(3,2)
print(a)
#a=[[[2,4],[5,7]]]
#b=torch.Tensor([[3,1]])
net=range(5)
pred_type = np.random.choice(net, p=[0.1,0.1,0.2,0.3,0.3])
print(pred_type)
#print(a.unsqueeze(1))
print(a.permute(1,2,0))
c=torch.tensor([1,7,8])
d=torch.tensor([2,4,3])
e=[]
e.append(c)
e.append(d)
e=torch.cat(e,0)
print(e)
print(nn.Softmax(1)(b))
print(b[np.arange(2),np.arange(2)])

a=torch.zeros(2,3,4)
print(a)
c = torch.cat(list(a)[::-1], 0)
print(c.size())
b = torch.cat(list(a)[::-1], 1)
print(b.size())
d = torch.cat(list(a)[::-1], -1)
print(d.size())
'''
