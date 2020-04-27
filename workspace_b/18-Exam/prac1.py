import numpy as np
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
from matplotlib import font_manager

df = pd.read_excel("dataset2017.xlsx")


plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['font.size'] = 16
plt.rcParams['figure.figuresize'] = (16,8)


# 월급 차이를 계산하기 위한 값이 뭔지 모르겠음
# 타이틀
plt.title('성별에 따른 평균 월급 차이')

# 라벨
plt.xlabel('index')
plt.ylabel('price')

# 막대그래프
plt.bar(df['index'], df['price'], color=['red','blue'])

plt.show()
