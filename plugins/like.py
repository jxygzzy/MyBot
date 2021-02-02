# from aiocqhttp import MessageSegment
# from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
#
# __plugin_name__ = '赞我'
# __plugin_usage__ = r"""
# 发送好友赞。
# 为防止违法行为，框架取消该功能
# """
#
#
# @on_command('like', aliases=('赞我', '赞', '名片赞'))
# async def like(session: CommandSession):
#     try:
#         await session.bot.send_like(self_id=session.event.self_id,user_id=session.event.user_id,times=10)
#         await session.send(MessageSegment.text('赞好了~'))
#     except Exception as e:
#         await session.send(MessageSegment.text('赞失败了，联系主人修复吧~'))
#         raise Exception(e)
#
#
# @on_natural_language(keywords={'赞'})
# async def _(session: NLPSession):
#     # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
#     return IntentCommand(90.0, 'like')
