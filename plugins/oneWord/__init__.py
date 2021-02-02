# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 19:24
# @Author  : P19Y0UN9
# @File    : oneWord.py
# @Software: PyCharm
import random
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand

from .data_source import get_oneWord

__plugin_name__ = '一言'
__plugin_usage__ = r"""
发送一句名言或热评
发送：一言
"""

@on_command('oneWord', aliases=('一言'))
async def oneWord(session: CommandSession):
    type = chr(random.randint(97, 107))
    oneWord_report = await get_oneWord(type)
    await session.send(oneWord_report)

