import folium

map_osm4 = folium.Map(location=[37.497929, 127.027609], zoom_start=17, 
                      tiles='Stamen Toner')
marker4 = folium.Marker([37.497929, 127.027609], popup='강남역')
marker4.add_to(map_osm4)
map_osm4.save('map_osm4.html')

map_osm5 = folium.Map(location=[37.497929, 127.027609], zoom_start=17, 
                      tiles='Stamen Terrain')
marker5 = folium.Marker([37.497929, 127.027609], popup='강남역')
marker5.add_to(map_osm5)
map_osm5.save('map_osm5.html')

map_osm6 = folium.Map(location=[37.497929, 127.027609], zoom_start=17, 
                      tiles='Stamen Toner')
marker6 = folium.CircleMarker([37.497929, 127.027609], radius=100,
                              fill_color='skyblue', popup='강남역')
marker6.add_to(map_osm6)
map_osm6.save('map_osm6.html')

map_osm7 = folium.Map(location=[37.497929, 127.027609], zoom_start=17, 
                      tiles='Stamen Terrain')
marker6.add_to(map_osm7)
map_osm7.save('map_osm7.html')
