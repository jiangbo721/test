# -*- coding:utf-8 -*-
# author: liujiangbo
"""
某次战役中，为便于信息交互，我军侦察部门将此次战役的关键高地坐标设定为（x=0，y=0）并规定，
每向东增加100米，x加1，每向北增加100米，y加1。

同时，我军情报部门也破译了敌军向坦克发送的指挥信号，其中有三种信号（L,R,M）用于控制坦克的运动，
L 和 R 分别表示使令坦克向左、向右转向，M 表示令坦克直线开进100米，其它信号如T用于时间同步，
P用于反转信号，既出现p，后面的信号向左变为向右，向右变为向左，向前变为向后，反之亦然。

一日，我军侦察兵发现了敌军的一辆坦克，侦察兵立即将坦克所在坐标（P, Q）及坦克前进方向
（W：西，E：东，N：北，S：南）发送给指挥部，同时启动信号接收器，将坦克接收到的信号实时同步发往指挥部，
指挥部根据这些信息得以实时掌控了该坦克的位置，并使用榴弹炮精准地击毁了该坦克。

假设，侦察兵发送给指挥部的信息如下：坦克坐标：（11，39）坦克运行方向：W，
坦克接收到的信号为：MTMPRPMTMLMRPRMTPLMMTLMRRMP，请通过编程计算出坦克所在的位置。
"""

class Tank(object):
    """
    坦克
    """
    direction_w = 'W'
    direction_n = 'N'
    direction_e = 'E'
    direction_s = 'S'
    left = 'L'
    right = 'R'
    DIRECTION_TUPLE = (direction_w, direction_n, direction_e, direction_s)

    def __init__(self, signals, direction, x=0, y=0):
        self.signals = signals
        self.x = x
        self.y = y
        self.W = -1
        self.N = 1
        self.E = 1
        self.S = -1
        self.left_index = -1
        self.right_index = -3
        self.direction = direction

    def go(self, direction):
        if direction == self.direction_w:
            self.x += self.W
        elif direction == self.direction_n:
            self.y += self.N
        elif direction == self.direction_e:
            self.x += self.E
        elif direction == self.direction_s:
            self.y += self.S
        else:
            raise KeyError("direction error")

    def turn(self, l_or_r):
        direction_idx = self.DIRECTION_TUPLE.index(self.direction)
        if l_or_r == self.left:
            self.direction = self.DIRECTION_TUPLE[direction_idx + self.left_index]
        elif l_or_r == self.right:
            self.direction = self.DIRECTION_TUPLE[direction_idx + self.right_index]
        else:
            raise KeyError("must L or R, not {}".format(l_or_r))

    def reverse(self):
        self.left_index, self.right_index = self.right_index, self.left_index
        self.W = -self.W
        self.N = -self.N
        self.E = -self.E
        self.S = -self.S

    def main(self):
        for signal in self.signals:
            if signal == "L":
                self.turn(self.left)
            elif signal == "R":
                self.turn(self.right)
            elif signal == "M":
                self.go(self.direction)
            elif signal == "T":
                pass
            elif signal == "P":
                self.reverse()
            else:
                raise KeyError("signal error!")
        print "坦克的当前位置是x: {x}, y: {y}".format(x=self.x, y=self.y)

if __name__ == '__main__':
    tank = Tank("MTMPRPMTMLMRPRMTPLMMTLMRRMP", "W", x=11, y=39)
    tank.main()