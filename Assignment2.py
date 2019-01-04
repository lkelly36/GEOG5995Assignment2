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
                'dgtdket', 'dgtdnox', 'dgtdleg', 'ddgany')]

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

# Define binary sex, wellbeing and drug variables as 0 and 1

def CleanBin(df1):
    # Replace sex variables 1=male, 0=female
    df1.sex.replace(2.0, 0, inplace=True)
    # Replace ever tried any drug 1=yes, 2=no
    df1.ddgany.replace(2.0, 0, inplace=True)
    # Replace wellbeing category variable
    df1.ddwbcat.replace(2.0, 0, inplace=True)
    # Replace drug variables 1=yes, 2=no
    df1.dgtdcan.replace(2.0, 0, inplace=True)
    df1.dgtdamp.replace(2.0, 0, inplace=True)
    df1.dgtdlsd.replace(2.0, 0, inplace=True)
    df1.dgtdecs.replace(2.0, 0, inplace=True)
    df1.dgtdcok.replace(2.0, 0, inplace=True)
    df1.dgtdket.replace(2.0, 0, inplace=True)
    df1.dgtdnox.replace(2.0, 0, inplace=True)
    df1.dgtdleg.replace(2.0, 0, inplace=True)

# Run function and check data
CleanBin(df1)
df1.head()

"""
Descriptive Statistics and Data Visualisation using Seaborn
Documentation: https://www.seaborn.pydata.org
"""

# Calculate some descriptive statistics for outcome variable
wbmean = np.mean(df1.ddwbscore) # mean wellbeing score
wbvar = np.var(df1.ddwbscore) # variance
print(wbmean)
print(wbvar)

# Produce descriptives for all drug use data
pd.set_option('display.max_columns', 20) # change pandas print options to show whole output

desc_list = [df1.describe()] + [df1.groupby([c])[df1.columns[0]].count() 
for c in df1.columns if df1[c].dtype == 'object']
for i in desc_list:
    print(i)
    print()
    
# Produce crosstab for drug use and wellbeing category
pd.crosstab(df1['ddgany'], df1['ddwbcat'])
# Produce crosstab for use of each individual drug and wellbeing category
pd.crosstab(df1['ddwbcat'], df1['dgtdcan'])
pd.crosstab(df1['ddwbcat'], df1['dgtdamp'])
pd.crosstab(df1['ddwbcat'], df1['dgtdlsd'])
pd.crosstab(df1['ddwbcat'], df1['dgtdecs'])
pd.crosstab(df1['ddwbcat'], df1['dgtdcok'])
pd.crosstab(df1['ddwbcat'], df1['dgtdket'])
pd.crosstab(df1['ddwbcat'], df1['dgtdnox'])
pd.crosstab(df1['ddwbcat'], df1['dgtdleg'])

# Bar chart of drug use on wellbeing
sns.barplot(x='ddgany', y='ddwbscore', hue='sex', data=df1)
#Set labels, save and show plot
plt.title('Relationship between drug use and wellbeing')
plt.xlabel('Ever used any drugs')
plt.ylabel('Wellbeing Scores')
plt.savefig('../bar_wb_drug.jpg',format='jpg')
plt.figure()

# Regression plots

# Ever tried cannabis
sns.regplot(x='dgtdcan', y='ddwbscore', data=df1)
plt.title('Relationship between cannabis use and wellbeing')
plt.xlabel('Ever tried cannabis')
plt.ylabel('Wellbeing Scores')
plt.savefig('../cannabis_wb.jpg',format='jpg')
plt.figure()

"""
Linear regression showing drug use and gender as predictors of wellbeing using seaborn.
"""

# Print regression model
model = ols("ddwbscore ~ ddgany + sex", df1).fit()
print(model.summary())

"""
Linear regression showing use of different drugs as predictors of wellbeing scores using stats models.
Documentation: https://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.OLS.html

"""

# Create X variable and control for sex
X = [df1.sex, df1.dgtdcan, df1.dgtdamp, df1.dgtdlsd, df1.dgtdecs, df1.dgtdcok, df1.dgtdket, df1.dgtdnox, df1.dgtdleg]
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
X = [df1.sex, df1.dgtdcan, df1.dgtdamp, df1.dgtdlsd, df1.dgtdecs, df1.dgtdcok, df1.dgtdket, df1.dgtdleg]
X = np.array(X)
X = X.T
X = sm.add_constant(X) # Include constant

# Run second linear regression model without insignificant variables
linear_model2=sm.OLS(y,X)
result_lin2=linear_model2.fit()
print(result_lin2.summary2()) # Print summary

"""
Logistic regression model showing use of different drugs as predictors of wellbeing category using stats models.
Documentation: https://www.statsmodels.org/dev/generated/statsmodels.discrete.discrete_model.Logit.html
"""

# Define X variable
X = [df1.sex, df1.dgtdcan, df1.dgtdamp, df1.dgtdlsd, df1.dgtdecs, df1.dgtdcok, df1.dgtdket, df1.dgtdnox, df1.dgtdleg]
X = np.array(X)
X = X.T
X = sm.add_constant(X) # Include constant in regression
# y variable
y = df1.ddwbcat

# Run logistic regression model
logit_model=sm.Logit(y,X)
result=logit_model.fit()
print(result.summary2())

# Redefine X variable, removing insignificant variables from previous model and controlling for sex
X = [df1.sex, df1.dgtdlsd, df1.dgtdecs, df1.dgtdcok, df1.dgtdket, df1.dgtdnox, df1.dgtdleg]
X = np.array(X)
X = X.T
X = sm.add_constant(X) # Include constant in regression

# Run logistic regression model again
logit_model2=sm.Logit(y,X)
result=logit_model2.fit()
print(result.summary2())

# Define X without insignificant variables for final time
X = [df1.sex, df1.dgtdlsd, df1.dgtdcok, df1.dgtdket, df1.dgtdnox]
X = np.array(X)
X = X.T
X = sm.add_constant(X) # Include constant in regression

# Final fit and run logit model
logit_model2=sm.Logit(y,X)
result=logit_model2.fit()
print(result.summary2())