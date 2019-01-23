# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 先排序后再用三个指针处理，注意i和j向右移或k向左移的过程中，如果遇到相同的数要跳过
        if len(nums) < 3:
            return []
        nums.sort()
        i, res = 0, []
        while i < len(nums)-2:
            if nums[i] > 0:
                break
            j, k, nums_i = i+1, len(nums)-1, nums[i]
            while j < k:
                nums_j, nums_k = nums[j], nums[k]
                nums_sum = nums_i + nums_j + nums_k
                if nums_sum == 0:
                    res.append([nums_i, nums_j, nums_k])
                if nums_sum <= 0:
                    j += 1
                    while nums[j] == nums_j and j < k-1:
                        j += 1
                if nums_sum >= 0:
                    k -= 1
                    while nums[k] == nums_k and k > j+1:
                        k -= 1
            i += 1
            while nums[i] == nums_i and i < len(nums) - 2:
                i += 1
        return res
