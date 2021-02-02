# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 13:41
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm
import requests

url='https://api.ixiaowai.cn/tgrj/'

async def get_Tian():
    result = ''
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    res = requests.get(url=url,headers=headers)
    result = res.text
    return result