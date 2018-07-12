# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:32:13 2018

@author: Inki Kim's lab
"""


import os
import pandas as pd
from tqdm import tqdm
from biosppy.signals import ecg,resp

os.chdir('path/to/2_SycronizedData')
outputpath = 'path/to/3_CalcBR/'


for file in tqdm(os.listdir()):
    signal = pd.read_csv(file)
    
    out = resp.resp(signal=signal.iloc[:,3], sampling_rate=32, show=True)
    ts_br = out['resp_rate_ts']/64
    br = out['resp_rate']
    df = pd.DataFrame({'time':ts_br})
    df['Breathe_rate'] = br*60
    df.to_csv(outputpath + file.split('.')[0] + '_BR_2017.csv', index = False)
