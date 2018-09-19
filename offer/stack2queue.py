# -*- coding:utf-8 -*-


class Solution:
    # 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx  如果出栈没了，就把入栈的全加入出栈
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()