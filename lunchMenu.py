import json
import datetime
import requests

def getLunchMenu(dateToday : str):
    lunchMenuURL = "https://open.neis.go.kr/hub/mealServiceDietInfo"
    lunchParams = dict(
        Type='json',
        ATPT_OFCDC_SC_CODE='D10',
        SD_SCHUL_CODE='7240272',
        MMEAL_SC_CODE='2',
        MLSV_YMD=dateToday
    )
    try:
        res = requests.get(url = lunchMenuURL, params = lunchParams)
        resJSON = res.json()
        lunchMenu: str = resJSON['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
    except KeyError:
        return 'noLunch'
    transTable = lunchMenu.maketrans({
        '(': ' ', # 왼쪽은 치환하고 싶은 문자, 오른쪽은 새로운 문자
        ')': ' ',
        '1': ' ',
        '2': ' ',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': ' ',
        '8': ' ',
        '9': ' ',
        '0': ' ',
        '.': ' ',
    })
    lunchMenu = lunchMenu.replace('<br/>', '')
    lunchMenu = lunchMenu.translate(transTable)

    return lunchMenu

lunchData = getLunchMenu(datetime.datetime.today().strftime('%Y%m%d'))
print(lunchData)