
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir("D:\\User\\Documents\\SMU CONTENT\\Year 3 Sem 1\\Godee Internship\\Python\\tutorial_map_plot\\.venv\\Scripts")


data1 = pd.read_csv("output_final_coords.csv", header=0)
maindf = pd.DataFrame(data1)


for i in range(1,15):

    data2 = pd.read_csv(f"output_final_coords{i}.csv", header = 0)
    df1 = pd.DataFrame(data2)
    print(len(df1))
    maindf = maindf.append(df1, ignore_index = True)
    print(len(maindf))
    print('ok')


maindf.to_csv('main_data1.csv') # ammended the data frame to include all the records

# print(maindf.head())


# plot data top 10 connections

# maindf['connection'].value_counts()[:20].plot(kind = 'barh')
# total number of rows ommited due to errors = 79



