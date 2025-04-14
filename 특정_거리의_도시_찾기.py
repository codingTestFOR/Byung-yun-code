from collections import deque

# 테스트
# 케이스 1
# N, M, K, X = 4, 4, 2, 1
# graph =

# 입력
N, M, K, X = map(int, input().split())
graph = [[] for i in range(N + 1)]


for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)

distance = [-1] * (N + 1)
distance[X] = 0

q = deque([X])

print(distance)
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.appendleft(next_node)
    print(distance)

flag = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        flag = True


if not flag:
    print(-1)