#!/usr/bin/env python
# coding: utf-8

# # **Data Cleaning**

# In[1]:


#import needed libraries
import time
import pandas as pd
import numpy as np


# In[2]:


#load the dataset and creating a copy to apply data cleaning in. 
df = pd.read_csv('flights.csv')
df_copy = df.copy()


# In[3]:


#exploring data
df_copy.head()


# In[4]:


df_copy.info()


# In[5]:


df_copy['CANCELLATION_REASON'].unique()


# In[6]:


df_copy['YEAR'].unique()


# this dataset only contains flight data for one year.

# ### Defining main data quality issues
# >1. date data type is int.
# >2. there are many rows that are unwarranted for.
# >3. cancellation reason letters are not indicative.

# In[7]:


#1. combining year, month, day rows into 1 column to create date.
df_copy['DATE'] = pd.to_datetime(df_copy[['YEAR','MONTH', 'DAY']])
df_copy.head()


# In[8]:


#1. we can replace day_of_week column with week day name instead of numbers as numbers can be confusing to interpret.
df_copy['WEEK_DAY'] = df_copy['DATE'].dt.day_name()


# In[9]:


#1. in order to compare the old day of week column and the column we created
df_copy.head()


# >__the weekdays starts with 1 which reflects to monday in the dataset.
# DAY_OF_WEEK column is now unneeded__

# In[10]:


#2. removing rows that won't be used.
df_copy.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1', 'MONTH', 'DAY','YEAR','DAY_OF_WEEK','TAXI_OUT','TAXI_IN','WHEELS_ON','WHEELS_OFF'], axis=1, inplace=True)
df_copy.head()


# >delay columns is indicative for the delay time therefore it's easier to work with than with scheduled and actual time.

# In[11]:


#4.removing columns that are repetitively described in data
df_copy.drop(['SCHEDULED_DEPARTURE','DEPARTURE_TIME','SCHEDULED_TIME','ELAPSED_TIME','SCHEDULED_ARRIVAL','ARRIVAL_TIME'], axis = 1, inplace =True)
df_copy.head()


# In[17]:


df_copy['CANCELLED'].value_counts()


# In[12]:


df_copy.info()


# In[13]:


df_copy.describe()


# In[14]:


#3. replacing letters in cancellation reason to its description
df_copy['CANCELLATION_REASON'] = df_copy['CANCELLATION_REASON'].replace(['A','B','C'],['Airline/Carrier','Weather','National Air System'])
df_copy['CANCELLATION_REASON'].unique()


# In[15]:


df_copy.head()


# In[16]:


#saving the clean dataset to analyze using tableau
df_copy.to_csv('flight_clean1.csv', index =False)

