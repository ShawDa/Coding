# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def ReverseSentence(self, s):
        # write code here
        s_list = s.split(' ')
        return ' '.join(s_list[::-1])

    def ReverseSentence1(self, s):
        # write code here
        s, begin = list(s)[::-1], 0
        for i, char in enumerate(s):
            if char == ' ':
                s[begin:i] = s[begin:i][::-1]
                begin = i+1
        s[begin:] = s[begin:][::-1]
        return ''.join(s)
