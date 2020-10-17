# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 17:16
# @Author  : P19Y0UN9
# @File    : call.py
# @Software: PyCharm
import nonebot
from aiocqhttp import MessageSegment
from nonebot import on_command, CommandSession, on_notice

bot = nonebot.get_bot()

@bot.on_message('group')
async def call(ctx):
    if ctx['raw_message']=='小鹅'or ctx['raw_message']=='鹅砸':
        await bot.send_group_msg(group_id=ctx['group_id'],message='干嘛呀！看功能艾特我说“功能”')
    if ctx['raw_message']=='牛雄赞':
        seq = MessageSegment.image("D:/Desktop/项目仓库/pic/nxz.jpg")
        rec = MessageSegment.record("D:/Desktop/项目仓库/rec/nxz.amr")
        await bot.send_group_msg(group_id=ctx['group_id'],message=seq)
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='约吗？' or ctx['raw_message']=='约吗':
        seq = MessageSegment.image("D:/Desktop/项目仓库/pic/wx.jpg")
        await bot.send_group_msg(group_id=ctx['group_id'],message=seq)
    if ctx['raw_message']=='羊叫':
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/小羊.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='猫叫':
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/小猫.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='我太难了':
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/我太难了.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='班门弄斧' or ctx['raw_message']=='大威天龙':
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/大威天龙.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='是否有很多问号' or ctx['raw_message']=='小朋友':
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/小朋友你是否有很多问号.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='给爷爬' or ctx['raw_message']=='爬':
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/给爷爬.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='狗叫' or ctx['raw_message']=='我旺不旺':
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/狗叫.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='狼叫' :
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/狼叫.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='老虎' :
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/老虎.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='马叫' :
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/马叫.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='猫咪':
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/猫咪.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='鸡叫' :
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/母鸡.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='牛叫':
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/牛叫.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='牵丝戏' :
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/牵丝戏.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='鸭子' or ctx['raw_message']=='鸭叫':
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/鸭叫amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='鹰叫' or ctx['raw_message']=='鹰':
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/鹰叫.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)
    if ctx['raw_message']=='猪叫' or ctx['raw_message']=='居叫':
        rec=MessageSegment.record("D:/Desktop/项目仓库/rec/猪叫.amr")
        await bot.send_group_msg(group_id=ctx['group_id'], message=rec)