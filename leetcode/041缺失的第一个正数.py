# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 整体思路就是把数放到其大小对应的index上
        length, i = len(nums), 0
        while i < length:
            num = nums[i]
            # 如果num在1到length之间且num-1处的值不为num,那么一直互换
            if 1 <= num <= length and nums[num-1] != num:
                nums[num-1], nums[i] = num, nums[num-1]
            else:
                i += 1
        for i, num in enumerate(nums):
            if num != i+1:
                return i+1
        return length + 1
