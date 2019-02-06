# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 用一个栈记录左括号的索引，如果有右括号出现，那么将当前长度与res对比，取较大值
        res, index, stack = 0, 0, []  # 结果;
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # 记录索引
            elif not stack:
                index = i + 1  # 从下一位重新开始
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    res = max(res, i - index + 1)
        return res

    def longestValidParentheses1(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动态规划的方法调了一会，在s的前面加个右括号后一切迎刃而解
        s = ')' + s
        dp = [0] * len(s)  # dp表示到该字符处的最长有效括号长度
        for i, char in enumerate(s):
            if i == 0:
                continue
            if char == ')':  # 只有右括号时才可能有效
                if s[i-1-dp[i-1]] == '(':  # 如果dp[i-1]范围前一个字符为左括号
                    dp[i] = dp[i-1] + 2
                dp[i] += dp[i-dp[i]]  # 加上dp[i]范围前一个字符的dp
        return max(dp)



