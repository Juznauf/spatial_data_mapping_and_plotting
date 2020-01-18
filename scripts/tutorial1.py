
# Tesla supercharging Stations in Python
# Start by installing plotly

import plotly
import chart_studio.plotly as py
import plotly.figure_factory as ff
from plotly.graph_objs import *
import math
import numpy as np
import requests 
import copy
import googlemaps
# print(plotly.__version__)  check plotly version

# to plot on mapbox maps with Plotly will need the Map
# In order to use the Google maps-directions API, you need to create an account with google and get the API key

GOOGLE_MAPS_API_KEY = "AIzaSyDKWLeV-ShWfbZqZwFihXFOjgfrqhfKlhs"


# Perform a GET request to retrieve HTML of the Google Maps Page with All tesla locations, then parse through to collect all the USA, Canada ones and store them in a dictionary. The dictionary is indexed by address and each address has a parameter for postal_code, country, latitude and longitude. 
# 

r = requests.get('https://www.tesla.com/en_CA/findus#/bounds/70,-50,42,-142,d?search=supercharger,&name=Canada')
r_copy = copy.deepcopy(r.text)

# with open('copy.txt', 'w') as out_file:
#     for line in r.text.split('\n'):
#         out_file.write(line.encode("utf8").decode('utf8'))

#     # out_file.write(r.text)
# # print(r_copy)


supercharger_locations = {}
params_for_locations = ['latitude":"', 'longitude":"']
location_param = 'location_id":"'

while True:
    # add address line to the dictionary
    index = r_copy.find(location_param)
    if index == -1:
        break
    index += len(location_param)
    print(index)

    index_end = index
    while r_copy[index_end] != '"':
        index_end += 1
    address_line_1 = r_copy[index:index_end]
    address_line_1 = str(address_line_1)
    supercharger_locations[address_line_1] = {}

    for param in params_for_locations:
        index = r_copy.find(param)
        if index == -1:
            break
        index += len(param)

        index_end = index
        while r_copy[index_end] != '"':
            index_end += 1
        supercharger_locations[address_line_1][param[0:-3]] = r_copy[index:index_end]

    r_copy = r_copy[index_end:len(r.text)]  # slice off the traversed code

all_keys = supercharger_locations.keys()
# print(supercharger_locations)


# Table of locations
# Create a table with a sample of the supercharger_locations data


data_matrix = [['Location ID', 'Latitude', 'Longitude']]
first_ten_keys = supercharger_locations.keys()
# print(first_ten_keys)
# for key in first_ten_keys[0:10]:
#     row = [key,
#            supercharger_locations[key]['latitude'],
#            supercharger_locations[key]['longitude']]
#     data_matrix.append(row)

# table = ff.create_table(data_matrix)
# py.iplot(table, filename='supercharger-locations-sample')


