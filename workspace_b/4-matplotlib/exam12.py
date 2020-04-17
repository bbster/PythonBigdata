from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np

member_IDs = 'm01', 'm02', 'm03', 'm04',
ex_before = 27, 35, 40, 33  # 운동 시작전
ex_after = 30, 38, 42, 37  # 운동 시작후

mpl.rcParams['font.family'] = 'Malgun Gothic'

mem_num = len(member_IDs)
index = np.arange(mem_num)
#plt.bar(index, ex_before)
#plt.show()

# 막대의 색상 지정
colors = 'r', 'g', 'b', 'c'
#plt.bar(index, ex_before, width=0.6, color=colors, tick_label=member_IDs)
#plt.show()

# 가로 막대 출력
#plt.barh(index, ex_before, height=0.4, color=colors, tick_label=member_IDs)
#plt.show()

# 막대바를 두개 같이 출력하기
# align = 'edge' : 막대그래프를 한쪽으로 치우치게 할수있다.
barwidth = 0.4
plt.bar(index, ex_before, width=barwidth, color='c',
        label='before', align='edge')
plt.bar(index+barwidth, ex_after, width=barwidth, color='m',
        label='after', align='edge')
plt.show()

# 범례 출력
plt.legend()
# x축 눈금 표시
plt.xticks(index+barwidth, member_IDs)
plt.xlabel('회원 ID')
plt.ylabel('윗몸일으키기 횟수')
plt.title('운동 시작전과 후의 근지구력(복근) 변화 비교')
plt.show()
