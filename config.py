# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 16:47
# @Author  : P19Y0UN9
# @File    : config.py
# @Software: PyCharm

from nonebot.default_config import *

from nonebot.default_config import *

from datetime import timedelta


# 表示“超级用户”，也就是机器人的主人。超级用户拥有最高的权限。在这里填入你的 QQ 号。
SUPERUSERS = { 1924451951 }
# 表示命令的前缀，例如假如命令叫 `天气`，那么只有用户在输入 `/天气` 时候才会触发命令。
COMMAND_START = { '' }
# 机器人昵称，设定后 "@机器人 天气" 和 "Merry 天气" 效果相同。
NICKNAME = { 'Saiki', 'saiki', '齐木' }
# 表示一条命令的超时（没有用户输入）时间。
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=2)
# 服务器和端口
HOST = '127.0.0.1'
PORT = 9244

# 关闭调试输出，提升性能。
DEBUG = False


