from pandas import DataFrame as df
from matplotlib import font_manager
import numpy as np

# 글꼴 폴더 확인
font_manager._rebuild()

# 목록을 리스트로 가져온다.
flist = font_manager.findSystemFonts()
print(flist[:5])
print('-'*40)

# 리스트로 정보조회
font_list = []
for v in flist:
    fprop = font_manager.FontProperties(fname=v)
    font_list.append({'name':fprop.get_name(), 'file':fprop.get_file()})
    
print(font_list[:5])
print('-'*40)
