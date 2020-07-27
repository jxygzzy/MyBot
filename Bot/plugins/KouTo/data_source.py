# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 13:59
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm

import requests

url='https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'

async def get_KouTo():
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    res = requests.get(url=url,headers=headers)
    result = res.text
    return result