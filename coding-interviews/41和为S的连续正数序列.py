# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        # 类似一个双指针滑动窗口的思路
        left ,right, res = 1, 2, []
        while left < right:
            here_sum = (left+right)*(right-left+1)/2
            if here_sum < tsum:
                right += 1
            elif here_sum > tsum:
                left += 1
            else:
                one = [i for i in range(left, right+1)]
                left += 1  # 左指针前进一位
                res.append(one)
        return res

    def FindContinuousSequence1(self, tsum):
        # write code here
        res = []
        import math
        for n in range(int(math.sqrt(2*tsum)), 1, -1):  # n越大起始值越小
            # 偶数时均值为中间两数之和的一半,两个数的余数为1
            if (n%2 == 1 and tsum%n == 0) or (tsum%n)*2 == n:
                start = (tsum//n)-(n-1)//2
                res.append(list(range(start, start+n)))
        return res
