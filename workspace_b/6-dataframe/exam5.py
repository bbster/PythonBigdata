from pandas import ExcelFile as ef

xls = ef('../data/children_house.xlsx')
print(xls)
print(type(xls))
print('-'*40)

# 엑셀 파일의 sheet이름에 대한 리스트
print(xls.sheet_names)
print('-'*40)

# 가져오고자 하는 sheet 이름을 지정하여 데이터프레임으로 변환
data = xls.parse(sheet_name=0)
print(data)
