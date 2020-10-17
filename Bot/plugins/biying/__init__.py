# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 20:34
# @Author  : P19Y0UN9
# @File    : biying.py
# @Software: PyCharm
__plugin_name__ = '每日壁纸'
__plugin_usage__ = r"""
必应每日壁纸
发送：壁纸
"""

from urllib.request import urlretrieve

import requests
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from Bot.plugins.biying.data_source import get_wall
from aiocqhttp import MessageSegment


@on_command('wall', aliases=('每日壁纸','壁纸'))
async def oneWord(session: CommandSession):
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    res = requests.get(url=url, headers=headers)
    text = res.json()

    result = 'https://www.bing.com' + text['images'][0]['url']
    image_url = result
    urlretrieve(image_url, 'D:/Desktop/项目仓库/pic/Bing.jpg')  # 将什么文件存放到什么位置
    seq = MessageSegment.image("D:/Desktop/项目仓库/pic/Bing.jpg")
    await session.send(seq)


@on_natural_language(keywords={'壁纸'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'wall')