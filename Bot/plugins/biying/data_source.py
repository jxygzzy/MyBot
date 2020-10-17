# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 20:34
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm

import os
from urllib.request import urlretrieve

import requests


async def get_wall():
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    res = requests.get(url=url, headers=headers)
    text = res.json()

    result = 'https://www.bing.com' + text['images'][0]['url']
    image_url = result
    urlretrieve(image_url, 'D:/Desktop/项目仓库/pic/Bing.jpg')  # 将什么文件存放到什么位置
    return True
