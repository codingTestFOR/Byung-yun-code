from collections import deque


"""

# 테스트 케이스

N = 3
K = 3
graph = [[1, 0, 2],
         [0, 0, 0],
         [3, 0, 0]
]

S, target_x, target_y = 2, 3, 2
for r in range(N):
    for c in range(N):
        if graph[r][c] != 0:
            virus_data.append((graph[r][c], 0, r, c))

"""

# --입력--
# graph         : 그래프
# virus_data    : 바이러스만 따로 보관, (바이러스 종류, 시간, X, Y)
# N             : 정사각형 그래프 크기
# K             : 바이러스의 종류 ( 사실 필요 없음 )

graph = []
virus_data = []

N, K = map(int, input().split())

for r in range(N):  # 그래프에 바이러스 입력
    graph.append(list(map(int, input().split())))
    for c in range(N):
        if graph[r][c] != 0:
            virus_data.append((graph[r][c], 0, r, c))  # 0 : 0초부터 시작



virus_data.sort()  # 낮은 바이러스부터 실행하기 위해서
que = deque(virus_data)

target_second, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지의 위치
delta_x = [-1, 0, 1, 0]
delta_y = [0, 1, 0, -1]

# --BFS--
while que:
    virus, second, x, y = que.popleft()

    if second == target_second:  # 시간 지나면 끝
        break

    for d in range(4):  # 현재 노드에서 주변 4가지 위치를 각각 확인
        new_x = x + delta_x[d] + 1
        new_y = y + delta_y[d] + 1
        if 1 <= new_x and new_x <= N and 1 <= new_y and new_y <= N:  # 그래프를 벗어나지 않았다면?
            if graph[new_x-1][new_y-1] == 0:  # 다른 바이러스가 점령하지 않았다면?
                graph[new_x-1][new_y-1] = virus              # 점령

                if new_x == target_x and new_y == target_y:  # 목표를 점령하면 더이상 계산할 필요 없음
                    break

                que.append((virus, second + 1, new_x-1, new_y-1))  # 큐에 1초 증가한 새로운 바이러스 넣기


print(graph[target_x - 1][target_y - 1])
