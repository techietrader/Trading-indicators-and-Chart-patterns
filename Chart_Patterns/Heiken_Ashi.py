# -*- coding: utf-8 -*-
"""
@author: techietrader

"""

import numpy as np
import pandas as pd  

#Heiken Ashi    
def HA(df):
    df['HA_Close']=(df['Open']+ df['High']+ df['Low']+ df['Close'])/4
    df['HA_Open']=(df['Open']+df['Close'])/2   
    #df['HA_Open'][1:]= (df['HA_Open'].shift(1)+df['HA_Close'].shift(1))/2 
    for i in range(1, len(df)):
        df['HA_Open'][i]=(df['HA_Open'][i-1]+df['HA_Close'][i-1])/2 
    df['HA_High']=df[['HA_Open','HA_Close','High']].max(axis=1)
    df['HA_Low']=df[['HA_Open','HA_Close','Low']].min(axis=1)
    return df
