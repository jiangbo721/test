# -*- coding:utf-8 -*-
# project: test
# author: liujiangbo
# file: ttt.py
# ide: PyCharm
# time: 2019-06-12 15:52


class Bug:
    def __eq__(self, other):
        return True

    def __new__(self, *args, **kwargs):
        return None

if __name__ == '__main__':

    b = Bug()
    assert b is not None and b == None, '没通过'
    print '通过了'
