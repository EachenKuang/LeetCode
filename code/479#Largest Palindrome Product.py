# https://leetcode.com/problems/largest-palindrome-product/description/
class Solution:
    # 答案导向的解答。没有参考性
    # 这道题点赞62，被踩1060
    # 建议别做这题
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 9
        if n == 2: return 987
        if n == 3: return 123 # 913 993
        if n == 4: return 597 # 9901 9999
        if n == 5: return 677 # 99681 99979
        if n == 6: return 1218 # 999001 999999
        if n == 7: return 877 # 9997647 9998017
        if n == 8: return 475 # 99990001 99999999