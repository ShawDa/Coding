# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # 丑数一定是2^x*3^y*5^z,维护三个指针，判断取了相对较小丑数时各指针所指位置
        if index == 0:
            return 0
        res = [1]
        p0, p1, p2 = 0, 0, 0
        for i in range(1, index):
            res.append(min(res[p0]*2, res[p1]*3, res[p2]*5))
            if res[i] == res[p0]*2:
                p0 += 1
            if res[i] == res[p1]*3:
                p1 += 1
            if res[i] == res[p2]*5:
                p2 += 1
        return res[-1]
