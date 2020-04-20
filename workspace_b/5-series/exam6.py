from pandas import Series as sr
from pandas import date_range as dr

items = 10,20,30,40,50

s1 = dr(start='2020/1/1', periods=5)
column = sr(items, s1)
print(column)
