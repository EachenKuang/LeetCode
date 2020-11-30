# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
#
# 示例 1：
#
# 输入：s = "We are happy."
# 输出："We%20are%20happy."
#
# 限制：
#
# 0 <= s 的长度 <= 10000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
class Solution:
    def replaceSpace(self, s: str) -> str:
        """
        第一种方法
        replace 年轻人不讲武德啊
        """
        return s.replace(" ", "%20")

    def replaceSpace2(self, s: str) -> str:
        """
        第二种方法
        """
        new_str_list = []
        for i in s:
            if i == " ":
                new_str_list.append("%20")
            else:
                new_str_list.append(i)
        return "".join(new_str_list)


if __name__ == '__main__':
    solution = Solution()
    input_items = "We are happy."
    output_items = solution.replaceSpace(input_items)
    assert output_items == "We%20are%20happy."
    output_items2 = solution.replaceSpace2(input_items)
    assert output_items2 == "We%20are%20happy."
