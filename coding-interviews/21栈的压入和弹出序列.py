# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) != len(popV) or sorted(pushV) != sorted(popV):
            return False
        stack, j = [], 0
        for i in range(len(pushV)):
            stack.append(pushV[i])
            while stack and stack[-1] == popV[j]:
                stack.pop(-1)
                j += 1
        if stack:
            return False
        return True
