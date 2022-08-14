import math

def cal(num):
    ans = []
    square = math.ceil(math.sqrt(num))  # 略大于或等于平方数的整数
    while num % 2 == 0:
        ans.append(2)
        num = num // 2
    for i in range(3, square, 2):
        while num % i == 0:
            ans.append(i)
            num = num // i
    if num > square:
        ans.append(num)
    return ans

if __name__ == '__main__':
    print(cal(1111))