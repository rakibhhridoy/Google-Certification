#!/usr/bin/env python3


import pandas as pd

data = pd.read_csv('../data/employees.csv')

#print(data.head())
#print(data.columns)

count = data.groupby([' Department']).count()

#print(type(count))

count.drop(columns = 'Full Name', inplace = True)

count.reset_index(inplace = True)
count.columns = ['Department','Count']

#print(count)


count.to_csv('report.txt', sep= ':', index = False, header= False)

