# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        left, right, count, len_w = 0, 0, 0, len(words)  # 左右指针位置和放置长度
        res = []
        while left < len_w:
            right, count, one_row = left, len(words[left]), ''
            while right+1 < len_w and (count+1+len(words[right+1])) <= maxWidth:
                count += 1+len(words[right+1])
                right += 1
            if right < len_w-1:  # 非最后一行
                if right-left > 0:  # 多个单词
                    a = (maxWidth-count) // (right-left)  # 单词之间至少填充空格数
                    b = (maxWidth-count) % (right-left)  # 前b个单词要多填充一个空格
                    for i in range(left, right):
                        one_row += words[i] + " " * (a+1)
                        if i-left < b:
                            one_row += ' '
                    one_row += words[right]
                else:  # 一个单词
                    one_row = words[left]
                    while len(one_row) < maxWidth:
                        one_row += ' '
                res.append(one_row)
                left = right+1
            else:  # 最后一行
                for i in range(left, len_w-1):
                    one_row += words[i] + ' '
                one_row += words[-1]
                while len(one_row) < maxWidth:
                    one_row += ' '
                res.append(one_row)
                break
        return res
