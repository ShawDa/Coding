# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 递归
        if not digits:
            return []
        nums, res = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'], []
        if len(digits) == 1:
            return list(nums[int(digits[0])-2])
        left = self.letterCombinations(digits[:-1])
        right = list(nums[int(digits[-1])-2])
        for i in left:
            for j in right:
                res.append(i+j)
        return res

    def letterCombinations1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        nums, res = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'], ['']
        for digit in digits:
            res = [a+b for a in res for b in nums[int(digit)-2]]
        return res

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 回溯
        if not digits:
            return []
        nums, res = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'], []

        def helper(s='', index=0):
            if len(s) == len(digits):
                res.append(s)
                return
            for char in nums[int(digits[index])-2]:
                helper(s+char, index+1)
        helper()
        return res
