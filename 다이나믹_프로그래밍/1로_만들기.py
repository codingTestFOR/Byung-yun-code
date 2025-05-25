import time

def solution(x):
    if x <= 3 or x == 5:
        return 1
    elif x == 4:
        return 2

    dp = [0] * (x + 1)
    dp[1] = dp[2] = dp[3] = 1
    dp[4] = 2
    dp[5] = 1

    for i in range(6, x + 1):
        candidates = []
        if i % 5 == 0:
            candidates.append(i // 5)
        if i % 3 == 0:
            candidates.append(i // 3)
        if i % 2 == 0:
            candidates.append(i // 2)
        candidates.append(i - 1)

        # 이전 dp 값이 가장 작은 경로 선택
        best = min(candidates, key=lambda k: dp[k])
        dp[i] = dp[best] + 1

    return dp[x]

if __name__ == '__main__':
    print(solution(int(input())))


    # 시간 복잡도 테스트
    # xs = [26, 9999, 30000]
    # print(f"{'x':>8} | {'time (s)':>10} | {'result':>6}")
    # print("-" * 30)
    #
    # for x in xs:
    #     start = time.perf_counter()
    #     res = solution(x)
    #     elapsed = time.perf_counter() - start
    #     print(f"{x:8d} | {elapsed:10.6f} | {res:6d}")
