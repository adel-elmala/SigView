#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:54:30 2020

@author: adel
Driver program
"""
import identify
import matplotlib.pyplot as plt
#get file name
jsonfile = "ecgjson.json"
csvfile = "arrhythmia_csv.csv"
edffile = "Normal_Subject_01.edf"

fileName , fileExtension = identify.identFile(jsonfile)

def redirectPlot(fileExtension):
    if fileExtension.lower() == '.json':
        plotJson(identify.redirect(jsonfile))
    elif fileExtension.lower() == '.edf':
        plotEdf(identify.redirect(edffile))       
    elif fileExtension.lower() == '.csv':   
        plotCsv(identify.redirect(csvfile))
    else:
        raise ValueError("File Extension Not Supported")
        
def plotJson(tuple):
    mypanda,time,ecg = tuple
    fig , ax = plt.subplots()
    ax.plot(mypanda[:500])
   
def plotEdf(tuple):
    #plotting 5 channels    
    fig,ax=plt.subplots(5,1)
    ch1,ch2,ch3,ch4,ch5,name = tuple
    
    x0 =len(ch1) 
    x1 =len(ch2) 
    x2 =len(ch3)
    x3 =len(ch4)
    x4 =len(ch5)
    ax[0].plot(ch1.iloc[1:x0,],color = 'r')
    ax[1].plot(ch2.iloc[1:x1,])
    ax[2].plot(ch3.iloc[1:x2,])
    ax[3].plot(ch4.iloc[1:x3,])
    ax[4].plot(ch5.iloc[1:x4,])
    plt.xlabel('time (s)')
    ax[0].set_ylabel(name[0])
    ax[1].set_ylabel(name[1])
    ax[2].set_ylabel(name[2])
    ax[3].set_ylabel(name[3])
    ax[4].set_ylabel(name[14])
    plt.legend(loc='best')
    plt.show()
    
 #   def zoomIn():
  #      x0 /= 2
  #      x1 /= 2
  #      x2 /= 2
  #      x3 /= 2
  #      x4 /= 2
        
    #zoomIn()
    #plotEdf(tuple)
    #plt.show()
    
def plotCsv(tuple):
    csvpanda = tuple    
    fig,(ax1,ax2) = plt.subplots(2,sharey=True)
    ax1.plot(csvpanda[0:200])
    ax2.plot(csvpanda[125:150])  #zoomed 
    plt.show() #Display the plot
    


#tests    
redirectPlot('.edf')
redirectPlot('.csv')
redirectPlot('.json')
    