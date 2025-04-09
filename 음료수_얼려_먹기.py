# 테스트 케이스
N, M = 5, 5
array = ["11011","10100","10100","00000","01011"]

# 입력
# N, M = list(map(int, input().split()))
# array = []
# for i in range(N):
#     array.append(input())

count = 0  # 얼음의 총 개수

# 계산
for row in array:
    ices = []  # 얼음 위치를 기억할 리스트
    for idx in range(len(row)):
        if row[idx] == "1":
            ices.append(idx)
    print(ices)




