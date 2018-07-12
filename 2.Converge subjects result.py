# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 16:38:37 2018

@author: Inki Kim's lab
"""

import pandas as pd
import numpy as np
import os
os.chdir('G:\\Resource for Xiang\\Lian Cui experiment\\Physiological data\\2018_NewData\\3_CalcBR')
outputpath = 'G:\\Resource for Xiang\\Lian Cui experiment\\Physiological data\\2018_NewData\\4_MergedData_BR\\'
filelist = os.listdir()
namelist = [i.split(' ', 1)[0] for i in filelist]
name_unique = np.unique(namelist)

for subject in name_unique:
    result = pd.DataFrame()
    indexes = [i for i in range(len(namelist)) if namelist[i]==subject]
    for i in indexes:
        df_add = pd.read_csv(filelist[i])
        df_add['subject'] = filelist[i].split('_')[0]
        result = result.append(df_add)
    result.to_csv(outputpath + subject + '_BR_2018.csv',index=False)
    print('finish add {}'.format(subject))
    
    #result = pd.concat(df)
    