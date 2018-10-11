# https://leetcode.com/problems/number-of-1-bits/description/
class Solution(object):
    # 1 编程之美上的题目
    # n&n-1每次都能够把最左边的1消去
    # 循环操作的步数为1的个数
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n>0:
            n&=n-1
            count+=1
        return count

    # 2 直接使用bin()函数然后使用str的count方法
    # 这样做直接使用了Python封装好的库，没有get到考察的点
    # 不推荐，单纯是炫技的one line Python code
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n)).count('1')

    # 3 利用移位操作来计算1的个数，每一位与1做且操作，如果为1则加1
    # 常规操作
    def hammingWeight(self, n):
        onesCount = 0
        
        while n > 0:
          if n & 0x1:
            onesCount += 1
          n = n >> 1

        return onesCount