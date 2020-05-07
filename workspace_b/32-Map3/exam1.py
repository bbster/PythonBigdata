from bs4 import BeautifulSoup as bs
from pandas import DataFrame
from pandas import ExcelFile

xlsx = ExcelFile('../data/senior_lsf.xlsx')
df = xlsx.parse(xlsx.sheet_names[0])
#print(df)

data_dict = {}
for i in df.index:
    key = df.loc[i, 'COUNTY']
    value = df.loc[i, 'NUMBER']
    data_dict[key] = value
    
print(data_dict)

map_svg = None

with open('../data/seoul.svg', 'r', encoding='UTF-8') as f:
    map_svg = f.read()

soup = bs(map_svg)
paths = soup.select('path[id]')
print(paths)

colors = ['#F1EEF6', '#D4B9DA', '#C994C7', '#DF65B9', '#DD1C77', '#980043']

for p in paths:
    if p['id'] == 'Yeongdeungpo-gu_1_':
        p['id'] = 'Yeongdeungpo-gu'
        
    count = data_dict[p['id']]
    
    if cont > 250: color_index = 5
    elif cont > 200: color_index = 4
    elif cont > 150: color_index = 3
    elif cont > 100: color_index = 2
    elif cont > 50: color_index = 1
    else : cololr_index = 0
    
    p['fill'] = colors[color_index]
    print(p)

