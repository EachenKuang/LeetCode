# 描述
# 任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。

# 数据范围：输入的数据满足 4≤n≤1000 
# 输入描述：
# 输入一个大于2的偶数

# 输出描述：
# 从小到大输出两个素数


def cal_susu_pair(num: int):
    if num == 4:
        return [2, 2]
    half = num // 2
    for i in range(half, 3, -1):
        if is_susu(i) and is_susu(num-i):
            return [i, num-i]



def is_susu(num):
    if num == 2 or num == 3:
        return True
    bound = int(num ** 0.5)
    for i in range(2, bound + 1):
        if num % i == 0:
            return False
    return True

input_nums = [20, 30, 100, 1000]
for i in input_nums:
    print(cal_susu_pair(i))