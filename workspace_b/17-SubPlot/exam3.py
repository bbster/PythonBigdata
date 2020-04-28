import numpy
from pandas import DataFrame
from matplotlib import pyplot
from pandas import read_excel

df = read_excel('data/시도별_월별_교통사고_20200327151519.xlsx')
#print(df)
print('-' * 30)

df_traffic = df.filter(['시도별(1)', '2017. 01','2017. 02','2017. 03',
                        '2017. 04','2017. 05','2017. 06','2017. 07',
                        '2017. 08','2017. 09','2017. 10','2017. 11',
                        '2017. 12',])
#print(df_traffic)
print('-' * 30)

df_traffic.drop(0, inplace=True)
#print(df_traffic)
print('-' * 30)

df_traffic = df_traffic.rename(index=df_traffic['시도별(1)'])\
            .drop('시도별(1)', axis=1)
#print(df_traffic)
print('-' * 30)

dic_month = {'2017. 01':'1월', '2017. 02':'2월', '2017. 03':'3월', 
             '2017. 04':'4월', '2017. 05':'5월', '2017. 06':'6월', 
             '2017. 07':'7월', '2017. 08':'8월', '2017. 09':'9월', 
             '2017. 10':'10월', '2017. 11':'11월', '2017. 12':'12월'}
df_traffic.rename(columns=dic_month, inplace=True)
#print(df_traffic)
print('-' * 30)

df = df_traffic.T
#print(df)
print('-' * 30)

df.drop(['경기','강원','충북','충남','전북','전남','경북','경남','제주',
         '광주','대전','울산','세종'], inplace=True, axis=1)
print(df)
print('-' * 30)

pyplot.rcParams['font.family'] = 'Malgun Gothic' 
pyplot.rcParams['font.size'] = 16
pyplot.rcParams['figure.figsize'] = (20, 10) 

fig = pyplot.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

fig.suptitle('2017년 교통사고 현황', fontsize=28, color='#00ff00')
fig.subplots_adjust(wspace=0.2, hspace=0.3)

df.plot(ax=ax1, color=['#66ff00','#ff6600','#ff0000','#0000ff'])
ax1.grid()
ax1.title.set_text('서울,부산,대구,인천의 2017년 교통사고 변화')
ax1.title.set_fontsize(24)
ax1.title.set_color('#ff0000')
ax1.set_xticks(list(range(0, 12)))
ax1.set_xticklabels(list(df.index), fontsize=12, color='#ff0000')
ax1.set(xlabel='월', ylabel='교통사고')
ax1.set_xlim([-0.5, 11.5])
ax1.set_ylim([0, 3500])

df.plot.bar(ax=ax2, rot=0, color=['#ff6600', 'green', 'cyan', 'blue'])
ax2.grid()
ax2.title.set_text('서울,부산,대구,인천의 2017년 교통사고 빈도')
ax2.title.set_fontsize(24)
ax2.title.set_color('blue')
ax2.set_xticks(list(range(0, 12)))
ax2.set_xticklabels(list(df.index), fontsize=12, color='blue')
ax2.set(xlabel='월', ylabel='교통사고')

df['서울'].plot.pie(ax=ax3, labels=df.index, autopct='%.1f%%',
                  textprops={'color':'#000000', 'fontsize':12})
ax3.title.set_text('서울의 월별 교통사고 비율')
ax3.set(ylabel=None)
ax3.legend(labels=df.index, title='범주', bbox_to_anchor=(1, 1))

df.plot.scatter(x='서울', y='부산', ax=ax4, color='#ff6600',
                label='교통사고', marker='X')
ax4.title.set_text('서울과 부산의 교통사고 관계')
ax4.set(xlabel='서울', ylabel='부산')
ax4.grid()

pyplot.show()









