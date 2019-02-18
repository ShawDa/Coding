# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                right -= 1
            else:
                left += 1
        return left
