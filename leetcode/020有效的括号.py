# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 借助一个栈，如果是左括号就进栈，是右括号就比较是不是和出栈的能配对
        stack = []
        brackets = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in brackets:
                top = stack.pop(-1) if stack else 'WRONG'
                if brackets[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
