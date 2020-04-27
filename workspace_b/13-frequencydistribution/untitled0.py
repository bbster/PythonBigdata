import numpy as np
import pandas as pd
from pandas import DataFrame as df
from matplotlib import font_manager

csv_file = pd.read_excel("시도별_월별_교통사고_20200327151519.xlsx")

#print(csv_file)
#print(type(csv_file))

# Dataframe에서 특정 데이터 추려냄
#csv_loc = csv_file.loc[:,['서울','부산','대구','인천']]
index = ['서울','부산','대구']
print(type(index))
#csv_data = csv_file.loc[index]
#print(csv_data)


# index month / columns 시도
# cv1 = csv_file.pivot(columns='시도별', values=)
# print(cv1)