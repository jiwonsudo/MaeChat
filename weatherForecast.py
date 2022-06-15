import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import json
import requests
import datetime

dateToday = datetime.datetime.today().strftime('%Y%m%d')
timeNow = datetime.datetime.now().strftime('%H%M')

weatherUrl = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0'
weatherParams = dict(
    ServiceKey = '4O+F9rGkT8FJUZ0uBfKYYrkfTJPn4Sigu54vxxbvn/tA8u+G0tM5pnwgS81EU2Oo7XaeSF3UAL0vITZWyD+KiA==',
    pageNo = '1',
    numOfRows = '1',
    dataType = 'JSON',
    base_date = dateToday,
    base_time = '0900',
    nx = '88', # Taejeon-1-dong
    ny = '92'
)

res = requests.get(url = weatherUrl, params = weatherParams)
print(res.content)