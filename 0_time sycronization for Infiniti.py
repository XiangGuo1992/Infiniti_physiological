# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 22:17:52 2018

@author: Inki Kim's lab
"""



import os
import pandas as pd
from tqdm import tqdm


timesycronization = pd.read_csv('path/to/time syncronization.csv')

rename = pd.read_excel('path/to/rename_2017.xlsx')

os.chdir('path/to/1_CleanedData')

outputpath = 'path/to/2_SycronizedData\\'


data = pd.DataFrame()



for file in tqdm(timesycronization.iloc[:,0]):
    trial = file.split('-')[0]
    index = list(timesycronization.iloc[:,0]).index(file)
    
    if trial not in list(rename['trial']):
        print('{} not in list'.format(trial))
        continue
    
    index2 = list(rename['trial']).index(trial)
    
    txtfile = rename['original name'][index2]
    
    df = pd.read_csv(txtfile)
    
    if 'Event' in df.columns:
        #print('Event in columns')
        startpoint = df['Time'][df['Time'][df['Event']=='start'].index[0]]
    else:
        startpoint = 'nan'
        print('{} has no Event'.format(file))
        continue
    
    newdata= pd.DataFrame(0, index=range(1), columns=range(3))
    
    newdata.iloc[0,0] = trial
    newdata.iloc[0,1] = timesycronization['start time'][index]  
    newdata.iloc[0,2] = startpoint  
    
    data = data.append(newdata)
    
    df2 = df[df['Event']=='start']
    df2.index = range(len(df2))
    df2.iloc[:,0] = df2.iloc[:,0] - df2.iloc[0,0]
    
    df2.to_csv(outputpath + trial +'.csv',index = False)
    #print('file {} with experiment start and start point {} is output'.format(trial,startpoint))
  
    

    
    
    
data.to_csv('path/to/Physiological_startTime.csv',index = False)    
