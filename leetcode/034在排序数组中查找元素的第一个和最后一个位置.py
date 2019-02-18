# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid + 1
            else:
                tmp= mid
                while tmp > 0 and nums[tmp-1] == target:
                    tmp -=1
                while mid < len(nums)-1 and nums[mid+1] == target:
                    mid += 1
                return [tmp, mid]
        return [-1, -1]
