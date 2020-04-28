import numpy
import pandas as pd
from pandas import DataFrame
from pandas import ExcelFile
from matplotlib import pyplot
import datetime as dt


xlsx = ExcelFile('data/dataset2017.xlsx')
df = xlsx.parse(xlsx.sheet_names[0])

# gen_year:
gen_year = df.filter(['h12_g3', 'h12_g4'])
print(gen_year)
print(type(gen_year))
print('-'*40)

# df_gen_year 1
df_gen_year = gen_year.rename(columns={'h12_g3':'성별', 'h12_g4':'태어난년도'})

# df_gen_year 2 / 성별 숫자 -> 남자,여자
df_gen_year['성별'] = numpy.where(df_gen_year['성별'] == 1, '남자', '여자')


# df_gen_year 3 / 연령대 추가
df_gen_year['연령대'] = (dt.datetime.now().year - df_gen_year['태어난년도']) //10 *10
print(df_gen_year)
print('-'*40)

# df_gen_year.isna().sum()
print(df_gen_year.isna().sum())
print('-'*40)

# df_age_gen_count: / 성별대로 카운트
df_age_gen_count = df_gen_year.groupby(['성별', '연령대'], as_index=False).count()

# sort
df_age_gen_sort = df_age_gen_count.sort_index()
print(df_age_gen_sort)
print('-'*40)

# df_age_gen / 태어난년도 rename 명
df_age_gen = df_age_gen_sort.rename(columns={'태어난년도':'명'})
print(df_age_gen)
print('-'*40)

pv_age_gen = df_age_gen.pivot('연령대', '성별', '명')
print(pv_age_gen)
print('-'*40)

index_after = {}
for i in list(pv_age_gen.index):
    index_after[i] = '%d대' %i
    
pv_age_gen.rename(index=index_after, inplace=True)
print(pv_age_gen)

pyplot.rcParams['font.family'] = 'Malgun Gothic'
pyplot.rcParams['font.size'] = 17
pyplot.rcParams['figure.figsize'] = (20,10)

pv_age_gen.plot.bar(rot=0)
pyplot.title('성별과 연령대별 분포')
pyplot.grid()
pyplot.xlabel('연령대')
pyplot.ylabel('성별')

pyplot.show()
