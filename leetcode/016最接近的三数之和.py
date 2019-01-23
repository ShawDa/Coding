# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res, i = sum(nums[:3]), 0
        while i < len(nums)-2:
            left, right = i+1, len(nums)-1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if abs(res-target) > abs(three_sum-target):
                    res = three_sum
                if three_sum == target:
                    return res
                elif three_sum > target:
                    right -= 1
                else:
                    left += 1
            i += 1
        return res

    def threeSumClosest1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res, i = sum(nums[:3]), 0
        while i < len(nums)-2:
            left, right = i+1, len(nums)-1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if abs(res-target) > abs(three_sum-target):
                    res = three_sum
                if three_sum == target:
                    return res
                elif three_sum > target:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1
        return res

    def threeSumClosest2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res, i = sum(nums[:3]), 0
        while i < len(nums)-2:
            left, right = i+1, len(nums)-1
            cond = nums[i] + nums[i+1] + nums[i+2]
            if cond > target:
                if abs(cond-target) < abs(res-target):
                    res = cond
                break
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if abs(res-target) > abs(three_sum-target):
                    res = three_sum
                if three_sum == target:
                    return res
                elif three_sum > target:
                    right -= 1
                else:
                    left += 1
            i += 1
        return res
