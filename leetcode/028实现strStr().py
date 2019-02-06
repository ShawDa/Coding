# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except:
            return -1

    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # BF
        if not needle:
            return 0
        if len(set(list(haystack))) < len(set(list(needle))):
            return -1
        p, a, b = 0, len(haystack), len(needle)
        while p <= a-b:
            match = True
            for i in range(b):
                if haystack[p+i] != needle[i]:
                    match = False  # 不匹配则match置False
                    p += 1
                    break
            if match:
                return p
        return -1

    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # KMP
        if not needle:
            return 0
        if len(haystack) < len(needle) or len(set(list(haystack))) < len(set(list(needle))):
            return -1  # 这里是为了解决无穷多a和无穷多a加个b这种例子
        partial_table, p, a, b = self.partial_table(needle), 0, len(haystack), len(needle)
        while p <= a-b:
            match = True
            for i in range(b):
                if haystack[p+i] != needle[i]:
                    match = False  # 不匹配则match置False
                    p += max(1, i-partial_table[i-1])  # p加上到之前一个字符的长度减去那个字符的部分匹配表值
                    break
            if match:
                return p
        return -1

    def partial_table(self, s):  # 求解部分匹配表
        s_length, res = len(s), [0]
        for i in range(1, s_length):
            s_str = s[:i+1]
            prefix = [s_str[:j] for j in range(1, i+1)]
            postfix = [s_str[j:] for j in range(1, i+1)]
            res_set = set(prefix).intersection(set(postfix))
            res.append(max([len(one) for one in res_set]) if res_set else 0)
        return res
