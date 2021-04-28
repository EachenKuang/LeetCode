# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#
#  
#
# 示例 1：
#
# 输入：m = 2, n = 3, k = 1
# 输出：3
# 示例 2：
#
# 输入：m = 3, n = 1, k = 0
# 输出：1
# 提示：
#
# 1 <= n,m <= 100
# 0 <= k <= 20
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof


def digit_sum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """
        递推法
        这里需要注意，所有的可能题解都是联通的，只需要考虑向右或者向下的情况。
        """
        vis = {(0, 0)}
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digit_sum(i) + digit_sum(j) <= k:
                    vis.add((i, j))
        return len(vis)

    def movingCount_2(self, m: int, n: int, k: int) -> int:
        """
        广度优先法
        """
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digit_sum(x) + digit_sum(y) <= k:
                s.add((x, y))
                q.put((x + 1, y))
                q.put((x, y + 1))
        return len(s)

