def cal(m, n):
    """
    求 Cn m+n
    """
    return factorial(m+n) // (factorial(m) * factorial(n))
    

def factorial(n):
    """
    求阶乘
    """
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

    