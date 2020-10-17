# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 15:36
# @Author  : P19Y0UN9
# @File    : news.py
# @Software: PyCharm
from aiocqhttp import MessageSegment
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand

from Bot.plugins.news.data_source import get_news

__plugin_name__ = '新闻资讯'
__plugin_usage__ = r"""
实时热点新闻
发送：新闻/新闻资讯
支持自然语言【例】给爷来条新闻
"""

@on_command('news', aliases=('新闻','新闻资讯'))
async def oneWord(session: CommandSession):
    news_report = await get_news()
    await session.send(news_report)
    share=MessageSegment.share('https://news.163.com/rank/','网易新闻排行榜','http://static.ws.126.net/cnews/img10/channelLogo2010/img_xwphb.jpg')
    await session.send(share)


@on_natural_language(keywords={'新闻'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'news')