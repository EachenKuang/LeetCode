while True:
    try:
        n = int(input())
        ans = dict()
        for _ in range(n):
            k, v = map(int, input().split())
            if k in ans:
                ans[k] += v
            else:
                ans[k] = v
        keys = ans.keys()
        keys.sort()
        for k in keys:
            print(k, ans[k])
    except:
        break