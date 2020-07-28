# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 20:34
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm

async def get_wall():
    import requests
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    res = requests.get(url=url, headers=headers)
    text = res.json()

    result = 'https://www.bing.com' + text['images'][0]['url']
    return result