# coding:utf8

class TankCoordinate:
    """
    实现检测敌军坦克所在坐标功能
    """

    def __init__(self, now_position, now_direct, signals):
        """
        初始化
        :param now_position: 当前坦克所在的坐标
        :param now_direct: 当前坦克所在的方向
        :param signals: 坦克接收到的信号字符串
        """
        self.position = now_position
        self.direct = now_direct
        self.signals = signals

    def get_position_tank(self):
        """
        获取坦克接收到信号之后，执行指令移动到的位置坐标
        :return: 坦克的坐标和朝向
        """
        real_time_direct = self.direct
        reversal_flag = False
        for signal in self.signals:
            if signal is "M":
                self.position = self.move_coordination(real_time_direct, self.position,
                                                       reversal_flag=reversal_flag)
            if signal is "R":
                real_time_direct = self.turn_direct(real_time_direct, turn_right=True,
                                                    reversal_flag=reversal_flag)
            if signal is "L":
                real_time_direct = self.turn_direct(real_time_direct, turn_right=False,
                                                    reversal_flag=reversal_flag)
            if signal is "P":
                reversal_flag = not reversal_flag
            # print("字母是什么", signal, '是否反转:', reversal_flag, "当前方向：", real_time_direct)
        return self.position, real_time_direct

    @classmethod
    def turn_direct(cls, direct, turn_right=True, reversal_flag=False):
        """
        获得坦克所朝方向
        :param direct: 当前坦克所朝的方向
        :param turn_right: 是否向右转
        :param reversal_flag: 是否反转
        :return: 坦克需要调转到的方向
        """
        direct_weight = {
            "N": 0,
            "E": 1,
            "S": 2,
            "W": 3
        }
        if (turn_right and not reversal_flag) or (not turn_right and reversal_flag):
            if direct_weight[direct] + 1 == 4:
                direct = "N"
            else:
                direct = [dire for dire, value in direct_weight.items() if
                          direct_weight[direct] + 1 == value][0]
        elif (not turn_right and not reversal_flag) or (turn_right and reversal_flag):
            if direct_weight[direct] - 1 == -1:
                direct = "W"
            else:
                direct = [dire for dire, value in direct_weight.items() if
                          direct_weight[direct] - 1 == value][0]
        return direct

    @classmethod
    def move_coordination(cls, direct, position, reversal_flag=False):
        """
        移动坐标
        :param direct: 当前坦克的朝向
        :param position: 当前坦克坐标
        :param reversal_flag: 是否反转标志
        :return: 坦克调整后的坐标
        """
        if reversal_flag:
            direct_dict = {
                "E": (-1, 0),
                "W": (1, 0),
                "N": (0, -1),
                "S": (0, 1)
            }
        else:
            direct_dict = {
                "E": (1, 0),
                "W": (-1, 0),
                "N": (0, 1),
                "S": (0, -1)
            }
        return direct_dict[direct][0] + position[0], direct_dict[direct][1] + position[1]


if __name__ == '__main__':
    tank = TankCoordinate((11, 39), "W", "MTMPRPMTMLMRPRMTPLMMTLMRRMP")
    postion, direct = tank.get_position_tank()
    print '坦克坐标为:', postion, '坦克所朝的方向为:', direct
