# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 17:41
# @Author  : P19Y0UN9
# @File    : scheduler.py
# @Software: PyCharm
from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from Bot.plugins.CheckIn_CUIT.data_source import checkIn

groupId = ['1079359698','887469565','141990544']

# @nonebot.scheduler.scheduled_job('cron', hour='22')#网抑云时间
# async def _():
#     bot = nonebot.get_bot()
#     #now = datetime.now(pytz.timezone('Asia/Shanghai'))
#     for group in groupId:
#         try:
#             await bot.send_group_msg(group_id=group,message=f'到点了,网抑[CQ:emoji,id=9729]')
#             await  bot.send_group_msg(group_id=group,message='[CQ:music,type=qq,id=213375591]')
#         except CQHttpError:
#             pass


@nonebot.scheduler.scheduled_job('cron', hour='19')#提醒填写收集表
async def _():
    bot = nonebot.get_bot()
    #now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await  bot.send_group_msg(group_id='887469565',
                                  message='https://docs.qq.com/form/page/Bd9bE84KHEk13tEO6f3pzSTV3a1kbV0NUoq93xC69Z2zKVDm2x5Bad3AJmm72HCkfg2PZsng2#/')
    except CQHttpError:
        pass

@nonebot.scheduler.scheduled_job('cron', hour='17')#提醒填写收集表
async def _():
    bot = nonebot.get_bot()
    #now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await  bot.send_private_msg(user_id='450174072',
                                  message='鹅砸提醒你运动啦！快去给居居打卡哦~')
    except CQHttpError:
        pass
