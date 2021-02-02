# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 13:40
# @Author  : P19Y0UN9
# @File    : TianGou.py
# @Software: PyCharm
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand

from plugins.TianGou.data_source import get_Tian

__plugin_name__ = '舔狗日记'
__plugin_usage__ = r"""
发送一条舔狗日记
发送：舔/舔狗/舔狗日记
支持自然语言【例】给爷来条舔狗日记
"""

@on_command('Tian', aliases=('舔狗','舔','舔狗日记'))
async def oneWord(session: CommandSession):
    Tian_report = await get_Tian()
    await session.send(Tian_report)

@on_natural_language(keywords={'舔狗','日记','舔'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'Tian')