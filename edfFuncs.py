#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:12:28 2020

@author: adel

READ EDF FILE AND RETURN 5 channels DataFrame + chs_names (all in tuple)
"""
#%matplotlib inline
#import matplotlib.pyplot as plt
#import plotly.plotly as py
#import numpy as np
import mne
import pandas as pd
#from plotly import tools
#from plotly.graph_objs import Layout, YAxis, Scatter, Annotation, Annotations, Data, Figure, Marker, Font
#plt.ion()

edffilename = "Normal_Subject_01.edf"
def ReadEdf(edffilename):
    mne.set_log_level("WARNING")
    raw = mne.io.read_raw_edf(edffilename, preload=False)
    #raw.plot()
    start, stop = raw.time_as_index([100, 115])  # 100 s to 115 s data segment
    
    picks = mne.pick_types(raw.info,include=(raw.ch_names))
    n_channels = len(raw.ch_names)
    data, times = raw[picks[:n_channels], start:stop]
    ch_names = [raw.info['ch_names'][p] for p in picks[:n_channels]]
    edfPanda1 = pd.DataFrame(data[0],times)
    edfPanda2 = pd.DataFrame(data[1],times)
    edfPanda3 = pd.DataFrame(data[2],times)
    edfPanda4 = pd.DataFrame(data[3],times)
    edfPanda5 = pd.DataFrame(data[14],times)
    return(edfPanda1,edfPanda2,edfPanda3,edfPanda4,edfPanda5,ch_names)
#print(data.shape)
#print(times.shape)
#print(times.min(), times.max())
#print(picks)

#plt.plot(times[1:55], data.T[1:55])


#plotting 5 channels    
#fig,ax=plt.subplots(5,1)
#ch1,ch2,ch3,ch4,ch5,name = ReadEdf(edffilename)
#ax[0].plot(ch1,color = 'r')
#ax[1].plot(ch2)
#ax[2].plot(ch3)
#ax[3].plot(ch4)
#ax[4].plot(ch5)
#plt.xlabel('time (s)')
#plt.ylabel('MEG data (T)')
#plt.legend(loc='best')
#plt.show()
