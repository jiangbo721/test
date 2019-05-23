# -*- coding:utf-8 -*-
# project: test
# author: liujiangbo
# file: export_excel.py
# ide: PyCharm
# time: 2019-05-23 14:02
import json

import xlrd
import xlwt


readbook = xlrd.open_workbook(r'/Users/mac/Downloads/test1.xlsx')
sheet = readbook.sheet_by_name('Sheet1')
nrows = sheet.nrows  # 行
ncols = sheet.ncols  # 列

channel_dict = {
    '1': 'V.Fine',
    '3': '新片场',
    '39': '头条',
    '40': '千库',
}

headers_cn = ['音乐人用户id', '订单id', '渠道', '支付价格', '目的', '范围', '区域', '时长',
              '被授权者', '授权代码', '授权时间', '授权项目', '项目描述', '授权投放渠道', '消费者id',
              '消费者名称', '消费者手机号', '消费者邮箱', '消费者注册时间', '消费者上次登录时间', '公司地址',
              '公司名称', '音乐名称', '音乐id', '音乐人名称']

headers_en = ['user_id', 'order_id', 'channel', 'price', 'purpose', 'detail', 'area', 'expires',
              'name', 'cf_uuid', 'cf_time', 'cf_project', 'project_desc', 'where_to_put', 'cuid',
              'user_name', 'user_phone', 'user_email', 'register_time', 'last_login', 'address',
              'company', 'music_name', 'music_id', 'musician']


write_list = []
for i in range(nrows):
    row_dict = {}
    purpose_dict = json.loads(sheet.cell(i,4).value)
    customer_dict = json.loads(sheet.cell(i,5).value)
    row_dict.update({
        "user_id": sheet.cell(i,0).value,
        "order_id": sheet.cell(i,1).value,
        "channel": channel_dict[str(int(sheet.cell(i,2).value))],
        "price": sheet.cell(i,3).value,
        'purpose': purpose_dict["choices"]["purpose"]["text"],
        'detail': purpose_dict["choices"]["detail"]["text"],
        'area': purpose_dict["choices"]["area"]["text"],
        'expires': purpose_dict["choices"]["expires"]["text"],
        'name': customer_dict.get("company") or customer_dict.get("name"),
        'cf_uuid': sheet.cell(i,6).value,
        'cf_time': sheet.cell(i,7).value,
        'cf_project': purpose_dict.get("project_name"),
        'project_desc': purpose_dict.get("project_desc"),
        'where_to_put': purpose_dict.get("project_where_to_put"),
        'cuid': sheet.cell(i,11).value,
        'user_name': sheet.cell(i,12).value,
        'user_phone': sheet.cell(i,13).value,
        'user_email': sheet.cell(i,14).value,
        'register_time': sheet.cell(i,15).value,
        'last_login': sheet.cell(i,16).value,
        'address': customer_dict.get("address"),
        'company': customer_dict.get("company"),
        'music_name': sheet.cell(i,8).value,
        'music_id': sheet.cell(i,9).value,
        'musician': sheet.cell(i,10).value,
    })
    write_list.append(row_dict)


write_book = xlwt.Workbook("UTF-8")

write_sheet = write_book.add_sheet(u'销售数据', True)
# 写标题
for i in range(25):
    write_sheet.write(0, i, headers_cn[i])

for idx, order in enumerate(write_list, 1):
    for j in range(25):
        write_sheet.write(idx, j, order[headers_en[j]])

write_book.save(r'/Users/mac/Downloads/test2.xlsx')

