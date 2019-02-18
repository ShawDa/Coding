# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        x_dict = [{} for x in range(9)]  # 9行
        y_dict = [{} for y in range(9)]  # 9列
        box_dict = [{} for box in range(9)]  # 从左到右从上到下9块
        for i in range(9):
            for j in range(9):
                try:
                    num = int(board[i][j])
                    box_index = (i // 3) * 3 + j // 3
                    x_dict[i][num] = x_dict[i].get(num, 0) + 1
                    if x_dict[i][num] > 1:
                        return False
                    y_dict[j][num] = y_dict[j].get(num, 0) + 1
                    if y_dict[j][num] > 1:
                        return False
                    box_dict[box_index][num] = box_dict[box_index].get(num, 0) + 1
                    if box_dict[box_index][num] > 1:
                        return False
                except ValueError:
                    pass
        return True

    def isValidSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        x_list = [[] for x in range(9)]  # 9行
        y_list = [[] for y in range(9)]  # 9列
        box_list = [[] for box in range(9)]  # 从左到右从上到下9块
        for i in range(9):
            for j in range(9):
                try:
                    num = int(board[i][j])
                    box_index = (i // 3) * 3 + j // 3
                    if num in x_list[i] + y_list[j] + box_list[box_index]:
                        return False  # 先判断后添加
                    x_list[i].append(num)
                    y_list[j].append(num)
                    box_list[box_index].append(num)
                except ValueError:
                    pass
        return True
