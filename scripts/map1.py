import os
import gmplot
import pandas as pd

# print(os.getcwd())

GOOGLE_MAPS_API = 'AIzaSyDKWLeV-ShWfbZqZwFihXFOjgfrqhfKlhs'

data = pd.read_excel("output_coords.xlsx")
df1 = pd.DataFrame(data)
# print(df1)
# print(df1.head())


# place map
# print(df1['to'][0])
gmap = gmplot.GoogleMapPlotter(10.82302,106.62965,13, apikey=GOOGLE_MAPS_API)
    # df1['to'][0][0],df1['to'][0][1])

result_ls_to = []
result_ls_fr = []

# to_lat,to_lon = zip(*[])
for row in df1.iterrows():
    # print(row[1]['to'])
    lat_to = float(row[1]['to'].lstrip('(').rstrip(')').split(', ')[0])
    lon_to = float(row[1]['to'].lstrip('(').rstrip(')').split(', ')[1])
    result_ls_to.append((lat_to,lon_to))
    lat_fr = float(row[1]['from'].lstrip('(').rstrip(')').split(', ')[0])
    lon_fr = float(row[1]['from'].lstrip('(').rstrip(')').split(', ')[1])
    result_ls_fr.append((lat_fr,lon_fr))    
    # lon = float(row[1]['to'][1])
    # gmap.scatter(lat,lon,color='red',size =50 , marker = True)
    # gmap.plot(lat,lon, 'cornflowerblue', edge_width = 3.0)
    # # # print(row[1]['to'])
    # break
# print(len(result_ls_to))
# print(len(result_ls_fr))
# print
to_lats,to_lons = zip(*result_ls_to)
fr_lats,fr_lons = zip(*result_ls_fr)

combined_ls = []

for row in df1.iterrows():
    # print(row[1]['to'])
    lat_to = float(row[1]['to'].lstrip('(').rstrip(')').split(', ')[0])
    lon_to = float(row[1]['to'].lstrip('(').rstrip(')').split(', ')[1])
    lat_fr = float(row[1]['from'].lstrip('(').rstrip(')').split(', ')[0])
    lon_fr = float(row[1]['from'].lstrip('(').rstrip(')').split(', ')[1])
    combined_ls.append((lat_to,lon_to))
    combined_ls.append((lat_fr,lon_fr))



# combine and alternate the zip

for i in range(0,len(combined_ls),2):
    c_lats, c_lons = zip(*combined_ls[i:i+2])
    # lats,lons = 
    gmap.plot(c_lats,c_lons,'orange', edge_width = 2.0)
# coords in combined_ls:


# lats,lons = zip(*com)
# can set the size to the count of the coords 

gmap.scatter(to_lats,to_lons, 'purple', size = 50, marker = True)
gmap.scatter(fr_lats,fr_lons,'red', size = 50, marker = False )
# for row in df1.iterrows():
#     # gmap.plot()
# gmap.plot(to_lats,to_lons,'purple', edge_width = 2.0)
# gmap.plot(fr_lats,fr_lons, 'red', edge_width= 2.2)
gmap.draw("my_map.html")


