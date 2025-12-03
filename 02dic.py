# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 20:08:58 2025

@author: lopif
"""
import os


os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC25')
import pandas as pd
from tqdm import tqdm
import numpy as np
with open('02.txt', 'r') as file:
    data = file.read()



#%%

#data='11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
ranges=[[int(num) for num in row.split('-')] for  row in data.split(',')]

lengths=[[len(num) for num in row.split('-')] for  row in data.split(',')]
#%%

to_check= sum([num[1]-num[0] for num in ranges])
check_ne= [num[1]-num[0] for num in lengths]
#%%
invalid=0

for r in range(len(ranges)):
    if lengths[r][0]%2+lengths[r][1]%2==2:
        print(r,'pass')
        pass
    else:
        len2=round(np.floor(lengths[r][1]/2))
        len3=round(np.ceil(lengths[r][1]/2))

        base=round(10**len2+1)
        end=min(ranges[r][1],10**(2*len2)-1)
        start=max(ranges[r][0],10**(2*len2-1))
        print(start,end)
        for n in range(round(start),end+1):
            if n%base==0:
                invalid=invalid+n
#%%

invalid=set()

for r in range(len(ranges)):
    for k in range(2,lengths[r][1]+1):
        if lengths[r][1]%k !=0:
            print(r,k,'pass')
            pass
        else:
            len2=round(np.floor(lengths[r][1]/k))
    
            base=sum(10**j for j in range(0,lengths[r][1],len2))
            end=min(ranges[r][1],10**(k*len2)-1)
            start=max(ranges[r][0],10**(k*len2-1))
            print(k,len2,base,start,end)
            for n in range(round(start),end+1):
                if n%base==0:
                    invalid.add(n)
                    print(n,base)
    for k in range(2,lengths[r][0]+1):
        if lengths[r][0]%k !=0:
            print(r,k,'pass')
            pass
        else:
            len2=round(np.floor(lengths[r][0]/k))
    
            base=sum(10**j for j in range(0,lengths[r][0],len2))
            end=min(ranges[r][1],10**(k*len2)-1)
            start=max(ranges[r][0],10**(k*len2-1))
            print(k,len2,base,start,end)
            for n in range(round(start),end+1):
                if n%base==0:
                    invalid.add(n)
                    print(n,base)

tot=sum(invalid)