import pandas as pd
import numpy as np
import folium
import html_render


centroid_lat = 16.7
centroid_lon = 81.095

x = .1

n = 10 

o_lats = np.random.uniform(low=centroid_lat - x, high=centroid_lat + x, size=(n,))
o_lons = np.random.uniform(low=centroid_lon - x, high=centroid_lon + x, size=(n,))
d_lats = np.random.uniform(low=centroid_lat - x, high=centroid_lat + x, size=(n,))
d_lons = np.random.uniform(low=centroid_lon - x, high=centroid_lon + x, size=(n,))
# print(o_lats)

df = pd.DataFrame({'origin_lng' : o_lons, 'origin_lat' : o_lats, 'destination_lng' : d_lons, 'destination_lat': d_lats})

# print(df.head())
# print(df.iterrows())
# for row in df.iterrows():
#     print(row[1]['origin_lng'])
m = folium.Map([centroid_lat, centroid_lon], zoom_start = 11)

for row in df.iterrows():
    folium.CircleMarker([row[1]['origin_lat'], row[1]['origin_lng']], radius=15, fill_color = '#3db7e4').add_to(m)

    folium.CircleMarker([row[1]['origin_lat'], row[1]['origin_lng']], radius=15, fill_color = '#red').add_to(m)

    folium.PolyLine([[row[1]['origin_lat'], row[1]['origin_lng']], 
                     [row[1]['destination_lat'], row[1]['destination_lng']]]).add_to(m)

# from tempfile import NamedTemporaryFile
# tmp = NamedTemporaryFile()
# m.save(tmp.name)
# with open(tmp.name,'r') as f:
#     folium_map = f

# html_render.run_html_server(folium_map_html)


# html_render.run_html_server(m)


m