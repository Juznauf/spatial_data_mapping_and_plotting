import os
import pandas as pd
import numpy as np
import googlemaps
from geopy.geocoders import GoogleV3 as g
import clean_district_names

# change directory
os.chdir("D:\\User\\Documents\\SMU CONTENT\\Year 3 Sem 1\\Godee Internship\\Python\\tutorial_map_plot\\.venv\\Scripts")

# set API key variable
GOOGLE_MAPS_API = 'AIzaSyDKWLeV-ShWfbZqZwFihXFOjgfrqhfKlhs'

# read in raw data to dataframe
data1 = pd.read_csv("TripRequest-2019-12-19_total6000.csv", header=0)
df = pd.DataFrame(data1)
df3 = df[5000:]   # alter this line to do batch processing
# print(df3)
# read in district name list from .py
district_name_ls = clean_district_names.get_names()

# create result dataframe
data2 = {'user': [], 'origin':[],'dest':[],'origin_district':[],'dest_district':[], 'connection':[], 'round_trip':[]}


# initialize the gmaps function
gmaps = googlemaps.Client(key = GOOGLE_MAPS_API)

# initialize counter to keep track of index and avoid index or value error
counter = 0


# initialize loop through dataframe to store in data 2 dict

for row in df3.iterrows():
    # call the geocode api
    extract_from = gmaps.geocode(row[1]['route_from'])
    extract_to = gmaps.geocode(row[1]['route_to'])

    try:
        data2['origin'].append((extract_from[0]['geometry']['location']['lat'],
        extract_from[0]['geometry']['location']['lng']))

        data2['dest'].append((extract_to[0]['geometry']['location']['lat'],
        extract_to[0]['geometry']['location']['lng']))
    except IndexError:
        
        if len(data2['origin']) > len(data2['dest']):
            data2['origin'].pop(counter)
        if len(data2['dest']) > len(data2['origin']):
            data2['dest'].pop(counter)
        continue

    # add in the user name to the dataframe
    data2['user'].append(row[1]['user'])

    #add in the origin lat,lon and dest lat,lon
    origin = row[1]['route_from']
    dest = row[1]['route_to']
    
    # extract origin district

    for district in district_name_ls:
        lower = ''
        if district.lower() in extract_from[0]['formatted_address'].lower():
            lower = district
            # data2['origin_district'].append(district)
            break
        else:
            lower = 'NA'
    data2['origin_district'].append(lower)
    for district in district_name_ls: 
        upper = ''
        if district.lower() in extract_to[0]['formatted_address'].lower():
            upper = district
            break
        else:
            upper = 'NA'
    data2['dest_district'].append(upper)

    # update the round_trip column
    data2['round_trip'].append(row[1]['round_trip'])


    # update the connection column
    data2['connection'].append((data2['origin_district'][counter],data2['dest_district'][counter]))
    


    # checker for lists within dictionary, as pandas will raise array value error if lengths of lists are not equal, might consider using numpy arrays in the future to avoid this problem
    for k,v in data2.items():
        while len(v) < counter +1:
            v.append('NA')
            print('ammend')
    

    # increment counter by one after each iteration
    counter += 1
    

print(counter)
    
# checker for final iteration, for the last row in the list, check if lists are all of the same lenght, if not pad the list with 'NAs'
for k,v in data2.items():
    while len(v) < counter:
        v.append("NA")
        print("ammend")


print("done extracting !")


for k,v in data2.items():
    print(len(v))

# parse dict data2 as pd dataframe
df1 = pd.DataFrame(data2)

# write dataframe to csv
df1.to_csv("output_final_coords14.csv")

# notify when done writing
print("done writing to file")

