# Алгоритм Вагнера — Фишера
def levenshtein_distance(line1, line2):
    dp = [[0] * (len(line2) + 1) for _ in range((len(line1) + 1))]
    for i in range(len(line1) + 1):
        for j in range(len(line2) + 1):
            if i == j == 0:
                dp[i][j] = 0
            elif j == 0 and i > 0:
                dp[i][j] = i
            elif i == 0 and j > 0:
                dp[i][j] = j
            else:
                diff_char = (1 if line1[i - 1] != line2[j - 1] else 0)
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # Вставка
                    dp[i][j - 1] + 1,  # Удаление
                    dp[i - 1][j - 1] + diff_char  # Замена
                )
    return dp[len(line1)][len(line2)]


print(levenshtein_distance('abcde', 'yaxdb'))
print(levenshtein_distance('exponential', 'polynomial'))
