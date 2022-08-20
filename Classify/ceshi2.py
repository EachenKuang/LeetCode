# # 先要排序，到达时间，计算完成时间，然后计算最终的消息负载的数量，然后排序
# server_count = int(input())
# message_count = int(input())
# pairs = [] # [[time_stop, over_time]]
# for i in range(message_count):
#     pairs.append(list(map(int, input().split())))


# pairs.sort(key=lambda a: a[0])



# def cal(server_count, message_count, pairs):
#     # server_work_time = [0] * server_count # 运行使用时间
#     # server_in_sleeping = [True] * server_count # 是否空闲
#     # server_current_work_left = [0] * server_count # 还剩多少时间可以结束当前任务

#     # last_time = pairs[0][0]
#     # last_buffer = pairs[0][1]

#     end_time = [0] * server_count # 结束时间
#     work_time = [0] * server_count # 累计运行使用时间

#     for pair in pairs:
#         using = False
#         for i in range(server_count):
#             if end_time[i] < pair[0]:
#                 end_time[i] = pair[0] + pair[1]
#                 work_time[i] += pair[1]
#                 using = True
#                 break
#         if not using:
#             continue
    
#     max_count = max(work_time)
#     ans = []
#     for i in range(server_count):
#         if work_time[i] == max:
#             ans.append(i)
#     return ans


def cal(server_count, message_count, pairs):
    end_time = [0] * server_count # 结束时间
    work_time = [0] * server_count # 累计运行使用时间

    for pair in pairs:
        using = False
        for i in range(server_count):
            if end_time[i] <= pair[0]:
                end_time[i] = pair[0] + pair[1]
                work_time[i] += pair[1]
                using = True
                break
        if not using:
            continue
    
    max_count = max(work_time)
    ans = []
    for i in range(server_count):
        if work_time[i] == max_count:
            ans.append(i)
    return ans

# 先要排序，到达时间，计算完成时间，然后计算最终的消息负载的数量，然后排序
server_count = int(input())
message_count = int(input())
pairs = [] # [[time_stop, over_time]]
for i in range(message_count):
    pairs.append(list(map(int, input().split())))


pairs.sort(key=lambda a: a[0])
ans = cal(server_count, message_count, pairs)
print(ans)


