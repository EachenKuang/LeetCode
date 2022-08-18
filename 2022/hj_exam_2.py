# 3
# 7
# 1 15
# 2 16
# 3 10
# 4 17
# 10 20
# 5 9
# 19 30

def cal(pairs, server_count) -> []:
    server_working_time = [0] * server_count  # 累计工作时间
    server_over_moment = [0] * server_count  # 结束时间
    for pair in pairs:
        start_time, duration = pair
        for index in range(server_count):
            if server_over_moment[index] <= start_time:
                # 如果结束时间在新任务的开始时间之前，说明可以进行
                server_over_moment[index] = start_time + duration # 更新结束时间
                server_working_time[index] += duration
                break
    ans = []
    max_working_time = max(server_working_time)
    for index, time in enumerate(server_working_time):
        if time == max_working_time:
            ans.append(index)
    return ans


if __name__ == '__main__':
    count = 3
    pairs = [
        [1, 15],
        [3, 10],
        [5, 6],
        [10, 20],
        [7, 13],
        [9, 17],
        [15, 20]
    ]
    pairs.sort(key=lambda a: a[0])
    print(pairs)
    print(cal(pairs, count))
