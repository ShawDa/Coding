# -*- coding:utf-8 -*-


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 暴力法
        if len(nums) <= 1:
            return None
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 建一个Dict
        if len(nums) <= 1:
            return None
        num_dict = {}
        for i, num in enumerate(nums):
            if (target-num) in num_dict:
                return [num_dict[target - num], i]
            if num not in num_dict:
                num_dict[num] = i
        return None
