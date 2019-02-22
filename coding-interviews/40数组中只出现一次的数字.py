# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        # 先求所有数字异或的值
        tmp = 0
        for num in array:
            tmp = tmp ^ num
        # 从后往前找到第一个1的位置,这两个数字在该位的值一定不相等
        first_one = 0
        while tmp & 1 != 1:  # 与运算
            tmp = tmp >> 1
            first_one += 1
        # 把所有数分为在该位不相等的两组就可以得到两个不同的数了
        a, b = 0, 0
        for num in array:
            if self.zero_one(num, first_one):
                a = a ^ num
            else:
                b = b ^ num
        return [a, b]

    def zero_one(self, num, loc):
        num = num >> loc
        return num & 1
