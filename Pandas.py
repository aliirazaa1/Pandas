# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14C3IrRK0nJ-BeExC5fvZZ4WvMb4akVtZ
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'Name': ['Ali', 'Ahsan', 'Hamza', 'Umer', 'Ali']
                   , 'Marks':[67, 78, np.nan, np.nan, 90]
                   , 'Age': (np.random.randint(10, 25, size=[5]))})
np.random.seed(5)

df

df.Age.iloc[3] = np.nan

df.Age.iloc[1] = np.nan

df

# df.ffill(axis = 0)
df.Age.fillna(method = 'ffill', inplace = True)
df.Marks.fillna(method = 'ffill', inplace = True)
df

df.duplicated(['Name'])

df.drop_duplicates(['Name'], keep = 'last')

df

nameToLname = {'Ali':'Raza', 'Ahsan': 'Moiz', 'Hamza': 'Khan', 'Umer': 'Najeeb'}

df["Father's Name"] = df.Name.map(nameToLname)
df

df['Results'] = df['Marks'].apply(lambda x: 'Pass' if x>70 else 'Fail')
df

df.replace({'Ali':'Taha'}, inplace = True)
df

df.index = df.index.map(lambda i: 'Student'+str(i))
df

