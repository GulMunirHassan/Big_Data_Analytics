from pstats import Stats
import numpy as np 
from numpy import *
from scipy import stats
a=np.array([10,20,30,40,50])
#print(a)
#print(shape(a))
#print(np.reshape(a, [5, 2]))
#print(a.dtype)
#print(a[0][0])
# print('Mean= ',mean(a))
# print('Median= ',median(a))
# print('Mode = ',stats.mode(a))

import array as ar 
a=ar.array('f',[10,20,30,40,50])
print(a.count(20))
print(a.index(30))
a.remove(30)
print(a)
a.append(33)
print(a)
print(a.itemsize)
a.insert(3,90)
print(a)
