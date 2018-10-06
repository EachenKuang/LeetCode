# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution:
    # 1 峰值 谷值相减法
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        i = 0
        valley = peak = prices[0]
        maxProfit = 0
        while i < len(prices)-1:
            while i<len(prices)-1 and prices[i]>=prices[i+1]:
                i+=1
            valley = prices[i]
            while i<len(prices)-1 and prices[i]<=prices[i+1]:
                i+=1
            peak = prices[i]
            maxProfit += peak - valley
        return maxProfit
    # 2 直接增加
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]       
        return maxProfit
