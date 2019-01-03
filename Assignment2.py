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
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

# Read in the data set

df = pd.read_table('~/Desktop/Data/sdd_archive.tab', low_memory=False)

"""
Cleaning the data using numpy and pandas
Guides obtained from http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
and https://realpython.com/python-data-cleaning-numpy-pandas/
and https://machinelearningmastery.com/handle-missing-data-python/
"""

# Select required variables and assign to df1
df1 = df.loc[:,('pupilwt','age1115', 'sex', 'ddwbscore', 'ddwbcat', 'dgtdcan', 
                'dgtdamp','dgtdlsd','dgtdecs', 'dgtdcok', 'dgtdket', 'dgtdnox',
                'dgtdleg', 'devrstm', 'devrpsy', 'devropi', 'devrcla', 
                'devrps', 'ddgany')]

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

# Change NaNs to average mean
df1 = df1.fillna(df1.mean())
df1.head()

# Check datatype
df1.info()

# Change floats to int
df1 = df1.astype(int)

# Create functions for binary variables

def CleanBin(df1):
   
    # Replace sex variables
    df1.sex.replace(1.0, 'male', inplace=True)
    df1.sex.replace(2.0, 'female', inplace=True)
    
    # Replace ever tried drug variables
    df1.dgtdcan.replace(1.0, 'yes', inplace=True)
    df1.dgtdcan.replace(2.0, 'no', inplace=True)
    df1.dgtdamp.replace(1.0, 'yes', inplace=True)
    df1.dgtdamp.replace(2.0, 'no', inplace=True)
    df1.dgtdlsd.replace(1.0, 'yes', inplace=True)
    df1.dgtdlsd.replace(2.0, 'no', inplace=True)
    df1.dgtdecs.replace(1.0, 'yes', inplace=True)
    df1.dgtdecs.replace(2.0, 'no', inplace=True)
    df1.dgtdcok.replace(1.0, 'yes', inplace=True)
    df1.dgtdcok.replace(2.0, 'no', inplace=True)
    df1.dgtdket.replace(1.0, 'yes', inplace=True)
    df1.dgtdket.replace(2.0, 'no', inplace=True)
    df1.dgtdnox.replace(1.0, 'yes', inplace=True)
    df1.dgtdnox.replace(2.0, 'no', inplace=True)
    df1.dgtdleg.replace(1.0, 'yes', inplace=True)
    df1.dgtdleg.replace(2.0, 'no', inplace=True)
    
    # Replace ever tried drug group variables
    df1.devrstm.replace(1.0, 'yes', inplace=True)
    df1.devrstm.replace(2.0, 'no', inplace=True)
    df1.devrpsy.replace(1.0, 'yes', inplace=True)
    df1.devrpsy.replace(2.0, 'no', inplace=True)
    df1.devropi.replace(1.0, 'yes', inplace=True)
    df1.devropi.replace(2.0, 'no', inplace=True)
    df1.devrcla.replace(1.0, 'yes', inplace=True)
    df1.devrcla.replace(2.0, 'no', inplace=True)
    df1.devrps.replace(1.0, 'yes', inplace=True)
    df1.devrps.replace(2.0, 'no', inplace=True)
    
    # Replace ever tried any drug
    df1.ddgany.replace(1.0, 'yes', inplace=True)
    df1.ddgany.replace(2.0, 'no', inplace=True)
    
    # Replace wellbeing category
    df1.ddwbcat.replace(1.0, 'low wellbeing', inplace=True)
    df1.ddwbcat.replace(2.0, 'not low wellbeing', inplace=True)

# Run function for binary variables
CleanBin(df1)

# Check data
df1.head()

"""
Descriptive Statistics and Data Visualisation using Numpy and Seaborn
"""

# Create plot to show distribution of wellbeing score
#sns.distplot(df1.ddwbscore)
#plt.title('Histogram of Wellbeing Scores')
#plt.xlabel('Wellbeing Scores')
#plt.ylabel('Estimated Density')
#plt.xticks((0,2,4,6,8,10,12,14,16,18,20))
#plt.xlim([0,20])
#plt.savefig('wellbeing_hist.jpg')
#plt.figure()

# Calculate descriptive statistics

wbmean = np.mean(df1.ddwbscore) # mean wellbeing score
wbvar = np.var(df1.ddwbscore) # variance
print(wbmean)
print(wbvar)

# Set parameters for visualising central tendency of wellbeing scores
xk,yk = ax.get_lines()[0].get_data()
mm = np.mean(df1.ddwbscore)
md = np.median(df1.ddwbscore)
mo = xk[np.argmax(yk)]

# Plot central tendency of wellbeing scores - including mean, median and KDE estimated mode
plt.figure(figsize=(5,2))
plt.plot(xk,yk,'-k')
xx = np.ones(2)
yy = np.array([0, 0.8])
plt.plot(mm*xx,yy,'--b',label='Mean')
plt.plot(md*xx,yy,'-.r',label='Median')
plt.plot(mo*xx,yy,':m',label='KDE-estimated Mode')
plt.xlabel('Wellbeing Score')
plt.ylabel('Estimated Density')
plt.xlim([0,20])
plt.legend()
plt.tight_layout()
plt.savefig('wellbeing_cent_tend.jpg')
plt.show()
    
