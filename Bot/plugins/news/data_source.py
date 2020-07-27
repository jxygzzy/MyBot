# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 15:37
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm

import requests


url='http://c.m.163.com/nc/article/headline/T1348649580692/0-40.html'
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
async def get_news():

    res=requests.get(url=url,headers=headers)
    text=res.json()
    count=0;
    result=''
    for i in text['T1348649580692']:
        result=result+i['title']+'\n'
        result=result+i['url']+'\n'
        count=count+1
        if count==10:
            break
    return result