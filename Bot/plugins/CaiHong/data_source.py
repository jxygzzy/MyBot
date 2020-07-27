# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 14:05
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm
import requests

url='https://chp.shadiao.app/api.php'

async def get_Kua():
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    res = requests.get(url=url,headers=headers)
    result = res.text
    return result