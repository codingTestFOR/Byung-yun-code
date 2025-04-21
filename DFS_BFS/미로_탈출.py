from collections import deque

N, M = 5, 6  # 탈출구
graph = [[1, 0, 1, 1, 1, 0],
         [1, 0, 1, 0, 1, 1],
         [1, 0, 1, 0, 0, 1],
         [1, 0, 1, 0, 0, 1],
         [1, 1, 1, 0, 0, 1]]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 1 or new_x > N or new_y < 1 or new_y > M:
                continue
            if graph[new_x - 1][new_y - 1] == 0:
                continue
            if graph[new_x-1][new_y-1] == 1:
                graph[new_x - 1][new_y - 1] = graph[x - 1][y - 1] + 1
                queue.append((new_x, new_y))

    return graph[N-1][M-1]


print(bfs(1, 1))


for i in graph:
    for j in i:
        print(j, end="\t")
    print()
