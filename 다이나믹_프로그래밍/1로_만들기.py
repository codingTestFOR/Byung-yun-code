def solution(x):
    if x <= 3 or x == 5:  # 계산하지 않고 바로 출력
        return 1
    elif x == 4:
        return 2

    dp = [0] * (x + 1)

    # 미리 할당
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 1

    for i in range(6, x + 1):

        results = []
        if i % 5 == 0:
            results.append(int(i / 5))
        if i % 3 == 0:
            results.append(int(i / 3))
        if i % 2 == 0:
            results.append(int(i / 2))

        results.append(i -1)

        print(f">>> index : {i}")
        results.sort(key=lambda k:dp[k])
        print("results :",results)
        dp[i] = dp[results[0]] + 1
        print(dp[i])
    return dp[x]

print(solution(int(input())))

# 1 <= x <= 30000
# 시간 복잡도: O(n)
