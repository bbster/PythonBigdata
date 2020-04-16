from packages.image.io_file import imgRead
from packages.image.io_file.imgRead import pngRead as pr
from packages.image.io_file.imgRead import jpgRead as jr


'''
from 폴더.파일 or 폴더 파일 클래스명/함수명
import 클래스/함수명
내장된 패키지 같은경우 import만 사용해도 된다. ex)numpy, pandas 등등
'''

imgRead.pngRead()
imgRead.jpgRead()
print('-'*30)
#pngRead()  # as로 별명 붙여주면 원래 이름 사용불가
#jpgRead()
print('-'*30)
pr()
jr()
print('-'*30)
