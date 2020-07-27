# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 12:33
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm
import requests

token='gsg8JGlHtbawMTX6mZE2QDkxko2UhtRNmzPvRQBBOJvRKqtfnzoKW3l1EN8y'

async def get_xuexiaoyi(question:str)->str:
    headers = {
        "Host": "app.51xuexiaoyi.com",
        "token": token,
        "device": "Auhqehd3s6Ml6mXky_5dV-Uv4zsdXeUYY7wKFktkH1ag",
        "platform": "android",
        "app-version": "1.0.6",
        "t": "1592904062239",
        "s": "e6a47dea8298225b1e9a9366bead8083",
        "content-type": "application/json;charset=utf-8",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.11.0"
    }
    url = "https://app.51xuexiaoyi.com/api/v1/searchQuestion?keyword=" + question
    res = requests.post(url, headers=headers)
    r = res.json()  # 返回的内容本身就是json
    if r['code']==200:
        data = r['data']
    else:
        data = r['msg']
    return data