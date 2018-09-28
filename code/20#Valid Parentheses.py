class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == "}" or i == "]" or i == ")":
                if not stack:
                    return False
                if i=="}" and stack[-1] == "{" or i=="]" and stack[-1] == "[" or i==")" and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack

                