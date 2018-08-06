# -*- coding:utf-8 -*-


class Solution:
    # 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
    def rectCover(self, number):
        # write code here
        if number <= 0:
            return False
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            # return self.rectCover(number-1) + self.rectCover(number-2)
            num1, num2 = 1, 2
            for i in range(2, number):
                num1, num2 = num2, num2+num1
            return num2


if __name__ == '__main__':
    s =Solution()
    print(s.rectCover(3))