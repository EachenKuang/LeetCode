# 输入一个字符串，打印出该字符串中字符的所有排列。
#
#  
#
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#
#  
#
# 示例:
#
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        """
        利用内置的库完成排序
        需要去重
        """
        from itertools import permutations
        return list(set(("".join(item)for item in permutations(s))))

    def permutation_2(self, s: str) -> List[str]:
        """
        dfs()
        """
        c, res = list(s), []

        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))  # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:
                    continue  # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)  # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换

        dfs(0)
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.permutation("abb"))

