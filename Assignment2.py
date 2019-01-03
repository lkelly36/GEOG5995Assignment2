"""
===================================================================================================================================

Assignment 2
GEOG5995M Programming for Social Scientists
University of Leeds student ID number: 201282995

This assignment looks to build a programme that will clean data, produce 
some descriptive statistics and analyse the data using regression models.

The data set used for this assignment was the Smoking, Drinking and Drug Use 
Among Young People (2016), which can be obtained from 
https://beta.ukdataservice.ac.uk/datacatalogue/studies/study?id=8320

===================================================================================================================================

"""

"""
Import libraries and data set using Pandas to convert .tab file
Documentation: https://www.pandas.pydata.org
"""
# Import required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Read in the data set

df = pd.read_table('~/Desktop/Data/sdd_archive.tab', low_memory=False)

"""
Cleaning the data using Numpy (https://www.numpy.org) and Pandas
Guides obtained from http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
and https://realpython.com/python-data-cleaning-numpy-pandas/
and https://machinelearningmastery.com/handle-missing-data-python/
"""

# Select required variables and assign to df1
df1 = df.loc[:,('pupilwt','age1115', 'sex', 'ddwbscore', 'ddwbcat', 'dgtdcan', 'dgtdamp','dgtdlsd','dgtdecs', 'dgtdcok', 
                'dgtdket', 'dgtdnox', 'dgtdleg', 'devrstm', 'devrpsy', 'devropi', 'devrcla', 'devrps', 'ddgany')]

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
    df1.devrps.replace(nan_values, np.nan, inplace=True)
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
# Check data
df1.head()

# Define binary sex  and drug variables

def CleanBin(df1):
    # Replace sex variables
    df1.sex.replace(1.0, 'male', inplace=True)
    df1.sex.replace(2.0, 'female', inplace=True)
    # Replace ever tried any drug
    df1.ddgany.replace(1.0, 'yes', inplace=True)
    df1.ddgany.replace(2.0, 'no', inplace=True)

CleanBin(df1)

"""
Descriptive Statistics and Data Visualisation using Seaborn
Documentation: https://www.seaborn.pydata.org
"""

# Calculate some descriptive statistics

wbmean = np.mean(df1.ddwbscore) # mean wellbeing score
wbvar = np.var(df1.ddwbscore) # variance
print(wbmean)
print(wbvar)

<<<<<<< HEAD

=======
>>>>>>> 56e42bd731f8e13cd130df4aa25d1c6b56256153
# Bar chart of drug use on wellbeing
sns.barplot(x='ddgany', y='ddwbscore', hue='sex', data=df1)
#Set labels, save and show plot
plt.title('Relationship between drug use and wellbeing')
plt.xlabel('Ever used any drugs')
plt.ylabel('Wellbeing Scores')
plt.savefig('../bar_wb_drug.jpg',format='jpg')
plt.figure()

"""
Linear regression showing drug use and gender as predictors of wellbeing.
Using seaborn for visualisation and statsmodels for regression.
Documentation: https://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.OLS.html
"""

# Print regression model
model = ols("ddwbscore ~ ddgany + sex", df1).fit()
print(model.summary())

"""
Linear regression showing use of different drugs as predictors of wellbeing.
"""

# As more variables, quicker to create X variable
X = [df1.dgtdcan, df1.dgtdamp, df1.dgtdlsd, df1.dgtdecs, df1.dgtdcok, df1.dgtdket, df1.dgtdnox, df1.dgtdleg]
X = np.array(X)
X = X.T
X = sm.add_constant(X) # Include constant in regression
# Create response variable - wellbeing scores
y = df1.ddwbscore

# Run linear regression model and print summary
linear_model=sm.OLS(y,X)
result_lin=linear_model.fit()
print(result_lin.summary2())

# Remove insignificant variables from model
X = [df1.dgtdcan, df1.dgtdamp, df1.dgtdlsd, df1.dgtdecs, df1.dgtdcok, df1.dgtdket, df1.dgtdleg]
X = np.array(X)
X = X.T
X = sm.add_constant(X) # Include constant

# Run second linear regression model without insignificant variables
linear_model2=sm.OLS(y,X)
result_lin2=linear_model2.fit()
print(result_lin2.summary2()) # Print summary

"""
Final linear regression model showing use of which drug categories has most
substantial effect on wellbeing.
"""
# Remove insignificant variables from model
X = [df1.devrstm, df1.devrpsy, df1.devropi, df1.devrcla, df1.devrps]
X = np.array(X)
X = X.T
X = sm.add_constant(X) # Include constant

# Run second linear regression model without insignificant variables
linear_model3=sm.OLS(y,X)
result_lin3=linear_model3.fit()
print(result_lin3.summary2()) # Print summary
