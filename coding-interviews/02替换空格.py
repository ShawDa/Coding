# -*- coding:utf-8 -*-


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = s.replace(' ', '%20')
        return s

    def replaceSpace1(self, s):
        # write code here
        space_count = list(s).count(' ')
        if space_count == 0:
            return s
        new_list = list(s) + ['0'] * (2*space_count)
        i = 0
        while i < len(new_list):
            if new_list[i] != ' ':
                i += 1
            else:
                new_list[i+3:len(new_list)] = new_list[i+1:len(new_list)-2]
                new_list[i:i+3] = ['%', '2', '0']
        return ''.join(new_list)

    def replaceSpace2(self, s):
        # write code here
        space_count = list(s).count(' ')
        if space_count == 0:
            return s
        new_list = list(s) + [' '] * (2*space_count)
        i, j = len(list(s))-1, len(new_list) - 1
        while i != j:
            if new_list[i] != ' ':
                new_list[j] = new_list[i]
                j -= 1
            else:
                new_list[j-2:j+1] = ['%', '2', '0']
                j -= 3
            i -= 1
        return ''.join(new_list)
