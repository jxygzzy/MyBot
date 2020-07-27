# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 23:55
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm

import requests
import re
from bs4 import BeautifulSoup

findImfor = re.compile(r'<div class="well">(.*?)</div>')

url='http://kw.fudan.edu.cn/cndbpedia/search/'

async def get_baike(qeury):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    params={
        "mention":qeury.encode('utf-8')
    }
    res=requests.get(url=url,headers=headers,params=params)
    html=res.text
    soup = BeautifulSoup(html,"html.parser")
    try:
        item = soup.find_all('div', class_='well')[0]
        item=re.findall(findImfor,str(item))[0]
        item=re.sub('<a href="./\?mention=.*?">','',item)
        item=re.sub('</a>','',item)
        item=re.sub('<.*?br.*?>','',item)
        # item=re.sub('</br>','',item)
    except:
        return "***暂未找到该词条***"
    return item