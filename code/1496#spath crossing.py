# https://leetcode.cn/problems/path-crossing/
# 给你一个字符串 path，其中 path[i] 的值可以是 'N'、'S'、'E' 或者 'W'，分别表示向北、向南、向东、向西移动一个单位。

# 你从二维平面上的原点 (0, 0) 处开始出发，按 path 所指示的路径行走。

# 如果路径在任何位置上与自身相交，也就是走到之前已经走过的位置，请返回 true ；否则，返回 false 。





class Solution:
    def isPathCrossing(self, path: str) -> bool:
        start_x = 0
        start_y = 0
        roads = {(0,0)}
        for i in path:
            if i == "N":
                start_y += 1
            elif i == "S":
                start_y -= 1
            elif i == "E":
                start_x += 1
            elif i == "W":
                start_x -= 1
            temp = (start_x, start_y)
            if temp in roads:
                return True
            else:
                roads.add(temp)
        return False

def main():
    solution = Solution()
    print(solution.isPathCrossing("NESWW"))

main()



