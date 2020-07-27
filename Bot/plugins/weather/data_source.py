# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 17:11
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm
import json

import requests

async def get_weather_of_city(city: str) -> str:
    url = 'https://tianqiapi.com/api'
    APP_ID = "71396633"
    APP_Secret = "R2z1enJg"
    Version = "v6"
    City = city.encode('utf-8')
    headrs = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    params = {
        "appid": APP_ID,
        "appsecret": APP_Secret,
        "version": Version,
        "city": City
    }
    res = requests.get(url=url, headers=headrs, params=params)
    text = json.loads(res.text)
    # print(text)
    result = text['city'] + ':'+ text['week'] + text['update_time'] + ',' + text['wea']
    result = result + ' ' + text['win'] + ' 最低气温' + text['tem2'] + '摄氏度' + ' 最高气温' + text['tem1']
    result = result + '摄氏度' + ' 空气质量' + text['air_level'] + ' ' + text['air_tips']

    return result