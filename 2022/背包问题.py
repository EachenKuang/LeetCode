weights = [2, 3, 4]
values = [15, 20, 30]
bag_weight = 5


def zero_one_bag1(weights, values, bag_weight):
    """
    使用数组保存动态规划
    """
    rows, cols = len(weights), bag_weight + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # 初始化dp数组.
    for i in range(rows):
        dp[i][0] = 0
    first_item_weight, first_item_value = weights[0], values[0]
    for j in range(1, cols):
        if first_item_weight <= j:
            dp[0][j] = first_item_value

    # 更新dp数组: 先遍历物品, 再遍历背包.
    for i in range(1, rows):
        cur_weight, cur_val = weights[i], values[i]
        for j in range(1, cols):
            if cur_weight > j:  # 说明背包装不下当前物品.
                dp[i][j] = dp[i - 1][j]  # 所以不装当前物品.
            else:
                # 定义dp数组: dp[i][j] 前i个物品里，放进容量为j的背包，价值总和最大是多少。
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight] + cur_val)
    return dp


def zero_one_bag2(weights, values, bag_weight):
    """
    滚动数组
    """
    rows, cols = len(weights), bag_weight + 1
    dp = [0] * cols
    for j in range(weights[0], bag_weight + 1):
        dp[j] = values[0]
    for i in range(1, rows):
        for j in range(bag_weight, weights[i] -1, -1):
            dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
    return dp

def zero_one_bag3(weights, values, bag_weight):
    """
    完全背包
    """
    rows, cols = len(weights), bag_weight + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # 初始化dp数组.
    # for i in range(rows):
    #     dp[i][0] = 0
    first_item_weight, first_item_value = weights[0], values[0]
    for j in range(1, cols):
        # temp = j
        # while temp >= first_item_weight:
        #     dp[0][j] += first_item_value
        #     temp -= first_item_weight
        count = j // first_item_weight
        dp[0][j] += first_item_value * count

    # 更新dp数组: 先遍历物品, 再遍历背包.
    for i in range(1, rows):
        cur_weight, cur_val = weights[i], values[i]
        for j in range(1, cols):
            if cur_weight > j:  # 说明背包装不下当前物品.
                dp[i][j] = dp[i - 1][j]  # 所以不装当前物品.
            else:
                # 定义dp数组: dp[i][j] 前i个物品里，放进容量为j的背包，价值总和最大是多少。
                # 枚举每件物品取k次的情况
                for k in range(1, j//cur_weight + 1):
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight * k] + cur_val * k)
    return dp


if __name__ == '__main__':
    print(zero_one_bag1(weights, values, bag_weight))
    print(zero_one_bag2(weights, values, bag_weight))
    print(zero_one_bag3(weights, values, bag_weight))