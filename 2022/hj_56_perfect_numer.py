# 描述
# 完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。

# 它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。

# 例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。

# 输入n，请输出n以内(含n)完全数的个数。

# 数据范围： 1 \le n \le 5 \times 10^{5} \1≤n≤5×10 
# 5
  
# 输入描述：
# 输入一个数字n

# 输出描述：
# 输出不超过n的完全数的个数

from json.tool import main


def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    return num in (6,28,496,8128,33550336)
# 2 常规法
def checkPerfectNumber(num):
    if num <= 1:
        return False
    res = 1
    bound = int(num**0.5)
    i = 2
    while i <= bound:
        if num%i==0:
            res += i + num//i
            bound = min(bound,num//i)
        if res>num:
            return False
        i+=1
    if res==num:
        return True
    return False

from collections import Count 