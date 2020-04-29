import json
import requests
from pandas import DataFrame
from matplotlib import pyplot

json_list_url = 'http://192.168.0.96/student.json'

r = requests.get(json_list_url)

if r.status_code != 200:
    print('[%d Error] %s' %(r.status_code, r.reason))
    quit()
    
result = json.loads(r.text)
print(result)
print(type(result))
print('-'*40)

df = DataFrame(result['student'])
print(df)
print('-'*40)

def test(*args):
    print(type(result), result)
    
test(result)
