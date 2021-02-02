__plugin_name__ = '涩图 [hidden]'
__plugin_usage__ = r"""
随机发送setu
"""

import json

import requests

from io import BytesIO
from PIL import Image
from nonebot import on_command, CommandSession
from aiocqhttp import MessageSegment

UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"

headers = {
    "user-agent": UserAgent
}

proxies = {
    "http": "http://www.pixiv.net",
}


@on_command('setu', aliases='色图')
async def setu(session: CommandSession):
    url = "https://api.lolicon.app/setu/?apikey=0961535560170e964e4689&r18=2&size1200=true"

    response = requests.get(url=url, headers=headers)
    data = json.loads(response.text)['data'][0]
    msg = "pid:" + str(data['pid']) + "\n" + "title:" + data['title'] + "\n" \
          + "author:" + data['author'] + "\n" + "url:" + data['url'] + "\n" + \
          "tags:" + str(data['tags'])
    # print(msg)
    await session.send(MessageSegment.text(msg))
    # imgUrl = data['url']
    # imgresp=requests.get(imgUrl,headers=headers,proxies=proxies)
    # img=Image.open(BytesIO(imgresp.content))
    # img.save('onebot/img/setu.png')
    # seq = MessageSegment.image('img/setu.png')
    # await session.send(seq)
