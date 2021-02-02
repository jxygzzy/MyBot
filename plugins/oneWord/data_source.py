# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 19:51
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm
import json

import requests
import re

async def get_oneWord(type):
    data=[]
    baseUrl = 'http://v1.hitokoto.cn'
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
        "c": type
    }
    response = requests.get(url=baseUrl, headers=header)
    text=json.loads(response.text)
    hitokoto = text['hitokoto']
    data.append(hitokoto)
    creator = text['from']
    data.append(creator)
    result = data[0]+'\t——'+'《'+data[1]+'》'
    return result