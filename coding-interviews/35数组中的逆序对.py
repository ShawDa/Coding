# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def InversePairs(self, data):
        # write code here
        if len(data) <= 1:
            return 0
        count = 0
        for i in range(len(data)-1):
            for j in range(i+1, len(data)):
                if data[i] > data[j]:
                    count += 1
        return count % 1000000007

    def InversePairs1(self, data):
        # write code here
        copy, count = [], 0
        for num in data:
            copy.append(num)
        copy.sort()
        for num in copy:
            count += data.index(num)  # 最小值index位置表示前面有index个原始大于它
            data.remove(num)  # 移除这个num
        return count % 1000000007

    def InversePairs2(self, data):
        # write code here
        global count
        count = 0
        def merge_sort(data):
            global count
            if len(data) <= 1:
                return data
            mid, array = len(data)//2, []
            left_a, right_a = merge_sort(data[:mid]), merge_sort(data[mid:])
            left, right = 0, 0
            while left < len(left_a) and right < len(right_a):  # 左右已经有序
                if left_a[left] <= right_a[right]:
                    array.append(left_a[left])
                    left += 1
                else:
                    array.append(right_a[right])
                    count += len(left_a)-left  # 若右边小则要加上所有左边剩下的
                    right += 1
            array += left_a[left:]
            array += right_a[right:]
            return array
        merge_sort(data)
        return count % 1000000007
