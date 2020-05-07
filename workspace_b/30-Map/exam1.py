import folium

map_osm =folium.Map(location=[37.497929, 127.027609], zoom_start=17)
map_osm.save('map_osm.html')

map_osm1 =folium.Map(location=[37.497929, 127.027609], zoom_start=17)
marker1 = folium.Marker([37.497929, 127.027609],popup='강남역', icon=folium.Icon(color='red', icon='info-sign'))

marker1.add_to(map_osm1)
map_osm1.save('map_osm1.html')

map_osm2 =folium.Map(location=[37.497929, 127.027609], zoom_start=17)
marker2 = folium.Marker([37.497929, 127.027609], popup='강남역', icon=folium.Icon(color='blue', icon='cloud'))

marker2.add_to(map_osm2)
map_osm2.save('map_osm2.html')

map_osm3 =folium.Map(location=[37.497929, 127.027609], zoom_start=17)
marker3 = folium.CircleMarker([37.497929, 127.027609], radius=100, color='#3186CC', 
                        fill_color='#3186CC', popup='강남역', )

marker3.add_to(map_osm3)
map_osm3.save('map_osm3.html')
