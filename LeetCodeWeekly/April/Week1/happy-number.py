# Write an algorithm to determine if a number n is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay), or it loops endlessly
# in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Return True if n is a happy number, and False if not.
#
# Example:
#
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# 方法，递归运算，但是有可能会造成死循环，这里可以增加一个层数的计数，比如超过n层退出循环（不可取，如果数字极大，那可能要多层）
# 方法 记录过程中的数字，如果出现重复数字，那说明是不可能是 happy number（理想的方法）
class Solution:

    def num_to_list(self, num: int):
        return list(str(num))

    def list_to_squares(self, num_list: [str]):
        return sum(int(num) ** 2 for num in num_list)

    def isHappy(self, n: int) -> bool:
        current_num = n
        history_num = []
        while current_num != 1:
            history_num.append(current_num)  # 保存历史数字
            current_num = self.list_to_squares(self.num_to_list(current_num))  # 计算出新的数字
            if current_num in history_num:
                return False
        return True


# 优化版
class Solution1:

    def square_sum(self, num):
        sum = 0
        while num:
            last_digit = num % 10
            sum = sum + last_digit ** 2
            num = num // 10
        return sum

    def isHappy(self, n: int) -> bool:
        current_num = n
        history_num = dict()
        while current_num != 1:
            history_num[current_num] = 1  # 保存历史数字
            current_num = self.square_sum(current_num)  # 计算出新的数字
            if current_num in history_num:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    assert solution.isHappy(19) is True
    assert solution.isHappy(4) is False
    solution1 = Solution1()
    assert solution1.isHappy(19) is True
    assert solution1.isHappy(4) is False
