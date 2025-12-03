# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 17:39:50 2025

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC25')
import pandas as pd
from tqdm import tqdm
with open('03.txt', 'r') as file:
    data = file.read()

import numpy as np

lines=[np.array([int(c) for c in i]) for i in data.split('\n')]

#%%
tot=0
for i in lines:
    n1=max(i[:-1])
    p=np.argmax(i[:-1])
    n2=max(i[p+1:])
    tot=tot+10*n1+n2
#%%

tot=0

for i in lines:
    nums=np.zeros(12)
    p=-1
    for j in range(12):
        print(p)
        nums[j]=max(i[p+1:len(i)-11+j])
        p=p+1+np.argmax(i[p+1:len(i)-11+j])
    print(nums)
    tot=tot+sum(10**(11-k)*nums[k] for k in range(12))