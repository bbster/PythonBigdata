import numpy
import pandas as pd
from pandas import DataFrame
from pandas import ExcelFile
from matplotlib import pyplot
import datetime as dt


xlsx = ExcelFile('data/dataset2017.xlsx')
df = xlsx.parse(xlsx.sheet_names[0])


# 연도 불러오기
year = df.filter(['h12_g4'])


# 컬럼명 변경
df_year = year.rename(columns={'h12_g4':'태어난년도'})


# 나이 추가
df_year['나이'] = dt.datetime.now().year - df_year['태어난년도']


# 연령대 추가 
df_year['연령대'] = (df_year['나이'] // 10) * 10
print(df_year)

# df.year.isna().sum()
print(df_year.isna().sum())

vcount = df_year['연령대'].value_counts()
df_age_band = DataFrame(vcount)
print(df_age_band)

df_age_band_sort = df_age_band.sort_index()
print(df_age_band_sort)

index_after = {}
for i in list(df_age_band_sort.index):
    index_after[i] = "%d대" %i
    
df_age_band_sort.rename(index=index_after, inplace=True)
print(df_age_band_sort)

pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['font.size'] = 17
pyplot.rcParams['figure.figsize'] = (20,10)

df_age_band_sort.plot.bar(rot=0)
pyplot.title('연령대 분포')
pyplot.grid()
pyplot.xlabel('연령대')
pyplot.ylabel('명')

for i ,v in enumerate(list(df_age_band_sort['나이'])):
    txt = '%d명' %v
    pyplot.text(i, v, txt, fontsize=14, color='blue', 
                horizontalalignment='center')
pyplot.show()
