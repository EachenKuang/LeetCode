# https://leetcode.com/problems/can-place-flowers/description/
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        sum_0s = 0 
        sum_flowers = 0 
        flowerbed.append(1)
        for i in flowerbed:
            if i == 1:
                if sum_0s==0:
                    continue
                else:
                    sum_flowers+=(sum_0s-1)//2
                    sum_0s = 0                
            else:
                sum_0s+=1
        return n==sum_flowers