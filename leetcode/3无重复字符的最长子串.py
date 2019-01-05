# -*- coding:utf-8 -*-


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 暴力法超时
        def check(part):
            part_list = []
            for i in range(len(part)):
                if part[i] in part_list:
                    return False
                else:
                    part_list.append(part[i])
            return True
        res = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if check(s[i:j]):
                    res = max(res, j-i)
        return res

    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        运用滑动窗口，需要保证窗口里没有重复的字符，并尽可能扩大窗口的大小，且要不停向右滑动。所以：
        1.如果遍历到的字符之前窗口未出现，则扩大右边界，并将该字符写入窗口；
        2.如果字符出现过，那么把左边索引向右移，直到越过之前和当前字符一样的字符；
        3.直到右边界超出范围，则停止。
        """
        res, left, right, window = 0, 0, 0, []
        while right < len(s):
            if s[right] not in window:
                window.append(s[right])
                right += 1
                res = max(res, right-left)
            else:
                window.remove(s[left])
                left += 1
        return res

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 用Dict
        res, left, right, window = 0, 0, 0, {}
        while right < len(s):
            if s[right] not in window:
                window[s[right]] = right
                right += 1
                res = max(res, right - left)
            else:
                tmp = window[s[right]] + 1
                for i in range(left, tmp):
                    del window[s[i]]
                left = tmp
        return res
