# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
#
# Example 1:
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
#
# Constraints:
#
# Methods pop, top and getMin operations will always be called on non-empty stacks.

# 保存两个stack,一个是原始的stack,一个用于保存最小值的stack，始终保持两个stack的值一一对应即可
# 这里也可是使用一个stack,每个元素使用(x,min)元组来表示即可
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], x))
        else:
            self.min_stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    assert minStack.stack == [-2]
    minStack.push(0)
    assert minStack.stack == [-2, 0]
    minStack.push(-3)
    assert minStack.stack == [-2, 0, -3]
    assert -3 == minStack.getMin() # return -3
    minStack.pop()
    assert minStack.stack == [-2, 0]
    assert 0 == minStack.top()    # return 0
    assert -2 == minStack.getMin() # return -2