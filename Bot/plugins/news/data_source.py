# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 15:37
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm

import re  # 正则表达式，进行文字匹配
from bs4 import BeautifulSoup  # 网页解析，获取数据
import urllib.request, urllib.error

findTitle = re.compile(r'target="_blank">(.*?)</a>')

url='http://top.baidu.com/buzz?b=1&c=513&fr=topbuzz_b42_c513'

async def get_news():
    data=[]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(request)
    html = res.read()
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('a', class_="list-title"):
        # print(item)
        tilte = re.findall(findTitle, str(item))[0]
        data.append(tilte)
    result=''
    for i in range(0,10):
        result =result+str(i+1)+'.'+data[i]+'\n'
    result = result+"详情链接：top.baidu.com/buzz?b=1"
    return result
