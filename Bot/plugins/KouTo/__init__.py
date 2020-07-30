# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 13:59
# @Author  : P19Y0UN9
# @File    : KouTo.py
# @Software: PyCharm
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand

from Bot.plugins.KouTo.data_source import get_KouTo

__plugin_name__ = '口吐莲花'
__plugin_usage__ = r"""
祖安机器人
发送：骂/骂我/口吐莲花
支持自然语言【例】你再骂？！
"""

@on_command('KouTo', aliases=('口吐莲花','骂我','骂'))
async def oneWord(session: CommandSession):
    To_report = await get_KouTo()
    await session.send(To_report)

@on_natural_language(keywords={'口吐莲花','骂','滚','傻逼','爬','艹','操','cnm','尼玛'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'KouTo')