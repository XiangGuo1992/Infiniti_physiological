# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import numpy as np
import pandas as pd
from pandas import read_csv
os.chdir('path/to/0_RawOutput')
outputpath = ('path/to/1_CleanedData')    
listfolder = os.listdir() 

for folder in listfolder:
    os.chdir('path/to/0_RawOutput'+folder) 
    listfile = os.listdir()
    for i in listfile:
        f = open(i,"r")
        lines = f.readlines()
        f.close()
        num = np.arange(8,len(lines))
        numlist = num.tolist()
        numlist.insert(0,6)
        
        f = open(outputpath+i,"w")
        for j in numlist:
            f.write(lines[j])
        f.close()





