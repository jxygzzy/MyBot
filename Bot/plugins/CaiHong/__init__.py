# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 14:05
# @Author  : P19Y0UN9
# @File    : __init__.py
# @Software: PyCharm

from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand

from Bot.plugins.CaiHong.data_source import get_Kua

__plugin_name__ = '彩虹屁'
__plugin_usage__ = r"""
夸你一下
发送：夸/彩虹屁
支持自然语言【例】快夸爷
"""

@on_command('Kua', aliases=('彩虹屁','夸我','夸'))
async def oneWord(session: CommandSession):
    Kua_report = await get_Kua()
    await session.send(Kua_report)

@on_natural_language(keywords={'夸','彩虹屁'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'Kua')