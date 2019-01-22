# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k <= 0:
            return []
        tinput.sort()
        return tinput[:k]

    def GetLeastNumbers_Solution1(self, tinput, k):
        # write code here
        if k > len(tinput) or k <= 0:
            return []
        self.quick_sort(tinput, 0, len(tinput)-1)
        return tinput[:k]

    def quick_sort(self, array, left, right):
        def partition(a, l, r):
            candi, i = a[r], l
            for j in range(l, r):
                if a[j] < candi:
                    a[i], a[j] = a[j], a[i]
                    i += 1
            a[i], a[r] = a[r], a[i]
            return i
        if left < right:
            q = partition(array, left, right)
            self.quick_sort(array, left, q-1)
            self.quick_sort(array, q+1, right)

    def GetLeastNumbers_Solution2(self, tinput, k):
        # write code here
        if k > len(tinput) or k <= 0:
            return []
        heap = tinput[:k]

        # 构建最大堆 自底向上
        for i in range(len(heap) // 2 - 1, -1, -1):
            self.max_heapify(heap, i, len(heap) - 1)

        for num in tinput[k:]:
            if num < heap[0]:  # 重构最大堆
                heap[0] = num
                self.max_heapify(heap, 0, len(heap) - 1)

        for end in range(len(heap) - 1, -1, -1):  # 排序
            heap[end], heap[0] = heap[0], heap[end]
            self.max_heapify(heap, 0, end - 1)
        return heap

    def max_heapify(self, array, start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and array[child + 1] > array[child]:
                child += 1  # 取较大子节点
            if array[child] > array[root]:
                array[child], array[root] = array[root], array[child]
                root = child  # 如果父子节点交换了,那么下面的可能要调整
            else:
                break
