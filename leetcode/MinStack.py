# -*- coding:utf-8 -*-


class MinStack(object):
    """
    设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
    push(x) -- 将元素 x 推入栈中。
    pop() -- 删除栈顶的元素。
    top() -- 获取栈顶元素。
    getMin() -- 检索栈中的最小元素。
    示例:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.getMin();   --> 返回 -2.
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.miniStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.miniStack.append(x)
        return True

    def pop(self):
        """
        :rtype: void
        """
        try:
            self.miniStack.pop(-1)
        except Exception:
            return False
        return True

    def top(self):
        """
        :rtype: int
        """
        return self.miniStack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.miniStack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # 返回 -3.
    minStack.pop()
    print(minStack.top())  # 返回 0.
    print(minStack.getMin())  # 返回 -2.