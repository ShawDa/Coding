# -*- coding:utf-8 -*-

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        return list(set(range(1,length+1)) - set(nums))


if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))