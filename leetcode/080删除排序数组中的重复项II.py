# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        cnt = 1
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                cnt = 1
                index += 1
            elif cnt < 2:
                nums[index] = nums[i]
                cnt += 1
                index += 1
            else:
                pass
        return index
