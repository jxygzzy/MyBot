# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 17:21
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm
async def get_music(song):
    import requests

    url = 'http://47.112.23.238/Music/getMusicList'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
        "Accept-Encoding": "gzip, deflate"
    }
    data = {
        "musicName": song,
        "type": "netease",
        "number": "5"
    }

    res = requests.post(url=url, headers=headers, data=data)
    text=res.json()
    result=''
    for data in text['data']:
        result=result+data['title']+"-"+data['author']+":http://music.163.com/#/song?id="+data['id']+'\n'
    return result