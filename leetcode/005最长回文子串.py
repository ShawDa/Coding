# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        max_length, start, length = 1, 0, 3
        dp = [[0]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1  # 一个字符始终是回文
            if i < len((s))-1 and s[i] == s[i+1]:
                dp[i][i+1] = 1
                start = i
                max_length = 2
        for length in range(3, len(s)+1):
            for i in range(len(s)-length+1):
                j = i + length - 1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = 1
                    start = i
                    max_length = length
        return s[start:start+max_length]

    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expand(s, i, i)  # 奇数
            len2 = self.expand(s, i, i+1)  # 偶数
            length = max(len1, len2)
            if length > end-start:
                start = i - (length-1) // 2
                end = i + (length) // 2
        return s[start:end+1]

    def expand(self, s, left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right-left-1  # 返回长度

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        new = '$#' + '#'.join(s) + '#@'
        center, right, lens = 0, 0, [0] * len(new)
        for i in range(1, len(new)-1):
            if i < right:
                lens[i] = min(lens[2*center-i], right-i)
            while new[i-lens[i]-1] == new[i+lens[i]+1]:
                lens[i] += 1
            if lens[i] + i > right:
                right = lens[i] + i
                center = i
        maxlen = max(lens)
        index = lens.index(maxlen)
        res = new[index-maxlen:index+maxlen+1].replace('#', '')
        return res
