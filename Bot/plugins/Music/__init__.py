# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 17:21
# @Author  : P19Y0UN9
# @File    : Music.py
# @Software: PyCharm
__plugin_name__ = '点歌'
__plugin_usage__ = r"""
分享网易云音乐链接
发送：点歌 [歌曲名/歌手名]
"""

from aiocqhttp import MessageSegment
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

from Bot.plugins.Music.data_source import get_music


@on_command('music', aliases=('点歌','来一首','我想听'))
async def weather(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    song = session.get('song', prompt='你想听什么歌呢？')
    # 获取城市的天气预报
    song_report = await get_music(song)
    # 向用户发送天气预报
    mus=MessageSegment.music(163,song_report)
    MessageSegment
    await session.send(mus)


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@weather.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['song'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要查询的歌曲名不能为空哦！')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg

# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'点歌','来一首','我想听'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'music')