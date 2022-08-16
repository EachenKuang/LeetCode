def del_least_char(s: str):
    # 先计算字符串中的个数
    str_count = dict()
    for i in s:
        if i in str_count:
            str_count[i] += 1
        else:
            str_count[i] = 1
    min_count = min(str_count.values())
    ans = ""
    for c in s:
        if str_count[c] != min_count:
            ans += c
    return ans

if __name__ == '__main__':
    print(del_least_char("aabcddd"))