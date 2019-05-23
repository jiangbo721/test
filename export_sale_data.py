# -*- coding:utf-8 -*-
# project: test
# author: liujiangbo
# file: export_sale_data.py
# ide: PyCharm
# time: 2019-05-23 16:03
import json

import pandas as pd

channel_dict = {
    '1': u'V.Fine',
    '3': u'新片场',
    '39': u'头条',
    '40': u'千库',
}

def aa(s_dict):
    purpose_dict = json.loads(s_dict)
    choices = purpose_dict.get("choices")
    new_list = []
    new_list.append(choices.get("purpose").get("text"))
    new_list.append(choices.get("expires").get("text"))
    new_list.append(choices.get("detail").get("text"))
    new_list.append(choices.get("area").get("text"))
    new_list.append(purpose_dict.get("project_name"))
    new_list.append(purpose_dict.get("project_desc"))
    new_list.append(purpose_dict.get("project_where_to_put"))
    pf = pd.Series(new_list)
    return pf

def bb(s_dict):
    customer_dict = json.loads(s_dict)
    new_list = []
    new_list.append(customer_dict.get("company") or customer_dict.get("name"))
    new_list.append(customer_dict.get("address"))
    new_list.append(customer_dict.get("company"))
    pf = pd.Series(new_list)
    return pf

def cc(cid):
    return channel_dict[str(cid)]

yinyue = pd.read_excel(r'/Users/mac/Downloads/test1.xlsx')
yinyue[[u"目标", u"时长", u"详情", u"地域", u"授权项目", u"项目描述", u"授权投放渠道"]] = yinyue[u"目的渠道地域时长"].apply(aa)
yinyue[[u"被授权者", u"公司地址", u"公司名称"]] = yinyue[u"被授权者信息"].apply(bb)
yinyue[u"渠道id"].apply(cc)

# yinyue.drop(['目的渠道地域时长', '被授权者信息'], axis=1)
yinyue.drop(columns=u"目的渠道地域时长", inplace=True)
yinyue.drop(columns=u"被授权者信息", inplace=True)
yinyue.to_excel(r'/Users/mac/Downloads/ss4.xlsx', index=False)