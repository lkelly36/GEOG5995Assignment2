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
Guide obtained from https://realpython.com/python-data-cleaning-numpy-pandas/
"""

# Select and keep only required variables
df1 = df[['pupilwt', 'version', 'region', 'age1115', 'sex', 'ethnicgpr', 'dgtdcan', 'dgtdamp','dgtdlsd','dgtdecs', 'dgtdsem', 'dgtdpop','dgtdtrn', 'dgtdher', 'dgtdmsh','dgtdmth', 'dgtdcrk', 'dgtdcok', 'dgtdket', 'dgtdmph','dgtdnox', 'dgtdleg', 'devrstm', 'devrpsy', 'devropi', 'devrcla', 'devrps', 'ddgany']]
df1.head()
