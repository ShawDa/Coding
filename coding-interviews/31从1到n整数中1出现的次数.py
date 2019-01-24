# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        for i in range(1, n+1):
            res += str(i).count('1')
        return res

    def NumberOf1Between1AndN_Solution1(self, n):
        # write code here
        count, base, tmp = 0, 1, n
        while tmp:
            res, tmp = tmp % 10, tmp // 10  # 余数,整除结果
            count += tmp*base
            if res == 1:
                count += n % base + 1  # 该位后面所有的数(0到n%base)
            elif res > 1:
                count += base  # 相当于tmp+1
            base *= 10
        return count
