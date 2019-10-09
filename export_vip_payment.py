# -*- coding:utf-8 -*-
# project: test
# author: liujiangbo
# file: export_vip_payment.py
# ide: PyCharm
# time: 2019-08-07 13:50

# -*- coding:utf-8 -*-
# project: test
# author: liujiangbo
# file: export_sale_data.py
# ide: PyCharm
# time: 2019-05-23 16:03
import json
import re

import pandas as pd

a = {"certificate": 10, "price": 8640, "discount": 0.7, "download": 30, "property": "limited",
     "day": 180}


def aa(s_dict):
    payment_dict = json.loads(s_dict)
    new_list = []
    new_list.append(payment_dict.get("price"))
    new_list.append(payment_dict.get("discount"))
    new_list.append(payment_dict.get("price") * payment_dict.get("discount"))
    pf = pd.Series(new_list)
    return pf


def gg(s):
    if isinstance(s, unicode):
        return re.sub("(\.\d{6})", "", s)
    else:
        return s


yinyue = pd.read_excel(r'/Users/mac/Downloads/导出数据/vfine4~6月会员支付信息.xlsx', dtype=str)
yinyue[[u"原价", u"折扣", u"实际支付价格"]] = yinyue[u"数据"].apply(aa)
# yinyue[u"支付订单号"] = yinyue[u"支付订单号"].apply()
yinyue.drop(columns=u"数据", inplace=True)

yinyue.to_excel(r'/Users/mac/Downloads/vfine 4~6月会员支付信息.xlsx', index=False)
