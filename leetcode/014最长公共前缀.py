# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res, flag = '', ''
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if j == 0:
                    res += flag
                    flag = strs[j][i]
                try:
                    if strs[j][i] != flag:
                        return res
                except IndexError:
                    return res
        res += flag
        return res
