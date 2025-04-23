from collections import deque

N, K = list(map(int, input().split()))
first = list(map(int, (input().split())))
second = list(map(int, (input().split())))


first.sort()
second.sort()

final = deque(first)

# 바꾸기
for i in range(K):
    final.popleft()
    final.append(second.pop())

print(sum(final))
