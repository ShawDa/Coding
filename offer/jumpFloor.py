# -*- coding:utf-8 -*-


class Solution:
    # 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
    def jumpFloor(self, number):
        # write code here 递归,可以看成先跳1级或2级，后面的再开始
        if number <= 0:
            return False
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            # return self.jumpFloor(number-2) + self.jumpFloor(number-1)
            num1 = 1
            num2 = 2
            while number-3 > 0:
                num1, num2 = num2, num2+num1
                number -= 1
            return num1+num2