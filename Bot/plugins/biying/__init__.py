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
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from Bot.plugins.biying.data_source import get_wall


@on_command('wall', aliases=('每日壁纸','壁纸'))
async def oneWord(session: CommandSession):
    wall_report = await get_wall()
    await session.send('[CQ:share,url=%s,title=必应每日壁纸]'%wall_report)

@on_natural_language(keywords={'壁纸'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'wall')