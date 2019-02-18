# -*- coding:utf-8 -*-
__author__ = 'ShawDa'


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.list_x = [[] for x in range(9)]
        self.list_y = [[] for y in range(9)]
        self.list_box = [[] for box in range(9)]
        for i in range(9):
            for j in range(9):
                try:
                    num = int(board[i][j])
                    box_index = 3 * (i//3) + j//3
                    self.list_x[i].append(num)
                    self.list_y[j].append(num)
                    self.list_box[box_index].append(num)
                except:
                    pass
        # 先记录每一行 列 块的情况，再从左上角开始回溯
        self.helper(board, 0 ,0)

    def helper(self, board, i, j):
        if i == 9:  # 超过最后一行
            return True
        if j == 9:  # 超过最后一列
            return self.helper(board, i+1, 0)
        if board[i][j] == '.':
            for k in range(1, 10):
                box_index = 3 * (i // 3) + j // 3
                if k not in self.list_x[i] + self.list_y[j] + self.list_box[box_index]:
                    board[i][j] = str(k)
                    self.list_x[i].append(k)
                    self.list_y[j].append(k)
                    self.list_box[box_index].append(k)
                    if self.helper(board, i, j+1):
                        return True
                    # 恢复造成的修改，进行下一次枚举或回溯
                    board[i][j] = '.'
                    self.list_x[i].remove(k)
                    self.list_y[j].remove(k)
                    self.list_box[box_index].remove(k)
        else:  # 下一个
            return self.helper(board, i, j+1)
        return False  # 如果所有方案都不可行那么说明之前方案有问题，进行回溯
