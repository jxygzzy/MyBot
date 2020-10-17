# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 21:54
# @Author  : P19Y0UN9
# @File    : netaesetext.py
# @Software: PyCharm


__plugin_name__ = '网抑云语录'
__plugin_usage__ = r"""
发送一句网抑云评论
发送：网抑云
"""

from nonebot import on_command, CommandSession

from Bot.plugins.netaesetext.data_source import get_text


@on_command('neteasetext', aliases=('网抑云','网易云','到点了','网易云语录','网抑云语录'))
async def text(session: CommandSession):
    text_report = await get_text()
    await session.send(text_report)
