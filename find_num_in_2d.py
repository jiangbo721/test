# -*- coding:utf-8 -*-
# project: test
# author: liujiangbo
# file: find_num_in_2d.py
# ide: PyCharm
# time: 2019-07-16 11:32

# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
# 判断数组中是否含有该整数。

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0:
            return False
        row = len(array)
        col = len(array[0])
        i = row - 1
        j = 0
        while i>=0 and j < col:
            this = array[i][j]
            if this > target:
                i -= 1
            elif this < target:
                j += 1
            else:
                return True


if __name__ == '__main__':
    print Solution().Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])