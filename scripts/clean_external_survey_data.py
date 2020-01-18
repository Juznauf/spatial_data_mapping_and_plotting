import pandas as pd
import numpy as np
import random


path1 = r"D:\User\Documents\SMU CONTENT\Year 3 Sem 1\Godee Internship\Results\cleaned_external.xlsx"

path2 = r"D:\User\Documents\SMU CONTENT\Year 3 Sem 1\Godee Internship\Results\cleaned_external_online.xlsx"




# print(path1, path2)

data1 = pd.read_excel(path1)
df1 = pd.DataFrame(data1)

print(df1.columns)

# print(df1.head())

data2 = pd.read_excel(path2)
df2 = pd.DataFrame(data2)
# print(df2.columns)

# maindf = df1.append(df2, ignore_index = True)
# print(maindf.head())

# maindf.to_csv('try1.csv')
# maindf.to_excel('try2.xlsx')