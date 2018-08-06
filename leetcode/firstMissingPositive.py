# -*- coding:utf-8 -*-


class Solution(object):
    """
    定一个未排序的整数数组，找出其中没有出现的最小的正整数。
    示例 1:
    输入: [1,2,0]
    输出: 3
    示例 2:
    输入: [3,4,-1,1]
    输出: 2
    示例 3:
    输入: [7,8,9,11,12]
    输出: 1
    """
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 1
        i = 0
        # 用索引对位排序0：1 1：2...
        while i<length:
            if nums[i]>0 and nums[i]<=length and nums[nums[i]-1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
                i -= 1
            i += 1
        print(nums)
        for i in range(length):
            if nums[i] != i+1:
                return i+1
        return length+1


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([3,4,-1,1]))