# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        length = len(numbers)
        # 如果某个数出现过就在对应位置上*-1,再出现就会知道了
        for i, num in enumerate(numbers):
            if num < 0:
                num = -num
            if numbers[num] < 0:
                duplication[0] = -numbers[num]
                return True
            numbers[num] = -1*numbers[num]
        return False
