# https://leetcode.com/problems/robot-return-to-origin/description/
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('L')==moves.count('R') and moves.count('U')==moves.count('D')