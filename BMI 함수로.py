
import requests
import json
url = 'https://api.odcloud.kr/api/15077586/v1/centers'
param={'page':1, 'perPage':10,
       'serviceKey': 'LROuCFeMjOxxJPV+ivgk2Zj+2PMI+L8teZ/0kreP8EbbdeNeAHkRTtwbwS6OikOHaK7YV86lVLihqapyoIhhiw=='}

reponse = requests.get(url,params=param)
#print(reponse.text)

a=json.loads(reponse.text)
print(a['currentCount'])