import folium
from pandas import DataFrame
from pandas import ExcelFile

xlsx = ExcelFile('../data/school2019.xlsx')
df = xlsx.parse(xlsx.sheet_names[0])
#print(df)

df2 = df.filter(['학교명', '학교급구분', '소재지도로명주소', '위도', '경도',])

#print(df2)

df3 = df2[df2['학교급구분'] == '고등학교']
df4 = df3[df3['소재지도로명주소'].str.contains('경기도') == True]

print(df4)

map_osm = folium.Map(location=[37.572833, 126.976894], zoom_start=12)
#map_osm.save('map_osm.html')

for i in df4.index:
    name = df4.loc[i, '학교명']
    lat = df4.loc[i, '위도']
    lng = df4.loc[i, '경도']
    
    marker = folium.Marker([lat, lng], pupup=name)
    marker.add_to(map_osm)

map_osm.save('map_osm.html')
