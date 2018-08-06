# -*- coding:utf-8 -*-


class Solution(object):
    """
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
    注意：答案中不可以包含重复的三元组。
    例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
    满足要求的三元组集合为：
    [
    [-1, 0, 1],
    [-1, -1, 2]
    ]
    """
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # brute
        return_list = []
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if num + nums[j] + nums[k] == 0 and sorted([num, nums[j], nums[k]]) not in return_list:
                        return_list.append(sorted([num, nums[j], nums[k]]))
                        break

        # pointer
        if len(nums) < 3:
            return []
        return_list = []
        nums = sorted(nums)
        # 定义三个指针,第一个从第一个开始,第二个从第一个后开始,第三个在最后一个,根据求和情况右移第二个或左移第三个指针
        i = 0
        while i < len(nums)-2:
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                sums = nums[i] + nums[j] + nums[k]
                if sums == 0:
                    return_list.append([nums[i], nums[j], nums[k]])
                if sums <= 0:
                    num_j = nums[j]
                    j += 1
                    while(nums[j] == num_j and j+1<k):
                        j += 1
                if sums >= 0:
                    num_k = nums[k]
                    k -= 1
                    while(nums[k] == num_k and j<k-1):
                        k -= 1
            num_i = nums[i]
            i += 1
            while(num_i == nums[i] and i+1 < len(nums) - 1):
                i += 1
        return return_list


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [0, 0, 0, 0, 0, 0]
    obj = Solution()
    print(obj.threeSum(nums))
    print(sorted([1, -1, 0, -1]))
    print([1, -1, 0, -1][:-2])
    pass
