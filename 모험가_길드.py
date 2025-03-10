n = input("n : ")
data = input('data : ')
data = list(map(int, data.split()))

data.sort()
print(data)

# 기본적으로 공포도 높은 사람은 마을에 버리는거임
count = 0   # 현재 그룹에 있는 모험가 수
result = 0  # 총 파티 수
for i in data:
    count += 1
    if count >= i:   # 그룹 내 인원 수가 이 사람의 공포도 보다 크거나 같다면
        result += 1  # 그룹 하나 증가
        count = 0    # 현재 그룹에 있는 모험가 수 초기화

print(result)