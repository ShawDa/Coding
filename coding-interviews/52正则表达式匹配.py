# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if pattern == '':
            return s == ''
        if len(pattern) > 1 and pattern[1] == '*':
            return self.match(s, pattern[2:]) or \
                   (s != '' and (s[0] == pattern[0] or pattern[0] == '.') and self.match(s[1:], pattern))
        else:
            return s != '' and (s[0] == pattern[0] or pattern[0] == '.') and self.match(s[1:], pattern[1:])
