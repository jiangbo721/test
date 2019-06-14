# -*- coding:utf-8 -*-
# project: test
# author: liujiangbo
# file: ergeng.py
# ide: PyCharm
# time: 2019-06-14 16:33
import json

import pandas as pd


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

yinyue = pd.read_excel(r'/Users/mac/Downloads/ergeng.xlsx')
yinyue[[u"用途", u"年限", u"方式", u"地域", u"项目名称", u"项目详情", u"投放渠道"]] = yinyue[u"data"].apply(aa)

yinyue.drop(columns=u"data", inplace=True)
yinyue.to_excel(r'/Users/mac/Downloads/ergengergeng.xlsx', index=False)