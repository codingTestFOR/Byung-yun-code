n = int(input())  # 1 < n < 1000
price = 1000 - n
coins = [500, 100, 50, 10, 5, 1]
count = 0
for i in coins:
    count += price // i
    price %= i

print(count)