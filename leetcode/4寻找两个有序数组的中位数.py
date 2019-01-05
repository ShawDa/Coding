# -*- coding:utf-8 -*-


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # O(m+n)时间复杂度
        m, n, res, i, j = len(nums1), len(nums2), [], 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i < m:
            res.extend(nums1[i:m])
        if j < n:
            res.extend(nums2[j:n])
        if len(res) % 2 == 0:
            return (res[len(res)//2] + res[(len(res)//2)-1])/2
        else:
            return res[len(res)//2] / 1

    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        题目要求用到O(log(m + n))的时间复杂度，一看就是需要二分的思想。
        主要的思想是对两个数组分别找到一个点把两个数组分成左右两边，所有左边的数个数为(m+n+1)//2个，
        且满足上面左边最大值小于等于下面右边最小值，上面右边最小值大于等于下面左边最大值。
        如果上面右边最小值小于下面左边最大值，那么上面left要向mid右移一位；
        如果上面左边最大值大于下面右边最小值，那么上面right要向mid左移一位。
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        x, y, z = 0, m, (m+n+1)//2
        while x <= y:
            i = (x+y) // 2
            j = z - i
            print(i, j)
            if i < m and nums1[i] < nums2[j-1]:
                x = i+1
            elif i > 0 and nums1[i-1] > nums2[j]:
                y = i-1
            else:
                if i == 0:
                    max2left = nums2[j-1]
                elif j == 0:
                    max2left = nums1[i-1]
                else:
                    max2left = max(nums1[i-1], nums2[j-1])

                if (m+n) % 2 == 1:
                    return max2left / 1.0

                if i == m:
                    min2right = nums2[j]
                elif j == n:
                    min2right = nums1[i]
                else:
                    min2right = min(nums2[j], nums1[i])
                return (max2left + min2right) / 2.0

    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        上面可以看到处理奇偶问题的时候有些复杂，那可不可以固定让数组的总长度变为偶数了？
        答案是可以的：
        对于2 3 5和1 4 7 9两组数，可以在数的间隔加上#，可得#2#3#5#和#1#4#7#9#,3和4的长度变成了7和9，
        前一个中位数在第三位，原数上是第一位，左右是(3-1)//2和3//2，后一个中位数在第四位，
        原数上是第一 二位，左右是(4-1)//2和4//2。每一步要求L1，R1，L2，R2，还要注意边界条件。
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        L1, R1, L2, R2, left, right = 0, 0, 0, 0, 0, 2*m
        import sys
        while left <= right:
            mid = (left+right)//2
            res = (m+n-mid)

            # 如果出现了mid==0或2×m的情况，说明结果在2上；如果res出现了该情况，说明结果在1上
            L1 = -sys.maxsize if mid == 0 else nums1[(mid-1)//2]
            R1 = sys.maxsize if mid == 2*m else nums1[mid//2]
            L2 = -sys.maxsize if res == 0 else nums2[(res-1)//2]
            R2 = sys.maxsize if res == 2*n else nums2[res // 2]

            if L1 > R2:  # 左移
                right = mid - 1
            elif L2 > R1:
                left = mid + 1
            else:
                break
        return (max(L1, L2) + min(R1, R2)) / 2.0
