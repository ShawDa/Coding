# -*- coding:utf-8 -*-


class Solution:
    # 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
    def __init__(self):
        self.stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)

    def pop(self):
        # write code here
        if len(self.stack) <= 0:
            return False
        self.stack.pop(-1)
        return True

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return min(self.stack)