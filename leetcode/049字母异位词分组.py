# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res_dict = {}
        for str in strs:
            tuple_str = tuple(sorted(str))
            if tuple_str not in res_dict:
                res_dict[tuple_str] = [str]
            else:
                res_dict[tuple_str].append(str)
        return list(res_dict.values())

    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res_dict = {}
        for str in strs:  # 因为都是小写字母,所以可以对字母计数
            count = [0] * 26
            for c in str:
                count[ord(c)-ord('a')] += 1
            tuple_count = tuple(count)
            if tuple_count not in res_dict:
                res_dict[tuple_count] = [str]
            else:
                res_dict[tuple_count].append(str)
        return list(res_dict.values())
