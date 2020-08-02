# # -*- coding: utf-8 -*-
# # @Time    : 2020/8/2 17:21
# # @Author  : P19Y0UN9
# # @File    : acount.py
# # @Software: PyCharm
#
#
# file='acounts.txt'
# async def get_ac(userId):
#     for line in open("file", "r"):  # 设置文件对象并读取每一行文件
#         if line.find(userId) != -1:
#             return line
#     return -1
#
# async def add_ac(userId,txtId,txtMM):
#     with open(file, "w") as f:
#         f.write(userId,txtId,txtMM)  # 自带文件关闭功能，不需要再写f.close()