# 테스트 케이스 1
# N, M = 4, 5
# array = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

# 테스트 케이스 2
N, M = 5, 5
array = [[0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]]

# 입력
# N, M = list(map(int, input().split()))
# array = []
# for i in range(N):
#     array.append(input())

def mark(r,c):
    if r < 0 or r >= N or c < 0 or c >= M:    # 맵 밖으로 나가면 무시
        return False
    if array[r][c] == 1:                      # 얼음이 아니면 무시
        return False
    array[r][c] = 1                           # 벽으로 채우기

    # 주위를 벽으로 채우기
    mark(r+1, c)
    mark(r, c+1)
    mark(r-1, c)
    mark(r, c-1)

    return True


def debug_array():
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] == 1:
                print("□", end="")
            else:
                print('■', end="")
        print()

count = 0


# 초기 상태
print("초기 상태")
debug_array()


for row in range(len(array)):
    for col in range(len(array[row])):
        flag = mark(row, col)
        if flag:
            count += 1
            print("-----", count, "-----")
            debug_array()


print(count)
