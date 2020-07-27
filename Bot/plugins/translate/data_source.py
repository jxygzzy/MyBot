# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 22:31
# @Author  : P19Y0UN9
# @File    : data_source.py
# @Software: PyCharm
import json
import urllib

async def get_translate(query: str)->str:
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"  # 有道翻译的地址
    data = {}
    data["i"] = query
    data["from"] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15951370098242'
    data['sign'] = 'fe4150e5d7a6c7085fa20867b73cdc53'
    data['ts'] = '1595137009824'
    data['bv'] = 'e9c283fcdef47746c8a8c8d0ed42d0ce'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'

    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    if target['errorCode'] == 0:
        result = ''
        for data in target['translateResult'][0]:
            result=result+data['tgt']
        return result
    else:
        return False