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
        await bot.send_group_msg(group_id=ctx['group_id'],message='“也许在此时停下脚步并不是好的选择，但却是我们必须做出的选择。”\n小鹅不知道还能陪大家多久了，说不定就是这两天了。\n也许未来会有机会重新上线。\n下面是酷Q的官方说明https://docs.cqp.cc/about/FAQ/\n看功能艾特我说“功能”')