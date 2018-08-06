# -*- coding:utf-8 -*-


class Solution:
    # 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            # return self.Fibonacci(n-2) + self.Fibonacci(n-1)
            num1, num2 = 1, 1
            while n-3 > 0:
                num1, num2 = num2, num1+num2
                n -= 1
            return num1 + num2

if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(39))