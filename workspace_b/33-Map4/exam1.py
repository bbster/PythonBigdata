import folium
import pandas as pd
from pandas import ExcelFile
from bs4 import BeautifulSoup
from pandas import DataFrame

xlsx = ExcelFile('../data/school2019.xlsx')
df = xlsx.parse(xlsx.sheet_names[0])


df2 = df.filter(['학교명','학교급구분','소재지도로명주소'])
df2.dropna(inplace=True)

df2['idx'] = df2['소재지도로명주소'].str.find(' ').astype(int)

for i in df2.index:
    addr = df2.loc[i, '소재지도로명주소']
    idx = df2.loc[i, 'idx']
    city = addr[:idx]
    df2.loc[i,'시도'] = city
    
#print(df2)
    
df_result = df2.filter(['시도', '학교급구분', '학교명']).groupby(['시도', '학교급구분']).count()

#print(df_result)

df_school_result = df_result.rename(columns={'학교명':'학교수'})

dict_elementry = {}
for index in df_school_result.index :
    a = index[0]
    b = index[1]
    
    if b == '초등학교':
        dict_elementry[a] = df_school_result.loc[index, '학교수']
        
print(dict_elementry)
