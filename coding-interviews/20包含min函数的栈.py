# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def __init__(self):
        self.stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)

    def pop(self):
        # write code here
        if len(self.stack) == 0:
            return False
        return self.stack.pop(-1)

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return min(self.stack)
