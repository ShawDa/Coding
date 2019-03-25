# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        left, right, count, t_dict, len_s = 0, 0, 0, {}, len(s)
        res, min_len, len_t = '', len_s+1, len(t)
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1
        while right < len_s:
            a = s[right]
            if a in t_dict:
                t_dict[a] -= 1
                if t_dict[a] >= 0:
                    count += 1  # 如果增加了个新元素count加一
                while count == len_t:
                    if right-left+1 < min_len:
                        res = s[left:right+1]
                        min_len = right-left+1
                    b = s[left]
                    if b in t_dict:
                        t_dict[b] += 1
                        if t_dict[b] > 0:  # 如果该处元素在t中
                            count -= 1
                    left += 1
            right += 1
        return res
