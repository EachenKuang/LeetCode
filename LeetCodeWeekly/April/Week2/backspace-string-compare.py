# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a
# backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:
#
# Can you solve it in O(N) time and O(1) space?
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.parse(S) == self.parse(T)

    def parse(self, s: str) -> []:
        res_str_list = []
        for i in s:
            if i == '#':
                if res_str_list:
                    res_str_list.pop()
            else:
                res_str_list.append(i)
        return res_str_list


class Solution2:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.backspace(S) == self.backspace(T)
    def backspace(self, string):
        length = len(string)
        restring = ''
        spaces = 0
        for i in range(length-1 , -1, -1):
            if string[i] == '#':
                spaces += 1
            else:
                if spaces == 0:
                    restring = string[i] + restring
                else:
                    spaces -= 1
        return restring


if __name__ == '__main__':
    solution = Solution()
    assert solution.backspaceCompare("a##c", "#a#c")
    solution2 = Solution2()
    assert solution2.backspaceCompare("a##c", "#a#c")