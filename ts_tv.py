#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:45:04 2019

@author: xhasam
"""
import os, glob
import pandas as pd
import sys
pd.set_option('display.max_colwidth', -1)

inputfile= open (sys.argv[1], 'r')

transition= ["G>A","C>T","T>C","A>G"]
transversion=["C>A","G>T","A>C","T>G","G>C","C>G","T>A","A>T"]

transi_dict={}
transv_dict={}

input_dir = inputfile

for files in glob.glob(os.path.join(input_dir,"*.stats")):
    finlename=files.split('/')[11]
    with open(files,'r') as files1:
        for line in files1:
            if line.startswith('SN'):
                lines=line.split()
                if lines[4]=='records:':
                    filedetails=finlename + ' '+'(Number of SNPs:'+ lines[5] + ')'

    with open(files,'r') as files2:
        for lines in files2:
            if lines.startswith('ST'):
                lines=lines.split()
                if lines[2] in transition:
                    muts= lines[2:]
                    sets_transi=[words for segment in muts for words in segment.split()] 
                    transi_dict.setdefault(filedetails,[]).append(sets_transi)
                    #transi_result=pd.DataFrame.from_dict(transi_dict, orient='index')
                    #with open('transition_results', 'w') as transifile:
                     #   transifile.write(str(transi_result))
                if lines[2] in transversion:
                    mut2s=lines[2:]
                    sets_transv=[words1 for segment1 in mut2s for words1 in segment1.split()] 
                    transv_dict.setdefault(filedetails,[]).append(sets_transv)


transi_result=pd.DataFrame.from_dict(transi_dict)
transv_result=pd.DataFrame.from_dict(transv_dict)
transi_result.to_excel("transitions.xlsx")
transv_result.to_excel("transversion.xlsx")
