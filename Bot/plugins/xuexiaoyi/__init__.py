# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 11:24
# @Author  : P19Y0UN9
# @File    : xuexiaoyi.py
# @Software: PyCharm
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

from Bot.plugins.xuexiaoyi.data_source import get_xuexiaoyi

__plugin_name__ = '搜题'
__plugin_usage__ = r"""
适用于慕课，智慧树，学习通等题库
发送：搜题  [题目]
"""


@on_command('xuexiaoyi', aliases=('搜题'))
async def weather(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（question），如果当前不存在，则询问用户
    question = session.get('question', prompt='请问你要搜什么题呢？')
    # 获取答案
    xuexiaoyi_report = await get_xuexiaoyi(question)
    # 向用户发送答案
    result=''
    count=0
    for ans in xuexiaoyi_report:
        if count == 3:
            break
        result=result+'问题：'+ans['q']+'\n答案：'+ans['a']+'\n\n'
        count=count+1
    await session.send(result)


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@weather.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将题目跟在命令名后面，作为参数传入
            # 例如用户可能发送了：搜题 ****
            session.state['question'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的题目（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要搜索的题目不能为空哦！')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg

# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'搜题'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'xuexiaoyi')