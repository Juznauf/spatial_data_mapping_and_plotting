
import os
import pandas as pd
import numpy as np
import googlemaps
# import requests
# import loggin
from geopy.geocoders import GoogleV3 as g
os.chdir("D:\\User\\Documents\\SMU CONTENT\\Year 3 Sem 1\\Godee Internship")
# with open("Request_2019_12_19.csv", 'r', encoding='utf-8') as in_file:
#     # print('it works')
#     counter = 0
#     for line in in_file:
#         if counter < 4:
#             print(line.split(','))
#             counter += 1
#         else:
#             break
    # line in in_file:
    #     print(line)
    #     break

GOOGLE_MAPS_API = "AIzaSyDuuwjgmoXIn80Odx5Whot6X3nW2eL2LN4"
data1 = pd.read_csv("Request_2019_12_19.csv", header=0)
# p
# print(data1[:3])
df = pd.DataFrame(data1)
# print(df.head(5))
# print(df.columns)
# for row in df.iterrows():
    # print(row)
    # print(row[1]['route_from'])
    # break
    # print(g.geocode(query = row[1]['route_from']))
    # break
# for row in df.iterrows()

gmaps = googlemaps.Client(key = GOOGLE_MAPS_API)
route_from_to_ls = []


# store the to from in a tuple and append to a list
for row in df.iterrows():

    route_from_to_ls.append((row[1]['route_from'],row[1]['route_to']))
    # print(gmaps.geocode(row[1]['route_from']))
    # break
# print(route_from_to_ls)
# writer = pd.ExcelWriter('try.xlsx')
resultls = []
result_dic = {'to': [], 'from': []}
for to,fr in route_from_to_ls:
    # print(to)
    result_to = gmaps.geocode(to)
    # print(result_to[0]["geometry"]['location']['lat'])
    # print(result_to[0]["geometry"]['location']['lng'])
    # print('\n')
    # print(fr)
    result_fr = gmaps.geocode(fr)
    # print(result_fr)

    resultls.append(((result_to[0]["geometry"]['location']['lat'],result_to[0]["geometry"]['location']['lng']),(result_fr[0]["geometry"]['location']['lat'],result_fr[0]["geometry"]['location']['lng'])))
    result_dic['to'].append((result_to[0]["geometry"]['location']['lat'],result_to[0]["geometry"]['location']['lng']))
    result_dic['from'].append((result_fr[0]["geometry"]['location']['lat'],result_fr[0]["geometry"]['location']['lng']))
    # df1 = pd.DataFrame({'to':result_to, 'from': result_fr})
    # print(df1)
    # df1.to_excel('try.xlsx')
    # break
print("done extracting !")
# print(resultls)

df1 = pd.DataFrame(result_dic)
df1.to_csv("output_coords")
print("done writing to file")
# print(df1)

# with open('latlon.csv','w') as out_file:
#     for tup in resultls:
        
#         out_file.write(tup)
#     # resultls.write(resultls)

