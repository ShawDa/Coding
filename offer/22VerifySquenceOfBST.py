# -*- coding:utf-8 -*-


class Solution:
    # 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
    def VerifySquenceOfBST(self, sequence):  # 二叉搜索树中序为递增的 左<中<右 去掉最后一个，有分割点将左右分开
        # write code here
        if len(sequence) == 0:
            return False
        mid = sequence[-1]
        i = 0
        for i in range(len(sequence)):
            if sequence[i] > mid:
                break
        for j in range(i, len(sequence)):  # 若右有小于mid的 false
            if sequence[j] < mid:
                return False
        left = right =True
        if i > 2:  # 任意三个数都为true
            left = self.VerifySquenceOfBST(sequence[:i])
        if left and len(sequence)-i > 2:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right


if __name__ == '__main__':
    s = Solution()
    print(s.VerifySquenceOfBST([4,8,6,12,16,14,10]))