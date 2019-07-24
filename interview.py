# -*- coding:utf-8 -*-
# @project: test
# @author: liujiangbo
# @file: interview.py
# @ide: PyCharm
# @time: 2019-04-09 15:19

def SepPositiveNegative(test_list):
    """
    将数组里的负数排在数组的前面，正数排在数组的后面。但不改变原先负数和正数的排列顺序。
    """
    if len(test_list) <= 1:
        return test_list
    for _ in range(len(test_list)):
        for i in range(len(test_list)):
            if test_list[i] > 0 and i < len(test_list) - 1:
                if test_list[i + 1] < 0:
                    test_list[i], test_list[i + 1] = test_list[i + 1], test_list[i]

    print test_list

SepPositiveNegative([-5, 2, -3, 4, -8, -9, 1, 3, -10])


def sort_stack_by_stack(test_list):
    """
    用一个栈实现另一个栈的排序

    :param list test_list:
    :return:
    """
    temp = []
    while test_list:
        current = test_list.pop()
        while temp and temp[-1] < current:
            test_list.append(temp.pop())
        temp.append(current)

    # 将临时的栈倒出来
    while temp:
        test_list.append(temp.pop())
    print test_list

sort_stack_by_stack([-5, 2, -3, 4, -8, -9, 1, 3, -10])

def check_parenthesis(test_str):
    """
    检查是否括号平衡
    :param str test_str:
    :return:
    """
    left_pattern = '({['
    right_pattern = ')}]'
    stack = []
    for i in test_str:
        if i in left_pattern:
            stack.append(i)
        if i in right_pattern:
            last = stack.pop()
            if right_pattern.index(i) != left_pattern.index(last):
                return False
    else:
        return True
print check_parenthesis('{}{}()([])')