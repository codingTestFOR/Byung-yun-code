"""
n, k = (10, 4200)
coins = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
"""

# 입력
n, k = list(map(int, input().split()))  # 10 4200

coins = []
for i in range(n):
    coins.append(input())

coins = list(map(int, coins))  # [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

# 계산
coins.sort(reverse=True)  # [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

count = 0  # 동전 개수
for i in coins:
    count += k // i
    k %= i

print(count)