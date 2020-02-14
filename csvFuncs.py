#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:21:20 2020

@author: adel

plotting CSV files

"""

#1 - identifiy file extension  DONE
#2 - read the file and proccess it 
#3 - plot the data
#4 - 
import pandas as pd
#import matplotlib.pyplot as plt

csvfilename = "arrhythmia_csv.csv"

def ReadCsv(csvfilename):
    dataset = pd.read_csv(csvfilename)
    return dataset["heartrate"]
    

#csvpanda = ReadCsv(csvfilename)



#ax1.set_title("ZOOM") #The title of our plot
#plt.xticks(range(0, 100,5))
#ax2.set_xlabel("Heart Rate Signal") 
#ax1.plot(dataset[50:350])
#ax2.plot(dataset[x:y]) #Draw the plot object
#ax1.yticks(range(0,105,25))

#x=0
#y=600


#fig,(ax1,ax2) = plt.subplots(2,sharey=True)
#ax1.plot(csvpanda[0:200])
#ax2.plot(csvpanda[125:150])  #zoomed 
#plt.show() #Display the plot
