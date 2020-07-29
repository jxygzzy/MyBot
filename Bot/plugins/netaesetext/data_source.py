# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 21:54
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm
async def get_text():
    import requests
    url = 'http://api.heerdev.top:4995/nemusic/random'

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    }

    res = requests.get(url=url, headers=header).json()
    return res['text']