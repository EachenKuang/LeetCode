# https://leetcode.com/problems/implement-stack-using-queues/description/
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack1.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack1[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self.stack1)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# 也可是使用deque双向队列
# from collections import deque
def __init__(self):
    """
    Initialize your data structure here.
    """
    self._queue = collections.deque()

def push(self, x):
    """
    Push element x onto stack.
    :type x: int
    :rtype: void
    """
    q = self._queue
    q.append(x)

def pop(self):
    """
    Removes the element on top of the stack and returns that element.
    :rtype: int
    """
    return self._queue.pop()

def top(self):
    """
    Get the top element.
    :rtype: int
    """
    return self._queue[-1]
    

def empty(self):
    """
    Returns whether the stack is empty.
    :rtype: bool
    """
    return len(self._queue) == 0 