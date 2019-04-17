# -*- coding:utf-8 -*-
__author__ = 'ShawDa'

from random_list import random_int_list


def heap_sort(arr):
    def max_heapify(start, end):
        # 调整最大堆
        root = start
        while True:
            child = 2 * root + 1
            if child > end:  # 无子节点
                break
            if child + 1 <= end and arr[child] < arr[child + 1]:  # 找较大子节点
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]  # 交换父子节点
                root = child
            else:
                break

    # 创建最大堆
    for start in range((len(arr) // 2) - 1, -1, -1):
        max_heapify(start, len(arr) - 1)

    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]  # 将最大值置后
        max_heapify(0, end - 1)
    return arr


if __name__ == '__main__':
    data = random_int_list(1, 100, 10)
    print(data)
    print(heap_sort(data))
