# https://www.nowcoder.com/practice/7960b5038a2142a18e27e4c733855dac?tpId=37&tqId=21244&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D2%26page%3D1%26pageSize%3D100%26search%3D%26tpId%3D37%26type%3D37&difficulty=2&judgeStatus=undefined&tags=&title=
# 描述
# 现在有一种密码变换算法。
# 九键手机键盘上的数字与字母的对应： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0，
# 把密码中出现的小写字母都变成九键键盘对应的数字，如：a 变成 2，x 变成 9.
# 而密码中出现的大写字母则变成小写之后往后移一位，如：X ，先变成小写，再往后移一位，变成了 y ，例外：Z 往后移是 a 。
# 数字和其它的符号都不做变换。
# 数据范围： 输入的字符串长度满足 1 \le n \le 100 \1≤n≤100
# 输入描述：
# 输入一组密码，长度不超过100个字符。
#
# 输出描述：
# 输出密码变换后的字符串
#
# 示例1
# 输入：
# YUANzhi1987
# 输出：
# zvbo9441987

mapping = "22233344455566677778889999"


def transfer(v: str):
    if v.isupper():
        # 大写字母
        return chr((ord(v.lower()) - ord('a') + 1) % 26 + ord('a'))
    elif v.islower():
        return mapping[ord(v) - ord('a')]
    return v


def transfer_str(s: str):
    ans = []
    for i in s:
        temp = transfer(i)
        ans.append(temp)
    return "".join(ans)


if __name__ == '__main__':
    print(transfer_str("YUANzhi1987"))