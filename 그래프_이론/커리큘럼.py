from collections import deque
import copy

v = int(input())

indegree = [0] * (v +1)              # 진입 차수
time = [0] * (v + 1)                 # 시간 정보
graph = [[] for i in range(v + 1)]   # 간선 정보

# 입력
for i in range(1, v +1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:  # 강의 번호, -1 제외
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    result = copy.deepcopy(time)  # list는 mutable이므로 deepcopy
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    # 출력
    for i in range(1, v + 1):
        print(result[i])


if __name__ == "__main__":
    topology_sort()



