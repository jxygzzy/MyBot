# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 23:29
# @Author  : P19Y0UN9
# @File    : __init__.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 22:52
# @Author  : P19Y0UN9
# @File    : __init__.py
# @Software: PyCharm
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from Bot.plugins.t_schedule.data_source import get_tSchedule

__plugin_name__ = '明日课程表'
__plugin_usage__ = r"""
发送[计科195]第二天课程表
发送：明日课程表/明日课程

"""




@on_command('tSchedule', aliases=('明日课程','明日课程表','明天上课','明日课'))
async def Schedule(session: CommandSession):
    schedule_report = await get_tSchedule()
    await session.send(schedule_report)

# @on_natural_language(keywords={'课程','课程表','上课','课'})
# async def _(session: NLPSession):
#     # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
#     return IntentCommand(90.0, 'Schedule')