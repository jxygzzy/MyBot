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
发送[计科195/196]第二天课程表
发送：明日课程表/明日课程

"""

# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('tSchedule', aliases=('明日课程', '明日课程表', '明日上课'))
async def _(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    Class = session.get('Class', prompt='你想查询哪个班级的课程呢？\n（发送:195/196）')
    # 获取城市的天气预报
    Schedule_report = await get_tSchedule(Class)
    # 向用户发送天气预报
    await session.send(Schedule_report)


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@_.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['Class'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要查询的班级名称不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg