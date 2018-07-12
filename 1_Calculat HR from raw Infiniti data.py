# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 20:50:22 2018

@author: Inki Kim's lab
"""

import os
import pandas as pd
from tqdm import tqdm
from biosppy.signals import ecg

os.chdir('G:\\Resource for Xiang\\Lian Cui experiment\\Physiological data\\2018_NewData\\2_SycronizedData')
outputpath = 'G:\\Resource for Xiang\\Lian Cui experiment\\Physiological data\\2018_NewData\\3_CalcHR\\'


for file in tqdm(os.listdir()):
    signal = pd.read_csv(file)
    out = ecg.ecg(signal=signal.iloc[:,1], sampling_rate=2048, show=True)
    ts_hr = out['heart_rate_ts']
    hr = out['heart_rate']
    df = pd.DataFrame({'time':ts_hr})
    df['Heart_rate'] = hr
    df.to_csv(outputpath + file.split('.')[0] + '_HR_2018.csv', index = False)
