# https://leetcode.com/problems/trapping-rain-water/description/
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

# 1
# 思路：可以一次算一层
# 对于 [0,1,0,2,1,0,1,3,2,1,2,1]
# 第一层： 只有index为2与index为5的两个坑有水 +2
# 充水一层后：[0,1,1,2,1,1,1,3,2,1,2,1]
# 将第一层减去后：[0,0,0,1,0,0,0,2,1,0,1,0]
# 第二层： 只有index为3,4,5和8的4个坑有水 +2
# 充水一层后：[0,0,0,1,1,1,1,2,1,1,1,0]
# 将第二层减去后：[0,0,0,0,0,0,0,1,0,0,0,0]
# 最后可以充水6

# 2

class Solution:
    # 1
    # O(n^2)
    # 暴力法
    # 对于每个柱子找左右两边最大的柱子作为存水
    # TLE
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        size = len(height)
        for i in range(size-1):
            max_l = max_r = 0
            for j in range(i,-1,-1):
                max_l = max(max_l, height[j])
            for j in range(i,size):
                max_r = max(max_r, height[j])
            ans += min(max_r,max_l)-height[i]
        return ans
    # 2
    # 动态规划使用数组保存
    # O(n)
    # O(n)
    def trap2(self, height):
        if not height:
            return 0
        ans = 0
        size = len(height)
        left_max = [0]*size
        right_max = [0]*size
        left_max[0] = height[0]
        for i in range(1,size):
            left_max[i] = max(height[i], left_max[i-1])
        right_max[-1] = height[-1]
        for i in range(size-2,-1,-1):
            right_max[i] = max(height[i],right_max[i+1])
        for i in range(1,size):
            ans += min(left_max[i], right_max[i])-height[i]
        return ans
    # 3
    def trap3(self, height):
        ans = current = 0
        stack = []
        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if len(stack)==0:
                    break
                distance = current - stack[-1] -1
                bounded_height = min(height[current], height[stack[-1]])-height[top]
                ans += distance * bounded_height
            current += 1
            stack.append(current)
        return ans

    def trap4(self, height):
        areas = 0
        max_l = max_r = 0
        l = 0
        r = len(height)-1
        while l < r:
            if height[l] < height[r]:
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    areas += max_l - height[l]
                l +=1
            else:
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    areas += max_r - height[r]
                r -= 1
        return areas