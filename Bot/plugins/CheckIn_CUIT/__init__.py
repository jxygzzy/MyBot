# # -*- coding: utf-8 -*-
# # @Time    : 2020/8/2 17:11
# # @Author  : P19Y0UN9
# # @File    : CheckIn_CUIT.py
# # @Software: PyCharm
#
#
# from Bot.plugins.CheckIn_CUIT.acount import get_ac
# from Bot.plugins.CheckIn_CUIT.data_source import checkIn
# import nonebot
#
# bot=nonebot.get_bot()
#
# @bot.on_message('private')
# async def daka(ctx):
#     if ctx['raw_message']=='打卡':
#     user=ctx['user_id']
#     txt=get_ac(user)
#     if txt == -1:
#         await bot.send_private_msg()(user_id=user, message='未找到该账号信息，请私聊添加')
#         return
#     txt=str(txt)
#     data=txt.split()
#     print(data)
#     # msg=checkIn(data[1],data[2])
#     # await bot.send_private_msg(user_id=user,message=msg)





