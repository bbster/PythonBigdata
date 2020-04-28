import requests
import json
from pandas import DataFrame as df
from matplotlib import pyplot as plt
from matplotlib.image import imread

simple_text_url = 'http://192.168.0.96/simple.json'

r = requests.get(simple_text_url)

print(r)
print('-'*40)

if r.status_code != 200:
    print('[%d Error] %s' %(r.status_code, r.reason))
    quit()


result = json.loads(r.text)
print(result)
print('-'*40)

data = df([result])
print(data)
print('-'*40)

img = imread(data.loc[0, 'img'])


plt.imshow(img)
plt.axis('off')
ply.show()
