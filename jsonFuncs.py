#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:52:57 2020

@author: adel

plotting JSON files
reads the json file & proccess it
& returns a panda(dataframe) of time and ecg readings
"""
#import identify


import pandas as pd
#from pandas.io.json import json_normalize
import json
import codecs
#import matplotlib.pyplot as plt

#name1 ,exten1 = identify.identFile('hola.json')

jsonfilename = 'ecgjson.json'

#reads the json file & proccess it & returns a panda(dataframe) of time and ecg readings
def ReadJson(jsonfilename):
    data = json.load(codecs.open(jsonfilename, 'r', 'utf-8-sig'))
    dataframe = pd.DataFrame.from_dict(data)
    ecg_dict = dataframe['ecg']['ECG']
    
    ecg_time_list =[]
    ecg_vals_list =[]

    for item in ecg_dict:
        ecg_time_list.append(list(item.keys()))
        ecg_vals_list.append(list(item.values()))

    flat_time_list = []
    flat_ecg_list = []

    def flatten(l,fl):
        for sublist in l:
            for item in sublist:
                fl.append(item) 
            
    flatten(ecg_time_list,flat_time_list)
    flatten(ecg_vals_list,flat_ecg_list)           
    jsonPanda = pd.DataFrame(flat_ecg_list,flat_time_list)
    
    return (jsonPanda,flat_time_list,flat_ecg_list)
#mypanda,time,ecg = ReadJson(jsonfilename)
    
#fig , ax = plt.subplots()
#ax.plot(mypanda[:500])
    