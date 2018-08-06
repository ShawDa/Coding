# -*- coding:utf-8 -*-


class Solution(object):
    """
    给定一个整数 (32位 有符整数型 )，请写出一个函数来检验它是否是4的幂。
    示例:当 num = 16 时 ，返回 true 。 当 num = 5时，返回 false。
    """
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 写成二进制,若只有一个偶数位为1,则是
        if num < 0:
            return False
        base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]
        mid = []
        while True:
            if num == 0: break
            num, rem = divmod(num, 2)
            mid.append(base[rem])
        print(mid[::-1])
        if mid.count('1') == 1 and mid.index('1') % 2 == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    num = -1
    obj = Solution()
    print(obj.isPowerOfFour(num))
    pass
