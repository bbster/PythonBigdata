from pandas import DataFrame as df
from pandas import ExcelFile

xlsx = ExcelFile('data/children_house.xlsx')
df = xlsx.parse(xlsx.sheet_names[0])
print(df)
print('-'*40)

children_house = df.rename(index=df['지역'])
print(children_house)
print('-'*40)

children_house.drop(['지역'], axis=1, inplace=True)
print(children_house)
print('-'*40)
