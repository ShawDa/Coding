# -*- coding:utf-8 -*-


class Solution(object):
    """
    写一个程序，输出从 1 到 n 数字的字符串表示。
    1. 如果 n 是3的倍数，输出“Fizz”；
    2. 如果 n 是5的倍数，输出“Buzz”；
    3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
    示例：
    n = 15,
    返回:
    [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
    """
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return_list = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 != 0:
                return_list.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                return_list.append("Buzz")
            elif i % 3 == 0 and i % 5 == 0:
                return_list.append("FizzBuzz")
            else:
                return_list.append(str(i))
        return return_list


if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15))