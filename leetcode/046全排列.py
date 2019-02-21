# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # BF
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            for one in self.permute(nums[0:i] + nums[i + 1:]):
                res.append([nums[i]] + one)
        return res

    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, length, one = [], len(nums), []
        visited = [0]*length  # 是否访问过
        def helper(count):
            if count == length:
                # 注意这里直接是one的话res里list会为空,因为最后one为[]
                res.append(one.copy())
                return
            for i in range(length):
                if visited[i] == 0:
                    one.append(nums[i])
                    visited[i] = 1
                    helper(count+1)
                    visited[i] = 0
                    one.remove(nums[i])
        helper(0)
        return res

    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, length, one = [], len(nums), []
        def helper(count):
            if count == length:
                # 注意这里直接是one的话res里list会为空,因为最后one为[]
                res.append(one.copy())
                return
            for i in range(count, length):
                one.append(nums[i])
                nums[i], nums[count] = nums[count], nums[i]
                helper(count+1)
                nums[i], nums[count] = nums[count], nums[i]
                one.remove(nums[i])
        helper(0)
        return res
