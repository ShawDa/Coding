# -*- coding:utf-8 -*-


class Solution(object):
    """
    给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
    找到所有出现两次的元素。
    你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
    示例：
    输入:
    [4,3,2,7,8,2,3,1]
    输出:
    [2,3]
    """
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # too long time
        single = []
        duplicate = []
        for num in nums:
            if num not in single:
                single.append(num)
            else:
                single.remove(num)
                duplicate.append(num)

        # 正负号标记法 如果num索引处的数小于0,加入dup，否则乘以-1
        dup = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dup.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return dup


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicates([4,3,2,7,8,2,3,1]))
