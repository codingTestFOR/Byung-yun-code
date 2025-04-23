# 입력
N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

# 연산
NUMBERS = numbers.sort(reverse=True)

print(" ".join(map(str, numbers)))

