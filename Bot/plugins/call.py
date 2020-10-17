# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 17:16
# @Author  : P19Y0UN9
# @File    : call.py
# @Software: PyCharm
import nonebot
from nonebot import on_command, CommandSession, on_notice

bot = nonebot.get_bot()
@bot.on_message('group')
async def call(ctx):
    if ctx['raw_message']=='小鹅'or ctx['raw_message']=='鹅砸':
        await bot.send_group_msg(group_id=ctx['group_id'],message='干嘛呀！看功能艾特我说“功能”')