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

# Select and keep only required variables
df1 = df[['darchsn', 'pupilwt', 'version', 'region', 'age1115', 'sex', 'ethnicgpr', 'dgtdcan', 'dgtdamp','dgtdlsd','dgtdecs', 'dgtdsem', 'dgtdpop','dgtdtrn', 'dgtdher', 'dgtdmsh','dgtdmth', 'dgtdcrk', 'dgtdcok', 'dgtdket', 'dgtdmph','dgtdnox', 'dgtdleg', 'devrstm', 'devrpsy', 'devropi', 'devrcla', 'devrps', 'ddgany']]
df1.head()

# Deal with missing values

# Mark -1, -8 and -9 values as missing or NaN
df1[['pupilwt', 'version', 'region', 'age1115', 'sex', 'ethnicgpr', 'dgtdcan', 'dgtdamp','dgtdlsd','dgtdecs', 'dgtdsem', 'dgtdpop','dgtdtrn', 'dgtdher', 'dgtdmsh','dgtdmth', 'dgtdcrk', 'dgtdcok', 'dgtdket', 'dgtdmph','dgtdnox', 'dgtdleg', 'devrstm', 'devrpsy', 'devropi', 'devrcla', 'devrps', 'ddgany']] = df1[['pupilwt', 'version', 'region', 'age1115', 'sex', 'ethnicgpr', 'dgtdcan', 'dgtdamp','dgtdlsd','dgtdecs', 'dgtdsem', 'dgtdpop','dgtdtrn', 'dgtdher', 'dgtdmsh','dgtdmth', 'dgtdcrk', 'dgtdcok', 'dgtdket', 'dgtdmph','dgtdnox', 'dgtdleg', 'devrstm', 'devrpsy', 'devropi', 'devrcla', 'devrps', 'ddgany']].replace(-1, np.NaN)
df1[['pupilwt', 'version', 'region', 'age1115', 'sex', 'ethnicgpr', 'dgtdcan', 'dgtdamp','dgtdlsd','dgtdecs', 'dgtdsem', 'dgtdpop','dgtdtrn', 'dgtdher', 'dgtdmsh','dgtdmth', 'dgtdcrk', 'dgtdcok', 'dgtdket', 'dgtdmph','dgtdnox', 'dgtdleg', 'devrstm', 'devrpsy', 'devropi', 'devrcla', 'devrps', 'ddgany']] = df1[['pupilwt', 'version', 'region', 'age1115', 'sex', 'ethnicgpr', 'dgtdcan', 'dgtdamp','dgtdlsd','dgtdecs', 'dgtdsem', 'dgtdpop','dgtdtrn', 'dgtdher', 'dgtdmsh','dgtdmth', 'dgtdcrk', 'dgtdcok', 'dgtdket', 'dgtdmph','dgtdnox', 'dgtdleg', 'devrstm', 'devrpsy', 'devropi', 'devrcla', 'devrps', 'ddgany']].replace(-8, np.NaN)
df1[['pupilwt', 'version', 'region', 'age1115', 'sex', 'ethnicgpr', 'dgtdcan', 'dgtdamp','dgtdlsd','dgtdecs', 'dgtdsem', 'dgtdpop','dgtdtrn', 'dgtdher', 'dgtdmsh','dgtdmth', 'dgtdcrk', 'dgtdcok', 'dgtdket', 'dgtdmph','dgtdnox', 'dgtdleg', 'devrstm', 'devrpsy', 'devropi', 'devrcla', 'devrps', 'ddgany']] = df1[['pupilwt', 'version', 'region', 'age1115', 'sex', 'ethnicgpr', 'dgtdcan', 'dgtdamp','dgtdlsd','dgtdecs', 'dgtdsem', 'dgtdpop','dgtdtrn', 'dgtdher', 'dgtdmsh','dgtdmth', 'dgtdcrk', 'dgtdcok', 'dgtdket', 'dgtdmph','dgtdnox', 'dgtdleg', 'devrstm', 'devrpsy', 'devropi', 'devrcla', 'devrps', 'ddgany']].replace(-9, np.NaN)

# Count the number of NaN values in each column
print(df1.isnull().sum())
