#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 17:12:24 2020

@author: adel


identify the file extension
"""
import jsonFuncs
import csvFuncs
import edfFuncs
import os

#make a function t retrive filename from GUI
jsonfile = "ecgjson.json"
csvfile = "arrhythmia_csv.csv"
edffile = "Normal_Subject_01.edf"
#extracting the file name & extension
def identFile(filename):
    filename, file_extension = os.path.splitext(filename)
    return (filename, file_extension)
    
#name , exten = identFile(file)    
#redirecting to it's opening func

def redirect(filename):
    name , extension = identFile(filename)
    if extension.lower() == '.json':
        print('JSON READ')
        return jsonFuncs.ReadJson(filename)
        
    elif extension.lower() == '.csv':
        #readCsv(file)
        print('CSV READ')
        return csvFuncs.ReadCsv(filename)
        
    elif extension.lower() == '.edf':
        #readEdf(file)
        print('EDF READ')
        return edfFuncs.ReadEdf(filename)
        
    else:
        raise NameError('File Extension not supported')


        
        
        