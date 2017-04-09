import sys
import numpy as np

b = np.arange(1)
c = b[:]
d = np.copy(b)
print(b,'\n')
b[0] = 9
print(b,'\n')
print(c,'\n')
print(d,'\n')
