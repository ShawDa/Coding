# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+nums[i])
            if max_reach >= len(nums)-1:
                return True
        return True

    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 从后往前,找最前一个之后第一个能到末端的,如果第一个能到这,那么就可以
        if not nums:
            return True
        nums, res = nums[::-1], 0
        for i in range(1, len(nums)):
            if nums[i] + res >= i:
                res = i  # res求得就是能到第一个的位置
        return res == len(nums)-1
