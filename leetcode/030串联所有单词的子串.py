# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # 减少重复计算:先根据起始点不同把s分成一个一个词，如s长度为18，words长度2，每个word长度3，
        # 那么可以分为0 3 6 9 12 15，1 4 7 10 13，2 5 8 11 14三段来计算 ；
        # 然后用双指针记录首尾单词的起始位置，和words_dict比较来移动两个指针；如果匹配则写入左指针。
        if not words:
            return []
        words_count, word_length = len(words), len(words[0])  # 单词个数和每个单词长度
        words_dict, res, s_length = {}, [], len(s)
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1
        for i in range(word_length):  # 根据单词长度划分几块
            left, right, count, now_dict = i, i, 0, {}  # 起始单词位置,单词数,单词字典
            while right <= s_length-word_length:
                right_str = s[right:right+word_length]
                if right_str not in words_dict:  # 词不在words中,从right右边重新开始
                    count, now_dict, right = 0, {}, right+word_length
                    left = right
                else:
                    now_dict[right_str] = now_dict.get(right_str, 0) + 1
                    right += word_length
                    count += 1
                    if now_dict[right_str] > words_dict[right_str]:
                        # 某个词多了,所以要把多了的这个词在前面的去掉一个
                        while now_dict[right_str] > words_dict[right_str]:
                            left_str = s[left:left+word_length]
                            now_dict[left_str] -= 1
                            count -= 1
                            left += word_length
                    if count == words_count:  # 如果dict和count都没问题,说明匹配
                        res.append(left)  # 之后left后移一位
                        now_dict[s[left:left+word_length]] -= 1
                        count -= 1
                        left += word_length
        return res
