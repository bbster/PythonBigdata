from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np

city = ['서울','인천','대전','대구','울산','부산','광주']
lat = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16]
lng = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85]
pop_den = [6154, 2751, 2839, 2790, 1099, 4454, 2995]


mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = 'False'

# 데이터별로 마커의 크기와 색상 지정
colors = 'r', 'g', 'b', 'c', 'm', 'k', 'y'
size = np.array(pop_den) * 0.5
plt.scatter(lng, lat, s=size, c=colors, alpha=0.5)
plt.xlabel('경도')
plt.ylabel('위도')
plt.title('지역병 인구밀도(2017)')
for x,y,z in zip(lng,lat,city):
    plt.text(x, y, z)

plt.show()
print(list(zip(lng,lat,city)))
