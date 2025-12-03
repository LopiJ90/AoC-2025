# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 13:06:31 2025

@author: lopif
"""

import os

os.chdir(r'C:\Users\lopif\OneDrive\Documenti\AoC25')
import pandas as pd
from tqdm import tqdm
with open('01.txt', 'r') as file:
    data = file.read()

lines=[i for i in data.split('\n')]

dire=[i[0] for i in lines]
rot=[int(i[1:]) for i in lines]

#%%
for n in range(len(lines)):
    if dire[n]=='L':
        pos=(pos-rot[n])%100
    if dire[n]=='R':
        pos=(pos+rot[n])%100
    if pos==0:
        com=com+1
#%%

pos=50
com=0
zero=False

for n in range(len(lines)):
    if dire[n]=='L':
        post=(pos-rot[n])
    if dire[n]=='R':
        post=(pos+rot[n])
    pos=post%100
    if not zero:
        com=com+abs((pos-post)/100)
        if pos==0:
            com=com+(post<=0)
            #print(com,post,pos,lines[n]) 
    if zero:
        com=com+min([abs((pos-post)/100),abs((pos-100-post)/100)])

    zero=pos==0    
    print(com,post,pos,lines[n]) 

