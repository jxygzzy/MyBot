# # -*- coding: utf-8 -*-
# # @Time    : 2020/10/16 21:25
# # @Author  : P19Y0UN9
# # @File    : __init__.py
# # @Software: PyCharm
# # -*- coding: gb2312 -*-
# # Author : Daisf
# # Date : 2020/4/30 22:45
# import json
# import re
# import requests
# from nonebot import on_command, CommandSession
# from nonebot import on_natural_language, NLPSession, IntentCommand
# @on_command('福建今日疫情', aliases=('福建今日疫情'))
# async def yiqing(session: CommandSession):
#     results = []
#     alist = []
#     url = "https://gwpre.sina.cn/interface/fymap2020_data.json?_=1588258367647&callback=dataAPIDAta"
#     headers = {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
#     r = requests.get(url, timeout=30, headers=headers)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     data = re.search("\(+([^)]*)\)+", r.text).group(1)
#     hjson = json.loads(data)
#     a = hjson['data']['list']
#     for i in a:
#         if i['ename'] == 'fujian':
#             city = i['city']
#             for j in city:
#                 name = j['name']  # 城市名称
#                 value = j['conNum']  # 累计确诊
#                 econNum = j['econNum']  # 现存确诊
#                 conadd = j['conadd']  # 今日确诊
#                 deathNum = j['deathNum']  # 累计死亡人数
#                 cureNum = j['cureNum']  # 累计治愈
#                 zerodays = j['zerodays']  # 零增长天数
#                 single_str = name + '\n' + "累计确诊：" + value + '\n' +   "现存确诊：" + econNum + '\n' +"今日确诊：" + conadd + '\n' +  "累计死亡人数：" + deathNum + '\n' + "累计治愈：" + cureNum +'\n' +  "零增长天数：" + zerodays + '\n'
#                 results.append(single_str)
#             break
#         else:
#             continue
#     for i in range(len(results)):
#         alist = alist + results[i]                        # 将列表里字符串的列表外壳去掉
#     await session.send(''.join(alist))                # 将列表里的字符串拼接并输出