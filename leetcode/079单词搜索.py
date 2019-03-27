# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x, y, len_word = len(board), len(board[0]), len(word)
        if x * y < len_word:
            return False
        def helper(loc_i, loc_j, count, locs):
            if count == len_word:
                return True
            if loc_i < 0 or loc_i >= x  or loc_j < 0 or loc_j >= y:
                return False
            if [loc_i, loc_j] not in locs and board[loc_i][loc_j] == word[count]:
                return helper(loc_i-1, loc_j, count+1, locs+[[loc_i, loc_j]]) or \
                       helper(loc_i+1, loc_j, count+1, locs+[[loc_i, loc_j]])or \
                       helper(loc_i, loc_j-1, count+1, locs+[[loc_i, loc_j]])or \
                       helper(loc_i, loc_j+1, count+1, locs+[[loc_i, loc_j]])
            return False
        for i in range(x):
            for j in range(y):
                if helper(i, j, 0, []):
                    return True
        return False
