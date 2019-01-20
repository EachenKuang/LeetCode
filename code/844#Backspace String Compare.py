class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def convert(string):
            stack = []
            for s in string:
                if s == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(s)
            return stack
        return convert(S) == convert(T)