# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 22:51:27 2018

@author: disiz
"""

import pandas as pd

url="https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv"

dataset=pd.read_csv(url)

print(dataset.head(15))
print("-"*80)

dataset.shape

#1. Delete unnamed columns
dataset=dataset.drop(dataset.columns[dataset.columns.str.contains('unnamed',case=False)],axis=1)
print(dataset.head(5))
print("-"*80)

# 2. Show the distribution of male and female
print(dataset.groupby('Gender').count()['Count'])
print("-"*80)

# 3. Show the top 5 most preferred names
c = dataset.groupby('Name').count()
c = c.sort_values(['Count'], ascending=False)
print(c.head(5)['Count'])
print("-"*80)

#4. What is the median name occurence in the dataset
print(c.iloc[int(c.shape[0]/2),4:])
print("-"*80)

#5. Distribution of male and female born count by states
print(dataset.pivot_table(index='State', columns='Gender', values='Count', aggfunc='sum'))
print("-"*80)

print("End of assignment")
