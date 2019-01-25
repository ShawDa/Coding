# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]
        return count+1
