# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def largestRectangleArea(self, heights):
        stack, res = [], 0  # 递增栈
        heights.append(0)  # heights加上0保证之前所有数都考虑到
        for i, num in enumerate(heights):
            while stack and num <= heights[stack[-1]]:  # 如果stack存在且当前数小于等于栈顶位置的数
                a = stack.pop(-1)  # 计算栈顶高度的面积
                res = max(res, heights[a]*(i-stack[-1]-1 if stack else i))
            stack.append(i)
        return res
