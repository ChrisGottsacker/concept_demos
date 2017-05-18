import sys
import numpy as np

a = np.zeros((2,3,4), dtype=np.uint8)
# print(a,'\n')
b = np.arange(6).reshape(2,3)
print('Array b:\n',b,'\n')
# print(np.clip(.5*b, 0, 3))
a[:,:,0] = b
# print('Array a:\n',a,'\n')
# print(np.where(b<3, 0, b))
b[b<3] = 0
# print(a)
