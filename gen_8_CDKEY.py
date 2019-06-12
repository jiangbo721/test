# -*- coding:utf-8 -*-
# project: test
# author: liujiangbo
# file: gen_8_CDKEY.py
# ide: PyCharm
# time: 2019-06-06 15:38

from itertools import permutations,combinations_with_replacement
from random import shuffle

import pandas as pd

# 生成所有8位数字的排列情况
all_8_num = permutations(range(10), 8)
res = []
for num in all_8_num:
    res.append(num)

# 洗牌
shuffle(res)

# 取出需要的数量
r_2000 = res[:2000]

# 导出到excel
pd.Series()
index = range(1, 2001)
excel_data = {u'序号': index, u'密码': [''.join([str(i) for i in r]) for r in r_2000]}
df2 = pd.DataFrame(excel_data)
df2.to_excel('/Users/mac/Documents/ss.xls', index=False)
