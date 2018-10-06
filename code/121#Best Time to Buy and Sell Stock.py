# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
import sys
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 只做一次交易，需要保证找出最小值与最大值，且最小值在最大值之前。
        minPrice = sys.maxsize
        maxProfit = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            elif p-minPrice>maxProfit:
                maxProfit = p-minPrice
        return maxProfit