def knapsack_dp(weights, values, capacity):
    n = len(weights)
    # Создаем таблицу dp размером (n+1) x (capacity+1), заполненную нулями
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    # Заполняем таблицу dp
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Если предмет помещается, выбираем максимальное значение:
                # либо не брать предмет, либо взять и добавить его ценность
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Если предмет не помещается, просто берем предыдущее значение
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


weights = [3, 1, 2, 1, 3]  # веса предметов: ноутбук, планшет, бинокль, книга
values = [3000, 1500, 1000, 500, 3500]  # ценности предметов
capacity = 5  # вместимость рюкзака
optimal_value = knapsack_dp(weights, values, capacity)
print(f"Оптимальная ценность (DP): {optimal_value}")
