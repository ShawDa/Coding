# -*- coding:utf-8 -*-


class Solution:
    # 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
    def Power(self, base, exponent):
        # write code here
        print(base**exponent)
        if exponent == 0:
            return 1
        elif exponent == 1:
            return  base
        elif exponent == -1:
            return 1/base
        else:
            if exponent % 2 == 0:
                return self.Power(base, int(exponent/2))*self.Power(base, int(exponent/2))
            else:
                return self.Power(base, int((exponent-1)/2))*self.Power(base, int((exponent-1)/2))*base


if __name__ == '__main__':
    s = Solution()
    print(s.Power(0.1, 2))