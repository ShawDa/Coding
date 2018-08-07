# -*- coding:utf-8 -*-

class Solution:
    # 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示
    # 正数的补码和原码相同，负数的补码为除了第一位符号位之外，其他位0变1,1变0，并且最后再加1
    def NumberOf1(self, n):  # 32位
        # write code here
        if n >= 0:
            print(bin(n).count('1'))
        else:
            print(bin(n & 0xffffffff).count('1'))
        if n < 0:
            n = n & 0xffffffff
        count = 0
        while n:  # n与n-1相与，位数都为1则为1,这样会少个1
            n = n & (n - 1)
            # print(n)
            count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(100 & 0xffffffff)
    print(s.NumberOf1(1000))