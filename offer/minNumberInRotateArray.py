# -*- coding:utf-8 -*-


class Solution:
    # 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个*非减排序*的数组的一个旋转，输出旋转数组的最小元素。
    # 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray) - 1
        mid = 0
        while rotateArray[left] >= rotateArray[right]:
            if right-left == 1:
                return rotateArray[right]
            mid = left + int((right-left)/2)
            if rotateArray[left] == rotateArray[mid] and rotateArray[right] == rotateArray[mid]:
                length = right - left
                minnum = rotateArray[left]
                for i in range(length):
                    if rotateArray[left+i] < minnum:
                        minnum = rotateArray[left+i]
                return minnum
            elif rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid
        return rotateArray[mid]