# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:46:46 2019

@author: Srinivas Raju
"""

import numpy as np
g=np.array([[1,2,3,4],[6,7,8,9],[1,2,4,5],int])
h=g.reshape(2,2)
print(h.ndim)
print(g.ndim)
a=np.array([1,2,3,4],dtype=float)
print(a.dtype)
b=a.reshape(2,2)
print(b)
c=a*2
print(c)
b=np.array([1+2j,5+5j])
print(b.dtype)
print(b.real)
print(b.imag)
c=a.data
print(c)
f=np.array2string(a)
print(f)
print(f.count('1'))
print(f.index('4'))
print(b.ndim)
print(b.shape)


