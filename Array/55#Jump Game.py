# https://leetcode.com/problems/jump-game/description/

# 1 动态规划 由上至下
# Time OUT
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = [0] * len(nums)
        memo[-1] = 1
        def canJumpFromPosition(position, nums):
            if memo[position] != 0:
                return True if memo[position] == 1 else False
            furthestJump = min(position + nums[position], len(nums)-1)
            for i in range(position+1, furthestJump+1):
                if canJumpFromPosition(i, nums):
                    memo[position] = 1
                    return True
            memo[position] = -1
            return False
        return canJumpFromPosition(0, nums)
# 2 动态规划 自底向上
# Time Limit Exceeded
class Solution2:
    def canJump(self, nums):
        memo = [0] * len(nums)
        memo[-1] = 1
        for i in range(len(nums)-2,-1,-1):
            furthest = min(i + nums[i], len(nums) - 1)
            for j in range(i+1,furthest+1):
                if memo[j]==1:
                    memo[i]=1
                    break
        return memo[0]==1

# 3 贪心算法
class Solution3:
    def  canJump(self, nums):
        lastPos = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=lastPos:
                lastPos=i
        return lastPos==0

if __name__ == '__main__':
    t = Solution3()
    print(t.canJump([2,3,1,1,4]))
    print(t.canJump([3, 2, 1, 0, 4]))