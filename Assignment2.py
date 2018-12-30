"""
Assignment 2
GEOG5995M Programming for Social Scientists
University of Leeds student ID number: 201282995

This assignment looks to build a programme that will clean data, produce 
some descriptive statistics and analyse the data using regression models.

The data set used for this assignment was the Smoking, Drinking and Drug Use 
Among Young People (2016), which can be obtained from 
https://beta.ukdataservice.ac.uk/datacatalogue/studies/study?id=8320
"""

"""
Import libraries and data set using Pandas to convert .tab file
"""
# Import required libraries

import pandas as pd
import numpy as np

# Read in the data set

df = pd.read_table('~/Desktop/Data/sdd_archive.tab', low_memory=False)

"""
Cleaning the data using numpy and pandas
Guides obtained from https://realpython.com/python-data-cleaning-numpy-pandas/
and https://machinelearningmastery.com/handle-missing-data-python/
"""

# Select required variables and assign to df1
df1 = df.loc[:,('pupilwt','age1115', 'sex', 'ddwbscore', 'ddwbcat', 'dgtdcan', 'dgtdamp','dgtdlsd','dgtdecs', 'dgtdcok', 'dgtdket', 'dgtdnox', 'dgtdleg', 'devrstm', 'devrpsy', 'devropi', 'devrcla', 'devrps', 'ddgany')]

# Create functions for cleaning missing values

def CleanData(df1):
    nan_values = [-1,-8,-9] # These variables have values missing at -1,-8,-9
    df1.sex.replace(nan_values, np.nan, inplace=True)
    df1.dgtdcan.replace(nan_values, np.nan, inplace=True)
    df1.dgtdamp.replace(nan_values, np.nan, inplace=True)
    df1.dgtdlsd.replace(nan_values, np.nan, inplace=True)
    df1.dgtdecs.replace(nan_values, np.nan, inplace=True)
    df1.dgtdcok.replace(nan_values, np.nan, inplace=True)
    df1.dgtdket.replace(nan_values, np.nan, inplace=True)
    df1.dgtdnox.replace(nan_values, np.nan, inplace=True)
    df1.dgtdleg.replace(nan_values, np.nan, inplace=True)
    df1.devrstm.replace(nan_values, np.nan, inplace=True)
    df1.devrpsy.replace(nan_values, np.nan, inplace=True)
    df1.devropi.replace(nan_values, np.nan, inplace=True)
    df1.devrcla.replace(nan_values, np.nan, inplace=True)
    df1.devrrps.replace(nan_values, np.nan, inplace=True)
    df1.ddgany.replace(nan_values, np.nan, inplace=True)
    
def CleanWell(df1):
    nan_values = [-8,-9,-98] # These variables have values missing at -8,-9,-98
    df1.ddwbscore.replace(nan_values, np.nan, inplace=True)
    df1.ddwbcat.replace(nan_values, np.nan, inplace=True)

# Run functions
CleanData(df1)
CleanWell(df1)
    
