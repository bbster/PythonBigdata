import numpy as np
import pandas as pd
from pandas import DataFrame as df
from matplotlib import pyplot as plt
from matplotlib import font_manager

csv_file = pd.read_excel("시도별_월별_교통사고_20200327151519.xlsx")


df_traffic = csv_file.filter(['시도별','2017. 01','2017. 02','2017. 03'
                             ,'2017. 04','2017. 05','2017. 06','2017. 07'
                             ,'2017. 08','2017. 09','2017. 10','2017. 11','2017. 12'])

df_traffic.drop(0, inplace=True)

df_traffic = df_traffic.rename(index=df_traffic['시도별'])\
                .drop('시도별', axis=1)

dic_month = {'2017. 01': '1월', '2017. 02': '2월', '2017. 03': '3월',
             '2017. 04': '4월', '2017. 05': '5월', '2017. 06': '6월',
             '2017. 07': '7월', '2017. 08': '8월', '2017. 09': '9월',
             '2017. 10': '10월', '2017. 11': '11월', '2017. 12': '12월'}

df_traffic.rename(columns=dic_month, inplace=True)

df = df_traffic.T
print(df)

df.drop(['경기', '강원', '충북', '전북', '전남', '경북', '경남', '제주', '광주',
          '대전', '울산', '세종'], inplace=True, axis=1)


plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['font.size'] = 16
plt.rcParams['figure.figuresize'] = (16,8)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

df.plot(ax=ax1)
df.plot.bar(ax=ax2)
