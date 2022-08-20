def tab(a):
    # minus_count = 0

    # for i in range(1, nums):
    #     if i < 0:
            
    # nums = [i-nums[0]  for i in nums]
    # ans = 0
    # for i in range(1, len(nums)):
    #     if nums[i] > nums[i-1]:
    #         ans += nums[i] - nums[i-1]
    # return ans + minus_count
    ans = 0
    for i in range(1, len(a)):
        if a[i] >= a[i-1]:
            ans += a[i] - a[i-1]
    return ans


print(tab([1,2,3,2,1]))
print(tab([2,3,3,0,2,1]))
print(tab([0, 1, 2, 0, 2, 4, 2, 1, 0]))
print(tab([0, 0]))
print(tab([1, 1, 1, 0, 11]))
print(tab([8,8]))

# 9
# 0 1 2 0 2 4 2 1 0

# while True:
#     try:
#         n = int(input())
#         nums = map(int, input().split())
#         print(tab(nums))
#     except:
#         break