# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def bracket(s='', left=0, right=0):  # 回溯法
            """
            :param s:当前生成序列
            :param left:左括号个数
            :param right:右括号个数
            :return:
            """
            if len(s) == 2*n:
                res.append(s)
                return
            if left < n:
                bracket(s+'(', left+1, right)
            if left > right:
                bracket(s+')', left, right+1)
        bracket()
        return res

    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']
        res = []
        for i in range(n):  # 把n看成左右两部分，左边被一个括号包着(右边也可以)
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                    res.append('('+left+')'+right)
        return res
