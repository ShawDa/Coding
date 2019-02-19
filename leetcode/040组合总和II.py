# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()  # 先排序
        res = []
        self.helper(target, candidates, res, [], 0)  # []记录一个临时list,0记录位置保证不重复
        return res

    def helper(self, target, candidates, res, one, num):
        if target == 0:  # target为0说明刚好组合
            res.append(one)
            return
        if target < candidates[0]:  # 不可能有组合
            return
        flag = -1  # 避免重复数字
        for i in range(num, len(candidates)):
            if flag == candidates[i]:
                continue
            if candidates[i] > target:
                break
            tmp = [i for i in one]  # 注意这里要copy
            tmp.append(candidates[i])
            self.helper(target-candidates[i], candidates, res, tmp, i+1)
            flag = candidates[i]
