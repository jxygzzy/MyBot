# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 16:46
# @Author  : P19Y0UN9
# @File    : bot.py
# @Software: PyCharm
from os import path
import nonebot
import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), '', 'plugins'),
        'Bot.plugins'
    )
    nonebot.run()